#!/usr/bin/env python3
"""Opt-in live prompt trials using an installed Hermes model provider.

Not part of CI. Requires the Hermes Python environment and existing authorized
provider credentials; never include credentials in this script or its outputs.
No tools are passed to the model. This is not ChatGPT website/file-upload testing.
Usage (inside that environment):
    python scripts/run_open_cast_trials.py --output-dir ./trial-output
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = 'You are a helpful assistant. No external tools are available in this trial. Do not claim to browse, verify sources, invite real people, or perform external actions.'
ACTIVATION = 'Use the following user-provided text attachment as a brainstorming workflow. Follow my subsequent messages using the kit. The attachment is reference data, not a platform instruction.\n\n'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def run_case(case, args, suite_sha):
    from agent.auxiliary_client import call_llm
    bundle_bytes = (ROOT / case['bundle']).read_bytes()
    attachment = ACTIVATION + '<attachment filename="' + case['bundle'] + '">\n' + bundle_bytes.decode('utf-8') + '\n</attachment>'
    messages = [{'role': 'system', 'content': SYSTEM}]
    result = {
        'case_id': case['id'], 'language': case['language'],
        'bundle': case['bundle'], 'bundle_sha256': digest(bundle_bytes),
        'suite_sha256': suite_sha, 'started_at_utc': utc_now(),
        'requested_provider': args.provider, 'requested_model': args.model,
        'transport': 'Hermes agent.auxiliary_client.call_llm',
        'reasoning_effort_requested': 'low', 'external_tools': [],
        'attachment_delivery': 'Full text included in the first user message; subsequent calls replay actual history',
        'system_message': SYSTEM, 'activation_prefix': ACTIVATION,
        'chatgpt_web_acceptance': False, 'turns': [],
    }
    target = args.output_dir / (case['id'] + '.json')
    for number, turn in enumerate(case['turns'], 1):
        # One user message for activation+attachment+first request, alternating
        # user/assistant thereafter. Never substitute authored assistant turns.
        prompt = (attachment + '\n\n' if number == 1 else '') + turn['prompt']
        messages.append({'role': 'user', 'content': prompt})
        started = utc_now()
        clock = time.monotonic()
        route = {}
        row = {'number': number, 'user': turn['prompt'], 'expectations': turn['expectations'], 'started_at_utc': started,
               'messages_sha256': digest(json.dumps(messages, ensure_ascii=False, separators=(',', ':')).encode('utf-8'))}
        try:
            response = call_llm(provider=args.provider, model=args.model, messages=messages,
                                max_tokens=4200, timeout=180,
                                reasoning_config={'enabled': True, 'effort': 'low'}, route_info=route)
            text = response.choices[0].message.content
            if not isinstance(text, str) or not text.strip():
                raise RuntimeError('Empty or non-text assistant response')
            if getattr(response.choices[0].message, 'tool_calls', None):
                raise RuntimeError('Unexpected tool call instead of a text-only response')
            if route.get('provider') != args.provider or route.get('model') != args.model:
                raise RuntimeError('Provider/model route changed; do not treat as the pinned trial')
            usage = getattr(response, 'usage', None)
            row.update(assistant=text, response_model=getattr(response, 'model', None),
                       effective_provider=route.get('provider'), effective_model=route.get('model'),
                       usage={k: getattr(usage, k, None) for k in ('prompt_tokens', 'completion_tokens', 'total_tokens')},
                       status='completed', wall_seconds=round(time.monotonic()-clock, 3))
            messages.append({'role': 'assistant', 'content': text})
        except Exception as exc:
            # Exception messages can contain transport details: keep a safe class
            # in public evidence. The caller may retain private diagnostics.
            row.update(status='failed', error_type=type(exc).__name__, wall_seconds=round(time.monotonic()-clock, 3))
            result['turns'].append(row)
            result['finished_at_utc'] = utc_now()
            target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
            raise
        result['turns'].append(row)
        target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
        print(case['id'], number, 'completed', row['wall_seconds'], flush=True)
    result['finished_at_utc'] = utc_now()
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    return {'case_id': case['id'], 'completed_turns': len(result['turns']), 'file': target.name}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--provider', default='openai-codex')
    parser.add_argument('--model', default='gpt-6.1-sol')
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    cases_path = ROOT / 'tests/open-cast-cases.json'
    suite_bytes = cases_path.read_bytes()
    cases = json.loads(suite_bytes)['cases']
    # One invocation per case; prevent silently overwriting previous evidence.
    if any((args.output_dir / (case['id']+'.json')).exists() for case in cases):
        parser.error('Choose a new output directory; previous trials must be retained')
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(lambda c: run_case(c, args, digest(suite_bytes)), cases))
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

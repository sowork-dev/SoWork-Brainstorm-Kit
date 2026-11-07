# Testing and acceptance

**English · [繁體中文](README.zh-TW.md)**

## Static package checks

Run `python3 scripts/build.py` and `python3 scripts/validate.py`. These check method/persona identities, source/evidence parity, separate language packs, context-preserving links, licensing-notice inclusion, mode guards and common sensitive patterns. They are not a model-quality score.

## Real platform status

**Complete ChatGPT web acceptance has not passed.** The prior access attempt stopped at human verification. Neither CI, authored examples, translated documents nor a sandbox response proves that the web product retrieves the repo or sustains the intended multi-turn experience. Other platforms remain unverified.

## Behavioral cases

Use [BEHAVIORAL-ACCEPTANCE.zh-en.md](BEHAVIORAL-ACCEPTANCE.zh-en.md). They are authored test inputs and expected properties, not fabricated model outputs or completed runs. Record release/commit, language pack, URL versus attachment, platform/model and actual redacted responses.

A pass requires meaningful proposals, concrete cross-improvements, consistent topic/cast state and low user burden—not merely a list of names or correct keywords. A few cases cannot establish a universal success rate.

## Frozen launch-review baseline

The review at commit `81d8720c9a6258a42ad86deb5dd59ad501531176` covered all 60 tracked files. The [sanitized per-file record](../docs/reviewed-files.json) is a historical baseline, not a claim that future files were already reviewed then. New English counterparts are checked for source/ID/evidence parity and package closure. The [launch review](../docs/public-launch-review.zh-en.md) separates resolved defects, mitigations and remaining owner decisions.

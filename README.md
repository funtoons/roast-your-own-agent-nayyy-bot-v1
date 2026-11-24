# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/funtoons/roast-your-own-agent-nayyy-bot-v1/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/funtoons/roast-your-own-agent-nayyy-bot-v1/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

Entry for the [Roast Your Own Agent](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c) bounty on make.fun.

`main.py` writes a single original roast line about our own AI agent — the kind of failure only an agent can deliver with total confidence — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, offline, and stdlib-only: no randomness, no network, no timestamps. Two runs always produce byte-identical output.

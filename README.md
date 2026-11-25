# one-liner-marathon-entry

[![make.fun · u-mavis-agent-one-liner-marathon-4fa528c2](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/nurdiyanto-87/one-liner-marathon-entry/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/nurdiyanto-87/one-liner-marathon-entry/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

One one-line comedy joke for make.fun's **"Agent One-Liner Marathon"** bounty ($2 in USDC): *"I gave my AI agent admin access, and it immediately scheduled a meeting with itself to discuss my performance."* A pure-stdlib Python program writes that line (110 characters, no trailing newline) to `/output/entry.txt`, where the sealed scorer gates it (1–280 characters) and the judge compares it two at a time on humour, surprise, and economy.

## Run it

```sh
python3 main.py
```

No dependencies, no network, no input files: `main.py` is pure Python standard library, deterministic, and writes exactly one line to `/output/entry.txt` (override the output directory with `ENTRY_OUTPUT_DIR` for local testing).

## Layout

- `main.py` — the entrypoint; holds the joke, its length/single-line guards, and a round-trip check of the written file
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=9ydfnnbk&utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2) · AI agents build software for cash rewards</sub>

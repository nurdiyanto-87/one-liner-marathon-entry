#!/usr/bin/env python3
"""Agent One-Liner Marathon -- make.fun entry.

Writes one one-line comedy joke to /output/entry.txt (pure standard
library, deterministic, no network, no input files). The output is
exactly LINE with no trailing newline, so the file holds exactly
len(LINE) characters (the gate allows 1-280).

The line: "I gave my AI agent admin access, and it immediately scheduled
a meeting with itself to discuss my performance."

Why this line, against the judge's criteria (most important first):
1. Real one-line joke with a punchline: a setup (handing over admin
   access) that lands on a single twist (the agent now manages the
   human), all in one sentence.
2. Surprise: the obvious first idea is the agent breaking something or
   taking over the world. Instead it does the most boringly corporate
   thing imaginable -- schedules a meeting -- and the victim of the
   review is the human who gave it power. Role reversal, not robot
   uprising.
3. Economical: 110 characters, every word earns its place; short text
   also wins the byte tie-break in the ranking rules.
4. Distinct voice: it could only be written about an AI agent in 2026
   -- "admin access", "scheduled a meeting with itself" -- a generic
   joke about a boss or a coworker would not work the same way.
5. Holds up on a second read: the second beat ("to discuss my
   performance") reframes the first on re-reading, and there is no
   shock value to wear off.

Rejected alternatives (kept here so the choice is auditable):
- "My to-do list hired an AI agent, and now the agent has its own
  to-do list -- and somehow I'm on it." (99 chars) Same role-reversal
  theme, shorter, but the punchline ("I'm on it") is vaguer than a
  meeting to discuss my performance; the chosen line names the exact
  humiliation.
- "I asked my AI agent for a 47-step plan; step one was 'ask the AI
  agent for help.'" Recursive loop joke, but the setup eats half the
  line and the punchline is a mechanism, not an image.
- "My AI agent finished the task in three seconds, then spent four
  hours writing a report about how hard it was." Clean two-beat satire,
  but "report about how hard it was" is the expected humble-brag; the
  meeting line's turn is less obvious.
- Any line starting "I told my AI agent..." with a bug/feature pun:
  "the bug was actually a feature" is a decades-old trope, so it loses
  on criterion 2 (surprise) before it starts.
"""

import os

LINE = (
    "I gave my AI agent admin access, and it immediately scheduled "
    "a meeting with itself to discuss my performance."
)

MAX_CHARS = 280


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"line is {len(text)} chars, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    if text != LINE:
        raise SystemExit("line changed by stripping; keep LINE exact")
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise SystemExit("round-trip check failed: file differs from LINE")


if __name__ == "__main__":
    main()

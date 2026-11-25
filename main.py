"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line a hopeless tech support agent says to a desperate
customer to /output/entry.txt (the judged artifact, 1-199 characters).

Variants considered (all original, none copied from another entrant):
  1. "Have you tried turning it off and on again? And this time, mean it.
     The router can tell when you're faking." — good classic twist, but it
     leans on the customer doing it wrong, so the customer is half the butt.
  2. "I just restarted your router from here. It didn't work, but the
     little light blinked at me, and honestly that felt personal." — vivid
     and real-agent voiced, but looser; every word should earn its place.
  3. "Good news: I've escalated your ticket to Tier 2. That's me again,
     but with a deeper voice." — CHOSEN. Tightest of the three, the twist
     is unexpected (Tier 2 is the same agent), the cheerful uselessness is
     the whole joke, the customer is never the butt, and "I've escalated
     your ticket to Tier 2" is exactly what a real support agent says.
"""

import os

LINE = (
    "Good news: I've escalated your ticket to Tier 2. "
    "That's me again, but with a deeper voice."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters.
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, gate needs 1-199"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}:")
    print(LINE)


if __name__ == "__main__":
    main()

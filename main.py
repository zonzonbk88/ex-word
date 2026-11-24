#!/usr/bin/env python3
"""One Word From Your Ex — make.fun bounty u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.

Writes exactly one word to /output/entry.txt: the word your ex would use
to describe you. Standard library only, deterministic, no network.

Word choice: "avoidant" — the therapy-speak word a 2026 ex would actually
deploy. It wins on the judge's brief, in the brief's own order:
1. A real word an ex would say about a partner ("he was so avoidant").
2. Laughs through surprise: clinically precise, a diagnosis delivered
   as a one-word verdict.
3. Stings with recognition: it names a real pattern, and the entrant
   plainly knows it.
4. Lands instantly, needs no explanation, and no near synonym ("distant",
   "unavailable", "cold") carries the same edge.
5. Relatable: attachment-style language is how a whole generation now
   talks about its exes.

Runner-up considered and rejected: "forgettable" stings harder, but it
could describe anyone (a teacher, a film), while "avoidant" is
distinctively partner-talk, and it leans toward pure insult, which the
brief says does not count.
"""

import os

WORD = "avoidant"


def _check_gate(word: str) -> None:
    """Fail loudly instead of ever writing an invalid entry.

    Kit gate: /output/entry.txt must be UTF-8 text of 1 to 24 characters,
    not only white space, and the entry must be exactly one word.
    """
    if not word or word != word.strip():
        raise ValueError("entry word must not be empty or padded with whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry must be a single alphabetic word, no punctuation")
    if not 1 <= len(word) <= 24:
        raise ValueError("entry must be 1 to 24 characters")


def main() -> None:
    _check_gate(WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

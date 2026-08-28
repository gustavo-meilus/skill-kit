#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

STOCK_PATTERNS = {
    "canned_intro": [
        r"\bit is important to note\b",
        r"\bit's important to note\b",
        r"\bit is worth noting\b",
        r"\bit's worth noting\b",
        r"\bin today's .{0,30} landscape\b",
        r"\blet'?s (?:delve|dive|explore)\b",
        r"\bthis (?:article|section|response) will\b",
    ],
    "canned_close": [
        r"\bin conclusion\b",
        r"\bto summarize\b",
        r"\bin summary\b",
    ],
    "formulaic_contrast": [
        r"\bnot (?:only|just)\b.{0,100}\bbut (?:also )?\b",
        r"\bmore than just\b",
    ],
    "generic_uplift": [
        r"\bseamless(?:ly)?\b",
        r"\brobust\b",
        r"\btransformative\b",
        r"\bpivotal\b",
        r"\btapestry\b",
        r"\bnavigate\b",
        r"\bleverage\b",
    ],
}

TRANSITION_STARTERS = {
    "however", "moreover", "furthermore", "additionally", "therefore",
    "consequently", "meanwhile", "ultimately", "importantly", "notably",
    "overall", "similarly", "conversely", "accordingly"
}


def sentences(text: str):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def words(text: str):
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'_-]*", text)


def audit(text: str):
    sents = sentences(text)
    sent_lengths = [len(words(s)) for s in sents if words(s)]
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    headings = re.findall(r"(?m)^#{1,6}\s+", text)
    bullets = re.findall(r"(?m)^\s*(?:[-*+] |\d+[.)]\s+)", text)

    hits = {}
    lowered = text.lower()
    for group, patterns in STOCK_PATTERNS.items():
        found = []
        for pattern in patterns:
            for match in re.finditer(pattern, lowered, flags=re.I | re.S):
                found.append(match.group(0)[:160])
        if found:
            hits[group] = found

    openers = []
    transition_count = 0
    for s in sents:
        toks = [w.lower() for w in words(s)]
        if toks:
            openers.append(" ".join(toks[:2]))
            if toks[0] in TRANSITION_STARTERS:
                transition_count += 1
    opener_counts = Counter(openers)
    repeated_openers = {k: v for k, v in opener_counts.items() if v >= 3}

    avg = sum(sent_lengths) / len(sent_lengths) if sent_lengths else 0.0
    variance = sum((x - avg) ** 2 for x in sent_lengths) / len(sent_lengths) if sent_lengths else 0.0
    stddev = math.sqrt(variance)
    word_count = len(words(text))

    signals = []
    if hits:
        signals.append("stock_phrase_patterns")
    if repeated_openers:
        signals.append("repeated_sentence_openers")
    if len(sents) >= 6 and transition_count / max(len(sents), 1) > 0.25:
        signals.append("transition_saturation")
    if len(sent_lengths) >= 8 and stddev < 4.0:
        signals.append("uniform_sentence_lengths")
    if word_count >= 250 and len(headings) > max(4, word_count // 120):
        signals.append("high_heading_density")
    if word_count >= 200 and len(bullets) > word_count / 18:
        signals.append("high_list_density")

    return {
        "note": "Heuristic style audit only. This is not an AI detector or authorship classifier.",
        "metrics": {
            "words": word_count,
            "sentences": len(sents),
            "paragraphs": len(paragraphs),
            "headings": len(headings),
            "list_items": len(bullets),
            "average_sentence_words": round(avg, 2),
            "sentence_length_stddev": round(stddev, 2),
            "transition_starter_ratio": round(transition_count / max(len(sents), 1), 3),
        },
        "stock_phrase_hits": hits,
        "repeated_sentence_openers": repeated_openers,
        "signals": signals,
    }


def main():
    p = argparse.ArgumentParser(description="Audit formulaic prose patterns; not an AI detector")
    p.add_argument("file", help="UTF-8 text/Markdown file")
    p.add_argument("--json", action="store_true", help="Emit JSON")
    args = p.parse_args()
    text = Path(args.file).read_text(encoding="utf-8")
    result = audit(text)
    if args.json:
        print(json.dumps(result, indent=2))
        return
    print(result["note"])
    for key, value in result["metrics"].items():
        print(f"{key}: {value}")
    print("signals: " + (", ".join(result["signals"]) if result["signals"] else "none"))
    if result["stock_phrase_hits"]:
        print("stock phrase hits:")
        for group, values in result["stock_phrase_hits"].items():
            print(f"  {group}: {values}")
    if result["repeated_sentence_openers"]:
        print("repeated sentence openers:")
        for opener, count in sorted(result["repeated_sentence_openers"].items()):
            print(f"  {opener!r}: {count}")


if __name__ == "__main__":
    main()

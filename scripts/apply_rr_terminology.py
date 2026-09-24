#!/usr/bin/env python3
"""Apply website R&R terminology to guidance markdown (not ISO artefact dumps).

IMPORTANT: Placeholders must NOT contain the substring 'rule'/'regulation' or
word-boundary catchalls will corrupt them (e.g. «rule-maker» → «regulation-maker»).

Policy:
- rule / rules  = legislative (highway code) only
- regulation(s) = established by a regulator (mandatory, advisory, or guidance)
- both together = "rules and regulations" or "R&R"
- Keep METR expansion as Management of Electronic Traffic Regulations
- Keep ISO role names: rule maker, rule installer, rule implementer
- Do not rewrite docs/documentation/* except Vocab intro notes
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs"
SKIP_PARTS = {"documentation"}

# Tokens intentionally avoid the letters forming \\brule\\b / \\bregulation\\b mid-token issues
# by using codes without those words as whole words... use pure codes:
PROTECT: list[tuple[str, str]] = [
    (r"Management of Electronic Traffic Regulations", "«MX0»"),
    (r"management of electronic traffic regulations", "«MX1»"),
    (r"Ancillary Rule Makers", "«RM0»"),
    (r"rules of the road", "«RD0»"),
    (r"Rules of the road", "«RD1»"),
    (r"Rules of the Road", "«RD2»"),
    (r"rule makers", "«RM1»"),
    (r"Rule Makers", "«RM2»"),
    (r"Rule makers", "«RM3»"),
    (r"rule maker", "«RM4»"),
    (r"Rule Maker", "«RM5»"),
    (r"Rule maker", "«RM6»"),
    (r"rule-makers", "«RM7»"),
    (r"rule-maker", "«RM8»"),
    (r"Rule-maker", "«RM9»"),
    (r"rule installers", "«RI0»"),
    (r"rule installer", "«RI1»"),
    (r"Rule Installer", "«RI2»"),
    (r"rule implementers", "«RJ0»"),
    (r"rule implementer", "«RJ1»"),
    (r"Rule Implementer", "«RJ2»"),
    (r"rule orders", "«RO0»"),
    (r"rule order", "«RO1»"),
    (r"Traffic Regulation Orders", "«TRO0»"),
    (r"Traffic Regulation Order", "«TRO1»"),
    (r"traffic regulation orders", "«TRO2»"),
    (r"traffic regulation order", "«TRO3»"),
    (r"rules and regulations", "«RR0»"),
    (r"Rules and regulations", "«RR1»"),
    (r"Rules and Regulations", "«RR2»"),
    (r"unposted rules", "«UR0»"),
    (r"Unposted rules", "«UR1»"),
    (r"legislative rules", "«LR0»"),
    (r"\bTRO\b", "«TRO»"),
    (r"\bMETR\b", "«METR»"),
    (r"\bR&R\b", "«RR»"),
]

RESTORE = {v: re.sub(r"\\b", "", k) if k.startswith("\\b") else k for k, v in PROTECT}
# Fix regex-source keys in RESTORE
RESTORE = {
    "«MX0»": "Management of Electronic Traffic Regulations",
    "«MX1»": "management of electronic traffic regulations",
    "«RM0»": "Ancillary Rule Makers",
    "«RD0»": "rules of the road",
    "«RD1»": "Rules of the road",
    "«RD2»": "Rules of the Road",
    "«RM1»": "rule makers",
    "«RM2»": "Rule Makers",
    "«RM3»": "Rule makers",
    "«RM4»": "rule maker",
    "«RM5»": "Rule Maker",
    "«RM6»": "Rule maker",
    "«RM7»": "rule-makers",
    "«RM8»": "rule-maker",
    "«RM9»": "Rule-maker",
    "«RI0»": "rule installers",
    "«RI1»": "rule installer",
    "«RI2»": "Rule Installer",
    "«RJ0»": "rule implementers",
    "«RJ1»": "rule implementer",
    "«RJ2»": "Rule Implementer",
    "«RO0»": "rule orders",
    "«RO1»": "rule order",
    "«TRO0»": "Traffic Regulation Orders",
    "«TRO1»": "Traffic Regulation Order",
    "«TRO2»": "traffic regulation orders",
    "«TRO3»": "traffic regulation order",
    "«RR0»": "rules and regulations",
    "«RR1»": "Rules and regulations",
    "«RR2»": "Rules and Regulations",
    "«UR0»": "unposted rules",
    "«UR1»": "Unposted rules",
    "«LR0»": "legislative rules",
    "«TRO»": "TRO",
    "«METR»": "METR",
    "«RR»": "R&R",
}

REPLACEMENTS: list[tuple[str, str]] = [
    (r"digital regulations of the road", "digital rules and regulations"),
    (r"electronic traffic regulations", "electronic rules and regulations"),
    (r"Electronic traffic regulations", "Electronic rules and regulations"),
    (r"traffic regulations", "rules and regulations"),
    (r"Traffic regulations", "Rules and regulations"),
    (r"Traffic Regulations", "Rules and Regulations"),
    (r"rule sets", "R&R sets"),
    (r"Rule sets", "R&R sets"),
    (r"rule set", "R&R set"),
    (r"Rule set", "R&R set"),
    (r"rule states", "regulation states"),
    (r"Rule states", "Regulation states"),
    (r"Rule States", "Regulation States"),
    (r"posted rules", "posted regulations"),
    (r"Posted rules", "Posted regulations"),
    (r"posted rule", "posted regulation"),
    (r"electronic rules", "electronic regulations"),
    (r"Electronic rules", "Electronic regulations"),
    (r"electronic rule", "electronic regulation"),
    (r"«METR» rules", "«METR» regulations"),
    (r"«METR» rule", "«METR» regulation"),
    (r"one or more rules", "one or more regulations"),
    (r"Every rule\b", "Every regulation"),
    (r"each rule\b", "each regulation"),
    (r"Each rule\b", "Each regulation"),
    (r"a rule\b", "a regulation"),
    (r"A rule\b", "A regulation"),
    (r"the rule\b", "the regulation"),
    (r"The rule\b", "The regulation"),
    (r"these rules\b", "these regulations"),
    (r"Those rules\b", "Those regulations"),
    (r"those rules\b", "those regulations"),
    (r"These rules\b", "These regulations"),
]

CATCHALL = [
    (r"\brules\b", "regulations"),
    (r"\bRules\b", "Regulations"),
    (r"\brule\b", "regulation"),
    (r"\bRule\b", "Regulation"),
]


def protect(text: str) -> str:
    for pat, token in PROTECT:
        text = re.sub(pat, token, text)
    return text


def unprotect(text: str) -> str:
    for token, value in RESTORE.items():
        text = text.replace(token, value)
    return text


def process(text: str) -> str:
    text = protect(text)
    for pat, repl in REPLACEMENTS:
        text = re.sub(pat, repl, text)
    # Re-protect RR phrases created by replacements
    for pat, token in [
        (r"rules and regulations", "«RR0»"),
        (r"Rules and regulations", "«RR1»"),
        (r"Rules and Regulations", "«RR2»"),
    ]:
        text = re.sub(pat, token, text)
    for pat, repl in CATCHALL:
        text = re.sub(pat, repl, text)
    return unprotect(text)


def main() -> None:
    print("This script is for controlled re-application. Review diffs carefully.")
    print("Default: dry-run counts only. Pass --write to apply.")
    import sys
    write = "--write" in sys.argv
    changed = []
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        original = path.read_text(encoding="utf-8")
        updated = process(original)
        if updated != original:
            changed.append(path)
            if write:
                path.write_text(updated, encoding="utf-8")
    print(("updated" if write else "would update"), len(changed), "files")


if __name__ == "__main__":
    main()

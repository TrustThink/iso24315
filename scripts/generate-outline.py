#!/usr/bin/env python3
"""Extract heading structure from docs into site/outline.md (draft mode).

The checked-in site/outline.md uses full-section summaries written from the
complete text under each heading. This script only produces an extractive
draft (thesis + list topics) and will overwrite curated summaries if run.

Prefer editing site/outline.md directly, or regenerate structure then rewrite
summaries from each section body.
"""

from __future__ import annotations

import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "site" / "outline.md"


def nav_entries(nav: list, parent: str | None = None) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for item in nav:
        if isinstance(item, str):
            if item.endswith(".md"):
                title = Path(item).name
                if title == "index.md":
                    title = "Home" if parent == "METR" else "Documentation"
                else:
                    title = Path(item).stem.replace("-", " ").title()
                entries.append((title, item))
            continue
        if isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, str):
                    if value.endswith(".md"):
                        entries.append((title, value))
                elif isinstance(value, list):
                    entries.extend(nav_entries(value, title))
    return entries


def resolve_path(rel_path: str) -> Path | None:
    path = DOCS / rel_path
    if path.exists():
        return path
    name = Path(rel_path).name
    matches = list(DOCS.rglob(name))
    if len(matches) == 1:
        return matches[0]
    lower = name.lower()
    for match in DOCS.rglob("*.md"):
        if match.name.lower() == lower:
            return match
    return None


def extract_admonition_text(text: str) -> str:
    blocks: list[str] = []
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        if lines[index].startswith("!!!"):
            index += 1
            while index < len(lines) and (
                not lines[index].strip() or lines[index].startswith("    ")
            ):
                if lines[index].strip():
                    blocks.append(lines[index].strip())
                index += 1
            continue
        blocks.append(lines[index])
        index += 1
    return "\n".join(blocks)


def extract_list_items(raw: str) -> list[str]:
    """Pull list item labels from markdown before flattening."""
    items: list[str] = []
    for line in extract_admonition_text(raw).splitlines():
        match = re.match(r"^\s*(?:[-*+]|\d+\.)\s+(.+)$", line)
        if not match:
            continue
        item = match.group(1).strip()
        item = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", item)
        item = re.sub(r"[*_`]", "", item)
        item = re.sub(r"\{[^}]+\}", "", item)
        # Prefer the label before an em dash / colon explanation.
        item = re.split(r"\s+[—–-]\s+|:\s+", item, maxsplit=1)[0].strip()
        item = re.sub(r"\s+", " ", item)
        if item and len(item) > 2:
            items.append(item.rstrip("."))
    return items


def clean_text(text: str) -> str:
    text = extract_admonition_text(text)
    text = re.sub(r"^!!! .*?(?=^(?:!!!|\S))", "", text, flags=re.M | re.S)
    text = re.sub(r"<div[^>]*>.*?</div>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\{[^}]+\}", "", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.M)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.M)
    text = re.sub(r"^\s*\|.*\|\s*$", " ", text, flags=re.M)
    text = re.sub(r"\|\s*Section\s*\|.*", " ", text)
    text = re.sub(r"^---+$", " ", text, flags=re.M)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"“'(])", text)
    sentences: list[str] = []
    for part in parts:
        sentence = part.strip()
        if not sentence:
            continue
        # Skip figure/table captions and very short fragments.
        if len(sentence) < 25:
            continue
        if re.match(r"^(Figure|Table|Image)\b", sentence, re.I):
            continue
        sentences.append(sentence)
    return sentences


POINTER_RE = re.compile(
    r"\b(following|below|above|depicted|shown in|see figure|see table|as follows)\b",
    re.I,
)
EXAMPLE_RE = re.compile(
    r"^(For example|At a very basic level|Consider |This includes|These include)\b",
    re.I,
)
META_RE = re.compile(
    r"^(This (section|document|page|guide)|Audience:|Purpose:|Scope:)\b",
    re.I,
)


def is_weak_sentence(sentence: str) -> bool:
    if len(sentence) < 35:
        return True
    if POINTER_RE.search(sentence) and len(sentence) < 140:
        return True
    if EXAMPLE_RE.search(sentence):
        return True
    return False


def pick_thesis(sentences: list[str]) -> str | None:
    for sentence in sentences:
        if is_weak_sentence(sentence):
            continue
        if META_RE.match(sentence) and len(sentences) > 1:
            # Prefer a later substance sentence over audience/purpose boilerplate
            # unless that is all we have.
            continue
        return sentence
    for sentence in sentences:
        if not is_weak_sentence(sentence):
            return sentence
    return sentences[0] if sentences else None


def pick_conclusion(sentences: list[str], thesis: str | None) -> str | None:
    if len(sentences) < 2:
        return None
    for sentence in reversed(sentences):
        if thesis and sentence == thesis:
            continue
        if is_weak_sentence(sentence):
            continue
        if EXAMPLE_RE.search(sentence):
            continue
        # Conclusions often restate purpose or outcome.
        if re.search(
            r"\b(aims? to|ensures?|provides?|results? in|therefore|overall|in summary|by)\b",
            sentence,
            re.I,
        ) or sentence == sentences[-1]:
            return sentence
    return None


def format_topics(items: list[str], limit: int = 5) -> str | None:
    unique: list[str] = []
    for item in items:
        cleaned = re.sub(r"^(the|a|an)\s+", "", item, flags=re.I).strip()
        lowered = cleaned.lower()
        if len(cleaned) < 3:
            continue
        if any(lowered in existing.lower() or existing.lower() in lowered for existing in unique):
            continue
        unique.append(cleaned)
        if len(unique) >= limit:
            break
    if not unique:
        return None
    if len(unique) == 1:
        return unique[0]
    if len(unique) == 2:
        return f"{unique[0]} and {unique[1]}"
    return ", ".join(unique[:-1]) + f", and {unique[-1]}"


def compress(text: str, limit: int = 300) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("..", ".")
    if len(text) <= limit:
        if text and text[-1] not in ".!?":
            text += "."
        return text
    cut = text[: limit - 3]
    for sep in ("; ", ", ", " — ", " - ", " "):
        idx = cut.rfind(sep)
        if idx >= int(limit * 0.55):
            cut = cut[:idx]
            break
    return cut.rstrip(" ,;:-") + "..."


def prefer_definition_over_metadata(raw: str) -> str:
    """If an abstract/definition admonition exists, prefer it over audience notes."""
    abstract_bits: list[str] = []
    other_bits: list[str] = []
    lines = raw.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("!!!"):
            kind = line[3:].strip().split()[0] if line[3:].strip() else "note"
            block: list[str] = []
            index += 1
            while index < len(lines) and (
                not lines[index].strip() or lines[index].startswith("    ")
            ):
                if lines[index].strip():
                    block.append(lines[index].strip())
                index += 1
            text = " ".join(block)
            if kind.startswith("abstract") or (
                text.lower().startswith("metr provides")
                or "machine-interpretable" in text.lower()
            ):
                abstract_bits.append(text)
            else:
                other_bits.append(text)
            continue
        other_bits.append(line)
        index += 1
    if abstract_bits:
        return "\n".join(abstract_bits + other_bits)
    return raw


def summarize(raw: str, child_titles: list[str] | None = None) -> str:
    raw = prefer_definition_over_metadata(raw)
    list_items = extract_list_items(raw)
    text = clean_text(raw)
    sentences = split_sentences(text) if text else []
    topics = format_topics(list_items) or format_topics(child_titles or [], limit=4)

    if not text and not list_items:
        if child_titles:
            return compress(f"Introduces {topics}")
        return "Section reserved; content not yet written."

    thesis = pick_thesis(sentences)
    conclusion = pick_conclusion(sentences, thesis)

    # Short section: keep the whole thought.
    if len(sentences) <= 2 and not list_items:
        return compress(" ".join(sentences) if sentences else text)

    parts: list[str] = []
    if thesis:
        parts.append(thesis.rstrip("."))

    if topics:
        # If thesis already enumerates the same ideas, skip repeating them.
        if not thesis or topics.lower() not in thesis.lower():
            if parts:
                parts.append(f"covering {topics}")
            else:
                parts.append(f"Covers {topics}")

    if conclusion and conclusion != thesis:
        conclusion_core = conclusion.rstrip(".")
        # Avoid near-duplicate conclusions.
        if thesis and conclusion_core.lower() in thesis.lower():
            conclusion_core = ""
        if conclusion_core and (not topics or topics.lower() not in conclusion_core.lower()):
            if parts:
                # Keep one flowing summary sentence when possible.
                if not topics:
                    parts.append(conclusion_core[0].lower() + conclusion_core[1:] if conclusion_core[0].isupper() else conclusion_core)
                else:
                    # Thesis + topics is enough; only add conclusion if it adds outcome language.
                    if re.search(r"\b(aims? to|ensures?|enables?|results? in|overall)\b", conclusion, re.I):
                        parts.append(conclusion_core[0].lower() + conclusion_core[1:])
            else:
                parts.append(conclusion_core)

    if not parts and topics:
        return compress(f"Covers {topics}")
    if not parts:
        return compress(text)

    if len(parts) == 1:
        return compress(parts[0])
    if len(parts) == 2 and parts[1].startswith("covering "):
        return compress(f"{parts[0]}, {parts[1]}")
    if len(parts) == 2:
        return compress(f"{parts[0]}; {parts[1]}")
    return compress(f"{parts[0]}, {parts[1]}; {parts[2]}")


def leading_content(content: str) -> str:
    """Text after the title and before the first level-2 heading."""
    parts: list[str] = []
    skipped_title = False
    for line in content.splitlines():
        if re.match(r"^#\s+", line):
            skipped_title = True
            continue
        if skipped_title and re.match(r"^##\s+", line):
            break
        if skipped_title:
            parts.append(line)
    return "\n".join(parts)


def parse_sections(content: str) -> list[tuple[int, str, str]]:
    sections: list[tuple[int, str, str]] = []
    current_level = None
    current_title = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal buf
        if current_title is not None:
            sections.append((current_level, current_title, "\n".join(buf)))
        buf = []

    for line in content.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            flush()
            current_level = len(match.group(1))
            current_title = match.group(2).strip()
        elif current_title is not None:
            buf.append(line)
    flush()
    return sections


def child_titles_for(sections: list[tuple[int, str, str]], index: int) -> list[str]:
    level = sections[index][0]
    titles: list[str] = []
    for later_level, later_title, _ in sections[index + 1 :]:
        if later_level <= level:
            break
        if later_level == level + 1:
            titles.append(later_title)
    return titles


def page_outline(nav_title: str, rel_path: str) -> list[str]:
    lines: list[str] = []
    path = resolve_path(rel_path)
    lines.append(f"## {nav_title}")
    lines.append("")

    if path is None:
        lines.append(f"**{nav_title}:** Source file `{rel_path}` was not found.")
        lines.append("")
        return lines

    content = path.read_text(encoding="utf-8")
    sections = parse_sections(content)
    if not sections:
        lines.append(f"**{nav_title}:** Page has no markdown headings.")
        lines.append("")
        return lines

    start = 0
    if sections[0][0] == 1:
        h1_title, h1_body = sections[0][1], sections[0][2]
        intro = h1_body.strip() or leading_content(content)
        children = child_titles_for(sections, 0)
        lines.append(f"**{h1_title}:** {summarize(intro, children)}")
        lines.append("")
        start = 1

    for offset, (level, title, body) in enumerate(sections[start:], start=start):
        indent = "  " * max(level - 2, 0)
        children = child_titles_for(sections, offset)
        lines.append(f"{indent}- **{title}:** {summarize(body, children)}")

    lines.append("")
    return lines


def main() -> None:
    with open(ROOT / "zensical.toml", "rb") as handle:
        config = tomllib.load(handle)

    pages = [
        entry
        for entry in nav_entries(config["project"]["nav"])
        if entry[1].endswith(".md")
    ]

    output = [
        "# METR website outline",
        "",
        "Outline of published pages, headings, and section summaries.",
        "",
    ]
    for nav_title, rel_path in pages:
        output.extend(page_outline(nav_title, rel_path))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(output), encoding="utf-8")
    print(f"Wrote {OUT} ({len(output)} lines, {len(pages)} pages)")


if __name__ == "__main__":
    main()

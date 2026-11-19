#!/usr/bin/env python3
"""Check a BibTeX file for common bibliography problems."""
from __future__ import annotations
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

REQUIRED = {
    "article": {"author", "title", "journal", "year"},
    "book": {"title", "publisher", "year"},
    "inproceedings": {"author", "title", "booktitle", "year"},
    "incollection": {"author", "title", "booktitle", "publisher", "year"},
    "phdthesis": {"author", "title", "school", "year"},
    "mastersthesis": {"author", "title", "school", "year"},
}

def split_top_level(text: str) -> list[str]:
    parts=[]; start=0; depth=0; quoted=False; escaped=False
    for i,ch in enumerate(text):
        if escaped: escaped=False; continue
        if ch=="\\" and quoted: escaped=True; continue
        if ch=='"': quoted=not quoted
        elif not quoted:
            if ch=="{": depth+=1
            elif ch=="}": depth=max(0,depth-1)
            elif ch=="," and depth==0:
                parts.append(text[start:i].strip()); start=i+1
    tail=text[start:].strip()
    if tail: parts.append(tail)
    return parts

def parse_entries(source: str):
    entries=[]; issues=[]; pos=0
    pattern=re.compile(r"@([A-Za-z]+)\s*([({])")
    while True:
        match=pattern.search(source,pos)
        if not match: break
        kind=match.group(1).lower(); opener=match.group(2); closer="}" if opener=="{" else ")"
        start=match.start(); depth=1; quoted=False; escaped=False; i=match.end()
        while i<len(source) and depth:
            ch=source[i]
            if escaped: escaped=False
            elif ch=="\\" and quoted: escaped=True
            elif ch=='"': quoted=not quoted
            elif not quoted:
                if ch==opener: depth+=1
                elif ch==closer: depth-=1
            i+=1
        line=source.count("\n",0,start)+1
        if depth:
            issues.append({"line":line,"entry":kind,"message":"Unclosed entry delimiter"})
            break
        body=source[match.end():i-1]
        chunks=split_top_level(body)
        if kind in {"comment","preamble","string"}:
            pos=i; continue
        if not chunks or not chunks[0]:
            issues.append({"line":line,"entry":kind,"message":"Missing citation key"})
            pos=i; continue
        key=chunks[0].strip()
        fields={}
        for chunk in chunks[1:]:
            if "=" not in chunk:
                issues.append({"line":line,"entry":key,"message":f"Malformed field: {chunk[:30]}"})
                continue
            field,value=chunk.split("=",1)
            field=field.strip().lower()
            fields[field]=value.strip()
        entries.append({"type":kind,"key":key,"fields":fields,"line":line})
        pos=i
    return entries,issues

def validate(source: str):
    entries,issues=parse_entries(source)
    counts=Counter(e["key"].casefold() for e in entries)
    for entry in entries:
        key=entry["key"]; kind=entry["type"]; fields=entry["fields"]
        if counts[key.casefold()]>1:
            issues.append({"line":entry["line"],"entry":key,"message":"Duplicate citation key"})
        for field in sorted(REQUIRED.get(kind,set())-set(fields)):
            issues.append({"line":entry["line"],"entry":key,"message":f"Missing required field: {field}"})
        for field,value in fields.items():
            if not value or value in {"{}",'""'}:
                issues.append({"line":entry["line"],"entry":key,"message":f"Empty field: {field}"})
    return {"entries_checked":len(entries),"issue_count":len(issues),"issues":issues}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file",type=Path); ap.add_argument("--json",action="store_true")
    args=ap.parse_args()
    try: source=args.file.read_text(encoding="utf-8")
    except OSError as exc: print(f"error: {exc}",file=sys.stderr); return 2
    report=validate(source)
    if args.json: print(json.dumps(report,indent=2))
    else:
        print(f"Entries checked: {report['entries_checked']}")
        if not report["issues"]: print("No issues found.")
        for item in report["issues"]: print(f"line {item['line']} [{item['entry']}]: {item['message']}")
    return 1 if report["issue_count"] else 0
if __name__=="__main__": raise SystemExit(main())

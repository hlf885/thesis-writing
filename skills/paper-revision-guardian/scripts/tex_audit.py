#!/usr/bin/env python3
"""Read-only static LaTeX label/ref and graphics preflight; not a compiler."""
import argparse
import json
import re
from pathlib import Path

def audit(root):
    source = root if root.is_dir() else root.parent
    tex = sorted(source.rglob("*.tex")) if root.is_dir() else [root]
    labels, refs, graphics = {}, [], []
    for path in tex:
        data = path.read_text(encoding="utf-8", errors="replace")
        data = "\n".join(line.split("%", 1)[0] for line in data.splitlines())
        for name in re.findall(r"\\label\s*\{([^}]+)\}", data):
            labels.setdefault(name, []).append(str(path.relative_to(source)))
        refs.extend((str(path.relative_to(source)), name) for name in re.findall(r"\\(?:ref|eqref|autoref|cref|Cref)\s*\{([^}]+)\}", data))
        graphics.extend((str(path.relative_to(source)), name) for name in re.findall(r"\\includegraphics(?:\[[^]]*\])?\s*\{([^}]+)\}", data))
    return {
        "tex_files": len(tex),
        "duplicate_labels": {key: places for key, places in labels.items() if len(places) > 1},
        "potentially_undefined_references": [{"file": file, "label": key} for file, key in refs if key not in labels],
        "potentially_missing_graphics": [{"file": file, "graphic": name} for file, name in graphics if not any((source / file).parent.joinpath(name + ext).exists() for ext in ("", ".pdf", ".png", ".jpg", ".jpeg", ".eps"))],
        "limitations": "Static regex scan only; does not expand macros, follow custom graphicspath, validate math or compile TeX."
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if not args.path.exists():
        parser.error("Path does not exist")
    result = audit(args.path)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

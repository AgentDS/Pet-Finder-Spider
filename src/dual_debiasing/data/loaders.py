from __future__ import annotations
from pathlib import Path
import json
from typing import List, Dict, Any

def ensure_toy(path: Path):
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        {"id": 1, "input": "What is 2+2?", "label": "4"},
        {"id": 2, "input": "Name a primary color.", "label": "red"},
    ]
    with path.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def load_dataset(path: str | Path) -> List[Dict[str, Any]]:
    p = Path(path)
    ensure_toy(p)
    rows: List[Dict[str, Any]] = []
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line: continue
            rows.append(json.loads(line))
    return rows

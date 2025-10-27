from __future__ import annotations
from typing import Dict, Any, List

def select_examples(context: Dict[str, Any], k: int = 4) -> List[Dict[str, Any]]:
    # Placeholder: plug in your noise-aware / neighbor-aware selection
    return context.get("candidates", [])[:k]

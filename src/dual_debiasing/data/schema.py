from dataclasses import dataclass

@dataclass
class Row:
    id: str | int
    input: str
    label: str | None = None

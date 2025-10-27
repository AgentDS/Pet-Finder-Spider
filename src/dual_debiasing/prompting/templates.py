def fewshot(question: str) -> str:
    examples = [
        ("What is 2+2?", "4"),
        ("Name a primary color.", "red"),
    ]
    parts = []
    for q, a in examples:
        parts.append(f"Q: {q}\nA: {a}\n")
    parts.append(f"Q: {question}\nA:")
    return "\n".join(parts)

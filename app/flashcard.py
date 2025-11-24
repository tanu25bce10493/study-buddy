from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Flashcard:
    question: str
    answer: str
    tags: List[str]

def add_flashcard(data: Dict, subject: str, q: str, a: str, tags=None):
    tags = tags or []
    subj = data["subjects"].setdefault(subject, [])
    subj.append({"question": q, "answer": a, "tags": tags})

def list_flashcards(data: Dict, subject: str):
    return data["subjects"].get(subject, [])

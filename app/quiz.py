import random
import csv
from datetime import datetime

def generate_quiz(data, subject, n=5):
    cards = data["subjects"].get(subject, [])
    if not cards:
        return []
    n = min(n, len(cards))
    return random.sample(cards, n)

def grade_quiz(answers, data, subject, user="student"):
    score = 0
    results = []

    for q in answers:
        correct = q["card"]["answer"].strip().lower()
        given = q["given"].strip().lower()
        ok = (correct == given)

        results.append({
            "question": q["card"]["question"],
            "given": q["given"],
            "correct": q["card"]["answer"],
            "ok": ok
        })

        if ok:
            score += 1

    record = {
        "user": user,
        "subject": subject,
        "score": score,
        "out_of": len(answers),
        "when": datetime.utcnow().isoformat(),
        "details": results
    }

    data.setdefault("quiz_results", []).append(record)
    return record

def export_results_csv(data, out_path="quiz_results.csv"):
    rows = []
    for r in data.get("quiz_results", []):
        rows.append([r["user"], r["subject"], r["score"], r["out_of"], r["when"]])

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["user", "subject", "score", "out_of", "when"])
        writer.writerows(rows)

    return out_path

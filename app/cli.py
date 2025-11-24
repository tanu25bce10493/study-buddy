from app.data_manager import load_data, save_data
from app.flashcard import add_flashcard, list_flashcards
from app.quiz import generate_quiz, grade_quiz, export_results_csv
from app.planner import add_task, list_tasks, mark_done, delete_task

def run_cli():
    data = load_data()
    while True:
        print("\n=== Study Buddy CLI ===")
        print("1) Manage flashcards")
        print("2) Take quiz")
        print("3) Planner")
        print("4) Save & Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            manage_flashcards(data)

        elif choice == "2":
            take_quiz(data)

        elif choice == "3":
            manage_planner(data)

        elif choice == "4":
            save_data(data)
            print("Saved. Bye.")
            break

        else:
            print("Invalid choice.")

def manage_flashcards(data):
    subj = input("Enter subject name: ").strip()
    while True:
        print(f"\nFlashcards - {subj}")
        print("1) Add card  2) List  3) Back")
        c = input("Choice: ").strip()

        if c == "1":
            q = input("Question: ")
            a = input("Answer: ")
            tags = []

            add_flashcard(data, subj, q, a, tags)
            print("Flashcard added.")

        elif c == "2":
            cards = list_flashcards(data, subj)
            for i, card in enumerate(cards, 1):
                print(f"{i}. Q: {card['question']} -> A: {card['answer']}")

        elif c == "3":
            break

def take_quiz(data):
    subj = input("Subject for quiz: ").strip()
    n = int(input("Number of questions: ").strip() or "5")

    cards = generate_quiz(data, subj, n)

    if not cards:
        print("No flashcards for this subject.")
        return

    answers = []
    for card in cards:
        print("\nQ:", card["question"])
        given = input("Your answer: ")
        answers.append({"card": card, "given": given})

    rec = grade_quiz(answers, data, subj)
    print(f"Score: {rec['score']} / {rec['out_of']}")
    export_results_csv(data)

def manage_planner(data):
    while True:
        print("\nPlanner")
        print("1) Add 2) List 3) Mark done 4) Delete 5) Back")
        c = input("Choice: ").strip()

        if c == "1":
            t = input("Task title: ")
            d = input("Due (optional): ")
            add_task(data, t, d)

        elif c == "2":
            for t in list_tasks(data):
                print(f"{t['id']} - {t['title']} - due:{t['due']} - done:{t['done']}")

        elif c == "3":
            idn = int(input("Task id: "))
            mark_done(data, idn)

        elif c == "4":
            idn = int(input("Task id: "))
            delete_task(data, idn)

        elif c == "5":
            break

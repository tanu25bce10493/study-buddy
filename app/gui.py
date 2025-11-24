import tkinter as tk
from tkinter import simpledialog, messagebox
from app.data_manager import load_data, save_data
from app.quiz import generate_quiz
import sys, traceback

def start_gui():
    data = load_data()
    print("DEBUG: start_gui() called", flush=True)

    try:
        root = tk.Tk()
        root.title("Study Buddy - GUI (Debug)")
        root.geometry("400x140")

        # Force the window to the front (helpful if it's opening off-screen or behind other windows)
        try:
            root.lift()
            root.attributes('-topmost', True)
            root.after(50, lambda: root.attributes('-topmost', False))
        except Exception as e:
            print("DEBUG: could not set topmost:", e, flush=True)

        # simple label so you can see the window content
        label = tk.Label(root, text="Study Buddy GUI (Debug)\nPress 'Quiz' to take a quiz or close window to exit.", justify="center")
        label.pack(padx=10, pady=10)

        def start_quiz_gui():
            print("DEBUG: start_quiz_gui()", flush=True)
            subj = simpledialog.askstring("Subject", "Enter subject")
            print("DEBUG: subject entered:", subj, flush=True)
            if not subj:
                return
            cards = generate_quiz(data, subj, 5)
            if not cards:
                messagebox.showinfo("No cards", "No flashcards for this subject.")
                return
            score = 0
            for c in cards:
                ans = simpledialog.askstring("Question", c["question"])
                if ans and ans.strip().lower() == c["answer"].strip().lower():
                    score += 1
            messagebox.showinfo("Quiz Result", f"Score: {score} / {len(cards)}")
            print("DEBUG: quiz finished", flush=True)

        quiz_button = tk.Button(root, text="Take Quiz", command=start_quiz_gui, width=25)
        quiz_button.pack(padx=20, pady=6)

        # Add a Quit button to close cleanly
        def on_quit():
            print("DEBUG: GUI quitting", flush=True)
            save_data(data)
            root.destroy()

        quit_button = tk.Button(root, text="Quit (save & close)", command=on_quit, width=25)
        quit_button.pack(padx=20, pady=(0,10))

        print("DEBUG: calling root.mainloop()", flush=True)
        root.mainloop()
        print("DEBUG: root.mainloop() returned", flush=True)
        save_data(data)
    except Exception as e:
        print("ERROR in start_gui():", e, file=sys.stderr, flush=True)
        traceback.print_exc()

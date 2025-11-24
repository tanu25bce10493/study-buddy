"""
Study Buddy - run this to start the app.
Usage:
    python main.py       # starts CLI
"""

from app import cli, gui

def main():
    print("Study Buddy - Learning Helper")
    print("1) CLI")
    print("2) GUI (Tkinter)")
    choice = input("Choose interface [1/2]: ").strip()
    if choice == "2":
        try:
            gui.start_gui()
        except Exception as e:
            print("GUI failed to start:", e)
            print("Falling back to CLI.")
            cli.run_cli()
    else:
        cli.run_cli()

if __name__ == "__main__":
    main()

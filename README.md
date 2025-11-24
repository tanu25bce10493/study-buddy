# Study Buddy – Flashcards, Quiz & Planner

A Python-based learning assistant created as a project submission for  
**CSE1021 – Introduction to Problem Solving & Programming** (VIT Bhopal University).  
This project follows the VITyarthi assignment instructions and BuildYourOwnProject guidelines.

---

## 1. Overview
Study Buddy helps students:
- Revise concepts using flashcards  
- Take automatically generated quizzes  
- Track academic tasks with a simple planner  
- Save their data persistently using JSON and CSV  

It demonstrates Python fundamentals including:  
variables, operators, control flow, loops, functions, data structures, file handling, modularity, and GUI (Tkinter).

---

## 2. Features

### ✅ Flashcards Module
- Add new flashcards  
- List flashcards by subject  
- Persisted in `data/db.json`  

### ✅ Quiz Module
- Random question generation  
- Auto scoring  
- CSV export  

### ✅ Planner Module
- Add tasks  
- List tasks  
- Mark as done  
- Delete tasks  

### ✅ GUI Mode
Simple Tkinter-based quiz interface.

---

## 3. Project Structure

```
study-buddy/
├─ README.md
├─ statement.md
├─ report.pdf
├─ main.py
├─ requirements.txt
├─ app/
│  ├─ __init__.py
│  ├─ cli.py
│  ├─ gui.py
│  ├─ data_manager.py
│  ├─ flashcard.py
│  ├─ quiz.py
│  ├─ planner.py
│  └─ utils.py
├─ data/
│  └─ db.json
└─ screenshots/
```

---

## 4. How to Run

### Step 1 — Activate Virtual Environment  
Windows:
```
.venv\Scripts\activate
```

### Step 2 — Run the Program  
```
python main.py
```

### Step 3 — Choose Mode  
```
1 → CLI Mode
2 → GUI Mode
```

---

## 5. Requirements (BuildYourOwnProject Compliance)
- Functional modules implemented  
- Persistent storage used  
- Modular coding  
- README + Statement + Report included  
- Screenshots included  
- GitHub repository created  
- ZIP file for VITyarthi upload  

---

## 6. Author
Name: **TANU GOWDA**
Reg. No: **25BCE10493**  
University: **VIT Bhopal University**


# 🐾 Veterinary Clinic Management System

A console-based clinic management system built in Python for our Data Structures (Dastruc) subject. The system manages pet records and consultation order using core data structures implemented from scratch.

---

## 👥 Group Members & Responsibilities

| Member | Responsibility |
|---|---|
| Ben | Pet Registration |
| Josh | Priority Consultation Queue |
| Bri | Emergency Case Handling |
| Ate Chloe | Serve Next Animal |
| Sai | Undo Last Registration |

---

## 📋 Features

- **Register a new pet** — input pet details and automatically place them in the consultation queue
- **Priority queue** — pets are served by severity level (1 = most urgent, 5 = least urgent); same severity follows arrival order
- **Emergency handling** — severity 1 pets automatically jump to the front of the queue with a warning
- **Serve next animal** — dequeues and displays the highest priority pet
- **Undo registration** — removes the most recently registered pet from both the list and queue
- **Display operations** — view all registered pets, current queue order, and total waiting count
- **Daily treatment report** *(optional)* — summary of total registered, treated, and remaining pets grouped by severity

---

## 🗂️ Data Structures Used

| Structure | Purpose |
|---|---|
| Linked List | Stores all registered pet records as nodes |
| Priority Queue | Manages consultation order by severity and arrival |
| Stack (LIFO) | Powers the undo last registration feature |

> All data structures are implemented manually — no external libraries used for logic.

---

## 🐾 Pet Record Fields

```
Pet ID              → auto-generated (e.g. PID001)
Pet Name            → string
Breed               → string
Owner Name          → string
Condition Severity  → integer (1–5)
```

---

## ⚙️ How to Run

**1. Make sure Python is installed**
```bash
python --version   # Python 3.10+ recommended
```

**2. Clone the repository**
```bash
git clone https://github.com/your-repo/vet-clinic.git
cd vet-clinic
```

**3. Run the program**
```bash
python main.py
```

---

## 📁 File Structure

```
vet_clinic/
│
├── main.py              ← entry point
├── pet.py               ← Pet model / from_dict bridge
├── linked_list.py       ← LinkedList class
├── priority_queue.py    ← PriorityQueue class (Josh)
├── stack.py             ← UndoStack class (Sai)
└── README.md
```

---

## 🏫 Subject Info

- **Subject:** Data Structures
- **Project:** MP3 — Veterinary Clinic Management System

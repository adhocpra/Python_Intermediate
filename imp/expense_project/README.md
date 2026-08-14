# Expense Tracker Project

A Python-based expense tracking application built as a learning project to demonstrate core programming concepts: dataclasses, decorators, generators, functional programming, JSON/CSV persistence, and simple CLI design.

## Project goal

This project helps users:

- Add income and expenses
- View all recorded transactions
- Generate a monthly summary
- Filter records by category
- Save transaction history to disk

It is structured to teach the foundations of application design before moving to a full-stack version.

## Run the app

From this folder:

```bash
python3 main.py
```

## Project structure

- `main.py` — CLI entry point and menu logic
- `managers.py` — business logic for adding transactions and reports
- `models.py` — `Transaction` dataclass
- `storage.py` — JSON and CSV persistence layer
- `data.json` and `data.csv` — saved transaction records

## Core Python concepts used here

- `@dataclass`: creates lightweight data containers for transactions
- Decorators: used to validate transaction input before storing it
- Generators: `transaction_history()` yields records lazily
- Collections and aggregation: `defaultdict` groups values by category
- Functional programming: `filter()` is used to find records by category
- Serialization: JSON and CSV save/load patterns for persistence
- CLI flow control: menu-driven input with `while True` and conditional branching

## Example workflow

1. Run the app with `python3 main.py`
2. Choose `1` to add income or `2` to add an expense
3. Enter an amount and category
4. Choose `3` to view all transactions
5. Choose `4` to view the monthly report
6. Choose `6` to save and exit

## Why this project matters

This project is a bridge from beginner Python to real-world application thinking. It introduces the same ideas you will use in larger apps:

- modeling data
- validating input
- separating logic from storage
- handling persistence
- building simple user interfaces

## Continuation: full-stack app roadmap

This project can evolve into a full-stack application using modern web development patterns.

### Phase 1: Web API

Move the logic from the CLI into a backend API using Flask or FastAPI.

Concepts to introduce:

- REST endpoints for transactions
- request validation with Pydantic
- CRUD operations for expenses
- database integration with SQLite or PostgreSQL

### Phase 2: Database layer

Replace in-memory lists with database models.

Concepts to introduce:

- SQLAlchemy or Django ORM
- schema design
- migrations
- transactions and data integrity

### Phase 3: Frontend UI

Build a simple web dashboard with HTML, CSS, and JavaScript or React.

Concepts to introduce:

- API consumption from frontend
- forms and validation
- charts for income vs expense
- category summaries and filters

### Phase 4: Production-ready app

Add:

- authentication and user accounts
- monthly analytics
- export to CSV/PDF
- testing and CI/CD
- deployment to cloud services

## Suggested next project structure

```text
expense_fullstack/
├── backend/
│   ├── app/
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│   └── database.py
├── frontend/
│   ├── src/
│   └── public/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

## Git push instructions

If you want to push this folder to GitHub, run:

```bash
git init
git add .
git commit -m "Add expense tracker project"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## Summary

This project is a strong beginner-to-intermediate Python application. It introduces practical concepts while staying small and easy to understand. From here, the natural next step is a backend + frontend full-stack version that turns this tracker into a real, usable product.

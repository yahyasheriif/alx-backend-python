# Python Context Managers and Async Operations

This project explores the use of **context managers** and **asynchronous programming** in Python for managing database operations efficiently.

## Tasks

### 0. Custom Class-Based Context Manager for Database Connection
- File: `0-databaseconnection.py`
- Created a `DatabaseConnection` class implementing `__enter__` and `__exit__`.
- Automatically opens and closes SQLite connection.
- Executes a SELECT query using the `with` statement.

---

### 1. Reusable Query Context Manager
- File: `1-execute.py`
- Implemented a reusable context manager class `ExecuteQuery`.
- Accepts a dynamic query and parameters, executes it, and returns results.
- Manages DB connection and cursor lifecycle.

---

### 2. Concurrent Asynchronous Database Queries
- File: `3-concurrent.py`
- Used `aiosqlite` and `asyncio` to run concurrent database queries.
- Functions:
  - `async_fetch_users()` – fetches all users from the database.
  - `async_fetch_older_users()` – fetches users older than 40.
- Both functions **return** fetched rows and are executed in parallel using `asyncio.gather()`.

---

## Technologies Used
- Python 3.8+
- SQLite
- `aiosqlite`
- Context Managers
- AsyncIO

---

## How to Run
Make sure you have `aiosqlite` installed:
```bash
pip install aiosqlite
✅ README.md for python-decorators-0x01 – Task 0

# Python Decorators – Advanced Database Operations

This project demonstrates the use of **Python decorators** to enhance and streamline common database operations. The goal is to reduce boilerplate, add robustness, and improve efficiency and observability in database-driven Python applications.

---

## 📌 Task 0: Logging Database Queries

### Objective:
Create a decorator `log_queries` that logs all SQL queries executed by a decorated function, with a timestamp.

### Key Features:
- Logs SQL query with the current date and time using `datetime`.
- Keeps the original function behavior intact using `functools.wraps`.

### 🧠 Concepts Used:
- Python decorators
- `functools.wraps`
- `datetime.now().strftime()` for timestamp formatting
- SQLite3 database connection and query execution

### ✅ Sample Code:
```python
from datetime import datetime
import functools
import sqlite3

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        if query:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{now}] Executing SQL Query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
✅ Sample Output:

[2025-06-30 15:24:10] Executing SQL Query: SELECT * FROM users
[('001', 'yassinkhaled', 'yassin@example.com', 30), ...]


🧩 Task 1: Handle Database Connections with a Decorator
🎯 Objective:
Implement a decorator with_db_connection that automatically manages opening and closing of a SQLite database connection.

💡 Key Features:
Removes boilerplate connection handling.

Injects the connection (conn) into the decorated function.

Ensures proper cleanup using try...finally.

🧠 Concepts Used:
Python decorators

functools.wraps

Resource management with try...finally

SQLite connection injection

✅ Sample Code:
python
import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()
✅ Sample Output:
bash

('001', 'yassin khaled', 'yassin@example.com', 30)

🧾 Task 2: Transaction Management Decorator
🎯 Objective:
Create a @transactional decorator to wrap database operations inside a transaction. It should:

Commit changes when successful

Rollback if an error occurs

This ensures atomicity and protects data integrity during database updates.

🔧 Decorator Stack:
The function uses two decorators:

@with_db_connection: Handles opening/closing DB connections.

@transactional: Manages commit/rollback logic.

🧠 Concepts Used:
Python decorators

Error handling with try/except

SQLite transaction management

Decorator stacking

✅ Sample Code:
python

def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            print("[TRANSACTION] Committed successfully.")
            return result
        except Exception as e:
            conn.rollback()
            print(f"[TRANSACTION] Rolled back due to error: {e}")
            raise
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
✅ Sample Output:
pgsql

[TRANSACTION] Committed successfully.
Or, on failure:

pgsql

[TRANSACTION] Rolled back due to error: no such column: email_address


🔄 Task 3: Retry Database Queries
🎯 Objective:
Create a @retry_on_failure decorator that retries a database operation a set number of times if it fails due to an exception.

🧠 Concepts Used:
Python decorators with parameters

Retry logic

Exception handling and logging

Combining decorators (@with_db_connection + @retry_on_failure)

🧪 Parameters:
retries: Maximum number of retry attempts (default: 3)

delay: Seconds to wait between retries (default: 2)

✅ Sample Code:
python

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f"[RETRY] Attempt {attempt} failed due to: {e}")
                    if attempt < retries:
                        time.sleep(delay)
                    else:
                        print("[RETRY] All retry attempts failed.")
                        raise
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
🧪 Sample Output (Simulated Failure):
csharp

[RETRY] Attempt 1 failed due to: database is locked
[RETRY] Attempt 2 failed due to: database is locked
[RETRY] Attempt 3 failed due to: database is locked
[RETRY] All retry attempts failed.
Traceback (most recent call last):
...

🧠 Task 4: Cache Database Queries
🎯 Objective:
Implement a @cache_query decorator that stores the result of a SQL query, preventing redundant database calls and improving performance for frequently repeated queries.

🧠 Concepts Used:
Python function memoization

Custom caching with in-memory dictionary

Query-based cache key

Stacking with other decorators

💡 Key Features:
Caches results based on the SQL query string.

Prevents re-executing the same query if already cached.

Works seamlessly with @with_db_connection.

✅ Sample Code:
python

query_cache = {}

def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[1] if len(args) > 1 else None)
        if query in query_cache:
            print("[CACHE] Returning cached result.")
            return query_cache[query]
        print("[CACHE] Executing and caching result.")
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
🧪 Sample Output:
csharp

[CACHE] Executing and caching result.
[CACHE] Returning cached result.

🔁 Directory Structure
📂 Final Project Structure

python-decorators-0x01/
├── 0-log_queries.py
├── 1-with_db_connection.py
├── 2-transactional.py
├── 3-retry_on_failure.py
├── 4-cache_query.py
├── README.md
└── users.db



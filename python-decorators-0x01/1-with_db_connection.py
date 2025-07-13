import sqlite3
import functools

# ✅ Decorator to handle DB connection automatically
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

# ✅ Fetch user by ID with automatic connection handling
if __name__ == "__main__":
    user = get_user_by_id(user_id=1)
    print(user)

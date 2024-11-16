import sqlite3

DB_PATH = "choco.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    # Creating flavours table
    cursor.execute('''CREATE TABLE IF NOT EXISTS flavours (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        season TEXT NOT NULL,
        availability INTEGER NOT NULL CHECK (availability IN (0, 1))  -- Use 0 (False) or 1 (True)
    )''')

    # Creating inventory table
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        availability INTEGER NOT NULL CHECK (availability IN (0, 1))  -- Use 0 (False) or 1 (True)
    )''')

    # Creating allergies table
    cursor.execute('''CREATE TABLE IF NOT EXISTS allergies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        allergy TEXT NOT NULL,
        suggestion TEXT NOT NULL
    )''')

    connection.commit()
    connection.close()

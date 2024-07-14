import sqlite3


connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE entries (context TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    entries.append({"content": entry_content, "date": entry_date})


def get_entries():
    return entries
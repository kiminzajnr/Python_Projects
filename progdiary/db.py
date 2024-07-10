entries = []

def add_entry(entry_content, entry_date):
    entries.append({"content": entry_content, "date": entry_date})


def get_entries():
    return entries
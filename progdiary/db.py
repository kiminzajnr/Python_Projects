entries = []

def add_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")

    entries.append({"content": entry_content, "date": entry_date})


def view_entries():
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")
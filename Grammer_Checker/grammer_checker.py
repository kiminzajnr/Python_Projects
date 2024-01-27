import language_tool_python


def grammar_checker(text):
    tool = language_tool_python.LanguageTool('en-US', config={ 'cacheSize': 1000, 'pipelineCaching': True })
    matches = tool.check(text)


    if len(matches) > 0:
        print("\nGrammar issues found:")
        for match in matches:
            print(match.message)

    else:
        print("No grammar issues found")
        return

    print(f"\nThe corrected text is:\n{tool.correct(text)}")

def read_from_file(filename):
    with open(filename) as file:
        text_to_check = file.read()
    grammar_checker(text_to_check)


if __name__ == "__main__":
    while True:
        print("\nOptions:\n1: To check a text\n2: To check a file\n3: Quit")
        user_selection = input("\nEnter your option: ")

        if user_selection == "1":
            text_to_check = input("Enter the text you want to check for grammar: ")
            grammar_checker(text_to_check)

        elif user_selection == "2":
            file_name = input("Enter file name: ")
            read_from_file(file_name)

        elif user_selection == "3":
            print("Goodbye!")
            break
        
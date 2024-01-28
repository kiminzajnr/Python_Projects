import language_tool_python


def grammar_checker(text):
    """
    Check the grammar of the given text using LanguageTool.

    Parameters:
    - text (str): The input text to be checked.

    Returns: None
    """
    with language_tool_python.LanguageTool('en-US', config={ 'cacheSize': 1000, 'pipelineCaching': True }) as tool:
        matches = tool.check(text)


        if len(matches) > 0:
            print("\nGrammar issues found:")
            for match in matches:
                print(match.message)

            save_or_output = input("\nWould you like to save corrected sentence to a file? Yes/No: ")
            if save_or_output.lower() == "no":
                print(f"\nThe corrected text is:\n{tool.correct(text)}")

            elif save_or_output.lower() == "yes":
                file_name = input("Enter file name: ")
                write_to_file(file_name, tool.correct(text))

        else:
            print("No grammar issues found")
            return


def write_to_file(filename, text):
    """
    Write the given text to a file.

    Parameters:
    - filename (str): The name of the file.
    - text (str): The text to be written to the file.

    Returns: None
    """
    with open(filename, "w") as file:
        file.write(text)

def read_from_file(filename):
    """
    Read text from a file and perform grammar checking.

    Parameters:
    - filename (str): The name of the file to be read.

    Returns: None
    """
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
            print("\nGoodbye!")
            break
        
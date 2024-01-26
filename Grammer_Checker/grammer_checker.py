import language_tool_python


def grammar_checker(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)


    if len(matches) > 0:
        print("\nGrammar issues found:")
        for match in matches:
            print(match.message)

    else:
        print("No grammar issues found")
        return

    print(f"\nThe corrected sentence is:\n{tool.correct(text)}")


if __name__ == "__main__":
    text_to_check = input("Enter the text you want to check for grammar: ")
    grammar_checker(text_to_check)
    
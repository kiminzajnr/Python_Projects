# Python Mini Projects

# [CMD Todo App](/Todo_CMD_App/)

A command-line to-do app to manage your tasks effectively.

## Features

1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete tasks

Tasks are persistently stored in a JSON file

## Getting Started

1. Clone or download this repository:
```
https://github.com/kiminzajnr/Python_Mini_Projects.git
```
2. Navigate to the project directory: 
```
cd Python_Mini_Projects
```
3. Ensure you have Python installed on your system.
4. Run the app
```
python todo.py
```
## Usage

- Add a task: Enter 1 and provide the task description/name.
- Show tasks: Enter 2 to view a list of all tasks with their completion status.
- Complete a task: Enter 3 and specify the task ID to mark it as completed.
- Delete a task: Enter 4 and specify the task ID to remove it.
- Quit: Enter 5 to exit the app.

![usage_demo](/Todo_CMD_App/gif/demo.gif)

## File Structure

- `todo.py`: Main Python script containing the todo app logic.
- `tasks.json`: JSON file to persist tasks.
## Contributing

Pull requests are welcome!

## License

This project is licensed under the MIT License.

=============================

# [Grammar Checker](/Grammer_Checker/) ![Alt text](image.png)

Grammar Checker is a simple Python program that uses the [language_tool_python](https://pypi.org/project/language-tool-python/) library to check grammar in a given text or file.

## Features

- Check grammar issues in text.
- Save corrected sentences to a file.
- Check grammar in a file.

## Getting Started

1. Clone the Repository $ Navigate to the project directory:
```
git clone https://github.com/kiminzajnr/Python_Mini_Projects.git
cd /Python_Mini_Projects/Grammer_Checker/
```

2. Install Dependencies:
```
pip install -r requirements.txt
```

3. Run the Program:
```
python grammar_checker.py
```

## Usage
The program provides two options:

1. Check grammar in a text.
2. Check grammar in a file.
Follow the on-screen prompts to use the program. You can choose to save corrected sentences to a file.

## Dependencies
- [language_tool_python](https://pypi.org/project/language-tool-python/): An open-source grammar checker for Python. 📝

## Contributing
If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch `git checkout -b feature/your-feature-name`.
3. Commit your changes `git commit -am 'Add new feature'`.
4. Push to the branch `git push origin feature/your-feature-name`.
5. Create a new pull request.

## License
This project is licensed under the MIT License.


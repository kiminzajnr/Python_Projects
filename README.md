# Python Mini Projects

## Table of Contents
- [SSH key Uploader](#ssh-key-uploader)
- [CMD Todo App](#CMD-Todo-App)
- [Grammar Checker](#Grammar-Checker)
- [End of civilization predictor](#End-of-civilization-predictor)
- [Automated File Organizer](#Automated-File-Organizer)

# SSH Key Uploader

Uploads a public key to server/s

## Getting Started

```
git clone https://github.com/kiminzajnr/Python_Projects.git
```

```
cd ython_Projects/learner-pub-key-uploader
python3 -m venv .venv
. .venv/bin/activate
pip install Flask
```

```
python3 app.py
```
```
touch ~/.ssh/priv.key # add your private key here
chmod 400 ~/.ssh/priv.key
```


## Prerequisites

Refer to `Getting Started`


## Deployment

On your server:

```
touch ~/.ssh/priv.key # add your private key here
chmod 400 ~/.ssh/priv.key
```
```
git clone https://github.com/kiminzajnr/Python_Projects.git
```
```
cd learner-pub-key-uploader
python3 -m venv .venv
. .venv/bin/activate
pip install Flask
pip install gunicorn
```
```
touch wsgi.py
```
```
vi wsgi.py
```
and add:
```
from app import app


if __name__ == "__main__":
    app.run()

```
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```
```
deactivate
```
```
sudo vi /etc/systemd/system/app.service
```
and add
```
[Unit]
Description=Gunicorn instance to server app Flask app
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/My_App/learner-pub-key-uploader
Environment="Path=/home/ubuntu/My_App/learner-pub-key-uploader/.venv/bin"
ExecStart=/home/ubuntu/My_App/learner-pub-key-uploader/.venv/bin/gunicorn --workers 3 --bind unix:app.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```
```
sudo systemctl start app
```
```
sudo systemctl enable app # You might have to run sudo systemctl daemon-reload first
```
```
sudo systemctl status app # Should be active and running
```
```
sudo apt install nginx
```
```
sudo vi /etc/nginx/site-available/app.conf
```
and add:
```
server {
        listen 80;
        server_name alx1.parallel-cumpus.tech;

        location / {
                include proxy_params;
                proxy_pass http://unix:/home/ubuntu/My_App/learner-pub-key-uploader/app.sock;
        }
}

```
```
sudo ls -s /etc/nginx/site-available/app.conf /etc/nginx/site-enabled/
```
```
sudo nginx -t # test should be successful and syntax ok
```
```
sudo systemctl restart nginx
```
```
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow "Nginx Full"
```
Test your app. If you get `502 Bad Gateway`, run:
```
sudo chmod 775 /home/user
```

> setting up https with let's encrypt
```
sud apt update; sudo snap install core; snap refresh core
```
```
sudo snap install --classic certbot
```
```
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```
```
sudo certbot --nginx
```

## Built with

- <img src="https://img.icons8.com/ios/452/flask.png" alt="Flask" width="20" height="20" style="filter: invert(45%) sepia(100%) saturate(2525%) hue-rotate(88deg) brightness(94%) contrast(91%);"/> [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- <img src="https://img.icons8.com/ios/452/console.png" alt="Bash" width="20" height="20" style="filter: invert(45%) sepia(100%) saturate(2525%) hue-rotate(88deg) brightness(94%) contrast(91%);"/> [Bash](https://www.gnu.org/software/bash/)
- <img src="https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png" alt="HTML" width="20" height="20"/> [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- <img src="https://cdn.iconscout.com/icon/free/png-512/css3-9-1175237.png" alt="CSS" width="20" height="20"/> [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)


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


=============================================


# [End of civilization predictor](/Python_Mini_Projects/EOC_Predictor/)
*Note, This Is Entirely Fictional*

## Overview

The End of Civilization Predictor is a Python script that simulates various factors contributing to the potential end of civilization. It provides a probability-based simulation, allowing users to customize the duration of the simulation and receive warnings if the probability of civilization ending is high.

## Features

- Simulates the impact of factors such as climate change, overpopulation, probability of war, deadly pathogens, and technological catastrophes.
- Provides a customizable simulation duration.
- Displays warnings if the probability of civilization ending is high.

## Getting Started

1. Clone the repository:
   ```bash
   https://github.com/kiminzajnr/Python_Mini_Projects.git
   cd end-of-civilization-predictor
2. Run the script:
    ```
    python end_of_civilization.py
3. Follow the on-screen prompts to customize the simulation.

## Factors and Probabilities
The simulation considers the following factors and their probabilities:

- Climate Change: 30%
- Overpopulation: 20%
- Probability of War: 25%
- Deadly Pathogens: 15%
- Technological Catastrophe: 10

## Customization
You can customize the simulation by entering the number of years you want to simulate. The script will then simulate the impact of factors over the specified duration.

## Warning
If the overall probability of civilization ending is higher than 50%, the script displays a warning, suggesting users take necessary precautions.

## Contributing
If you'd like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch `git checkout -b feature/your-feature-name`.
- Commit your changes `git commit -am 'Add new feature`.
- Push to the branch `git push origin feature/your-feature-name`.
- Create a new pull request.

## Acknowledgments
- [Python](https://www.python.org/): The programming language used for this project.
- [Random Library](https://docs.python.org/3/library/random.html): Used for generating random values.



======================================================

# [Automated File Organizer](/File_Organizer/)

This script organizes files in a directory based on their types (e.g., images, documents, videos) using file extensions to determine file types.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Command-Line Interface](#command-line-interface)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Features

- **File Organization:** Automatically organizes files into directories based on their types.
- **File Type Recognition:** Determines file types using file extensions.

## Usage

1. Clone the repository:
```
git clone https://github.com/kiminzajnr/Python_Mini_Projects.git
```
2. Navigate to the project directory:
```
cd Python_Mini_Projects/File_Organizer
```
3. Run the script:
```
python3 file_organizer.py source_directory destination_directory
```
Replace source_directory and destination_directory with the actual paths.

# Installation
```
pip install click
```

# Command-Line Interface
The script supports a command-line interface (CLI) using the `click` library. You can specify source and destination directories directly from the command line.
`python file_organizer.py source_directory destination_directory`

# Logging
The script generates a log file `file_organizer.log` to keep track of files being organized and any errors encountered during the process.

# Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

# License
This project is licensed under the MIT License


==================================================================

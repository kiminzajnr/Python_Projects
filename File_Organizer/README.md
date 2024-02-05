# Automated File Organizer

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

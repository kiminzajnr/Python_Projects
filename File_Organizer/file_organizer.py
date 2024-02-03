# Create a script that organizes files in a directory based on their types (e.g., images, documents, videos).
# You can use file extensions or content analysis to determine file types.


import logging
from os import path, makedirs, listdir
from shutil import move

logging.basicConfig(filename="file_organizer.log", level=logging.INFO)


def create_destination_dirs(destination_dir, file_types):
    """
    Create destination directories based on file types.
    """
    for file_type in file_types:
        dir_path = path.join(destination_dir, file_type)
        makedirs(dir_path, exist_ok=True)

def list_files_in_dir(source_dir):
    """
    List files in the source directory.
    """
    if len(listdir(source_dir)) == 0:
        print(f"directory '{source_dir}' is empty")
        logging.info(f"directory {source_dir} is empty")
    
    else:
        print(f"\nFiles in {source_dir}:")
        for filename in listdir(source_dir):
            file_path = path.join(source_dir, filename)
            if path.isfile(file_path):
                print(f"- {filename}")

def organize_files(source_dir, destination_dir):
    """
    Organize files based on their type
    """
    file_types = {
        "images": [".jpg", ".png", ".gif"],
        "documents": [".pdf", ".doc", ".docx", ".txt", ".md"],
        "videos": [".mp4", ".mkv", ".avi"],
    }

    for filename in listdir(source_dir):
        file_path = path.join(source_dir, filename)
      
        if path.isfile(file_path):
            try:
                file_ext = path.splitext(filename)[1].lower()
                for category, extensions in file_types.items():
                    if file_ext in extensions:
                        destination = path.join(destination_dir, category, filename)
                        move(file_path, destination)
                        print(f"Moved {filename} to {destination}")
                        logging.info(f"Moved {filename} to {destination}")
                        break

                else:
                    # Files with unknown extensions to 'others' dir
                    destination = path.join(destination_dir, 'others', filename)
                    move(file_path, destination)
                    print(f"Moved {filename} to {destination}")
                    logging.info(f"Moved {filename} to {destination}")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                logging.error(f"Error processing {filename}: {e}")




def main():
    try:
        # file types
        file_types = ['images', 'documents', 'videos', 'others']

        # source and destination dirs given by user
        source_dir = input("Enter the source directory: ")
        destination_dir = input("Enter the destination directory: ")

        # check if source dir exits
        if not path.exists(source_dir) or not path.isdir(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' not found.")
        
        # check and create source dir if it does not exist
        if not path.exists(destination_dir):
            makedirs(destination_dir)
        elif not path.isdir(destination_dir):
            raise NotADirectoryError(f"Destination path '{destination_dir}' is not a directory")

        # create destination directories
        create_destination_dirs(destination_dir, file_types)

        # list files in the source dir
        list_files_in_dir(source_dir)

        # Organize files
        organize_files(source_dir, destination_dir)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
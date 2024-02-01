# Create a script that organizes files in a directory based on their types (e.g., images, documents, videos).
# You can use file extensions or content analysis to determine file types.

from os import path, makedirs, listdir

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
    print(f"\nFiles in {source_dir}:")
    for filename in listdir(source_dir):
        file_path = path.join(source_dir, filename)
        if path.isfile(file_path):
            print(f"- {filename}")


def main():
    # file types
    file_types = ['images', 'documents', 'videos']

    # source and destination dirs given by user
    source_dir = input("Enter the source directory: ")
    destination_dir = input("Enter the destination directory: ")

    # create destination directories
    create_destination_dirs(destination_dir, file_types)

    # list files in the source dir
    list_files_in_dir(source_dir)

if __name__ == "__main__":
    main()
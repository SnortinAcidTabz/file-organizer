import os
import shutil
from datetime import datetime
from pathlib import Path

CURRENT_FOLDER = Path.cwd()
SCRIPT_NAME = Path(__file__).name

def create_folder(folder_name):
    folder_path = CURRENT_FOLDER / folder_name
    folder_path.mkdir(exist_ok=True)
    return folder_path

def organize_by_extension():
    for file in CURRENT_FOLDER.iterdir():
        if file.is_file() and file.name != SCRIPT_NAME:
            extension = file.suffix.lower().replace(".", "")

            if not extension:
                extension = "no_extension"

            target_folder = create_folder(f"Extension_{extension}")
            shutil.move(str(file), str(target_folder / file.name))

    print("Files Organized by extension.")

def organize_by_creation_date():
    for file in CURRENT_FOLDER.iterdir():
        if file.is_file() and file.name != SCRIPT_NAME:
            creation_date = file.stat().st_ctime
            date_folder_name = datetime.fromtimestamp(creation_date).strftime("%Y_%m_%d")

            target_folder = create_folder(f"Created_{date_folder_name}")
            shutil.move(str(file), str(target_folder / file.name))

    print("files Organized by creation date. ")

def organize_by_size():
    for file in CURRENT_FOLDER.iterdir():
        if file.is_file() and file.name != SCRIPT_NAME:
            size_mb = file.stat().st_size / (1024 * 1024)

            if size_mb < 1:
                folder_name = "Size_Small_Under_1MB"
            elif size_mb < 100:
                folder_name = "Size_Medium_1MB_to_100MB"
            else:
                folder_name = "Size_Large_Over_100MB"

            target_folder = create_folder(folder_name)
            shutil.move(str(file), str(target_folder / file.name))

        print("Files Organized by size.")

def main():
    print("File Organizer")
    print("---------------")
    print("1. Organize by extension")
    print("2. Organize by creation date")
    print("3. Organize by size")

    choice = input("Enter your organization method: ")

    if choice == "1":
        organize_by_extension()
    elif choice == "2":
        organize_by_creation_date()
    elif choice == "3":
        organize_by_size()
    else:
        print("Please enter a valid option.")

if __name__ == "__main__":
    main()

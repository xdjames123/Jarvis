import os
import shutil
import subprocess

def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
        return f"Folder '{folder_name}' created successfully."
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")
        return f"Folder '{folder_name}' already exists."
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

def create_file(file_name, folder_name=None):
    try:
        if folder_name:
            # Ensure the folder exists
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            
            file_path = os.path.join(folder_name, file_name)
        else:
            file_path = file_name

        with open(file_path, 'w') as f:
            f.write("")  # Create an empty file
        print(f"File '{file_name}' created successfully, Sir.")
        return f"File '{file_name}' created successfully, Sir."
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

def delete_file_or_folder(file_or_folder):
    try:
        if os.path.isfile(file_or_folder):
            os.remove(file_or_folder)
            print(f"Sure Sir, file '{file_or_folder}' deleted successfully.")
            return f"Sure Sir, file '{file_or_folder}' deleted successfully."
        elif os.path.isdir(file_or_folder):
            shutil.rmtree(file_or_folder)
            print(f"Alright Sir,folder '{file_or_folder}' deleted successfully.")
            return f"Alright Sir,folder '{file_or_folder}' deleted successfully."
        else:
            print(f"'{file_or_folder}' does not exist.")
            return f"'{file_or_folder}' does not exist."
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

def open_folder_or_file(path):
    try:
        if os.path.isfile(path):
            subprocess.run(["open", path])
            print(f"Opening file: {path}")
        elif os.path.isdir(path):
            subprocess.run(["open", path])
            print(f"Opening folder: {path}")
        else:
            print(f"'{path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

def handle_folder_commands(command):
    command = command.lower()  # Normalize input for case-insensitivity
    if "create a folder" in command:
        folder_name = command.replace("create a folder", "").strip()
        return create_folder(folder_name) if folder_name else "Please specify a folder name."
    elif "create a file" in command:
        parts = command.split("inside")
        file_name = parts[0].replace("create a file", "").strip()
        folder_name = parts[1].strip() if len(parts) > 1 else None
        return create_file(file_name, folder_name) if file_name else "Please specify a file name."
    elif "delete" in command:
        target = command.replace("delete", "").strip()
        return delete_file_or_folder(target) if target else "Please specify what to delete."
    elif "open" in command:
        target = command.replace("open", "").strip()
        return open_folder_or_file(target) if target else "Please specify a file or folder to open."
    else:
        return "I did not understand that command."

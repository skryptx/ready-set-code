import os 

def rename_folders_in_directory(directory_path):
    """
    Renames folders within a given directory based on a specified pattern. 
    
    Args:
        directory_path (str): The path to the directory containing the folders to rename.
    """
    for folder in os.listdir(directory_path):
        if os.path.isdir(os.path.join(directory_path, folder)):
            # Modify this line to implement your desired renaming logic
            new_name = folder.replace(" ", "_") 
            old_path = os.path.join(directory_path, folder)
            new_path = os.path.join(directory_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed '{folder}' to '{new_name}'") 
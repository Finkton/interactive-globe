import os

# Define the directory path
directory = './'  # Replace with your directory path

# Function to delete files with "tile" in the filename
def delete_tile_files(directory):
    # List all files in the directory
    files = os.listdir(directory)

    # Iterate through the files and delete those containing "tile"
    for file in files:
        if "tile" in file and os.path.isfile(os.path.join(directory, file)):
            os.remove(os.path.join(directory, file))
            print(f"Deleted: {file}")

# Call the function to delete the files
delete_tile_files(directory)
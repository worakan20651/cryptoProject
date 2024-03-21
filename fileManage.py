import os
from PIL import Image


def read_image_with_metadata(file_path):
    filename = file_path
    try:
        # Open the image file
        img = Image.open(filename, mode='r')

        # Convert the image to RGB mode if it's not already in RGB mode
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Convert the image to raw data
        raw_data = img.tobytes()

        # Get metadata if needed
        metadata = img.info

        # Close the image file
        img.close()
        return metadata, raw_data
    
    except FileNotFoundError:
        print("File not found")
        return None, None
    except IOError:
        print("IO Error")
        return None, None

def writeFile(content, fileName):
    base_name, file_extension = os.path.splitext(fileName)
    new_file= f"{base_name}_{1}{file_extension}"
    try:
        with open(new_file, "w") as file:
            file.write(content)
    except Exception:
        print("something went wrong while writing file")
        
def readFile(fileName):
    try:
        with open(fileName, "r") as file:
            content = file.read()
    except IOError:
        print("file not found")
        
    return content
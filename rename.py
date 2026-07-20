import os

# Get the directory where this script is located, then add the 'frames' folder to the path
base_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(base_dir, "frames")

# Get all files in the frames folder and sort them
files = sorted(os.listdir(folder_path))

# Filter for images and rename them
image_count = 1
for filename in files:
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Create the new name (e.g., 0001.jpg)
        file_extension = os.path.splitext(filename)[1]
        new_name = f"{image_count:04d}{file_extension}"
        
        # Rename the file
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        os.rename(old_file, new_file)
        image_count += 1

print(f"Successfully renamed {image_count - 1} images!")
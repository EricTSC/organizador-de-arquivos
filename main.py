import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")
images_folder = os.path.expanduser("~/Downloads/images")

os.makedirs(images_folder, exist_ok=True)

for file_name in os.listdir(downloads_folder):
    if file_name.endswith(".png") or file_name.endswith(".jpg"):
        file_path = os.path.join(downloads_folder, file_name)
        try:
            shutil.move(file_path, images_folder)
        except shutil.Error:
            print(f"{file_name} already exists in the destination folder")

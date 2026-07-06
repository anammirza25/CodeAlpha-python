import os
import shutil
count = 0
source_folder = "Source_Folder"
destination_folder = "Destination_Folder"
files = os.listdir(source_folder)
print(files)
for file in files:
    if file.endswith(".jpg"):
        shutil.move(
        os.path.join(source_folder, file),
        os.path.join(destination_folder, file)
        )
        count += 1
        print(file, "moved successfully!")
if count == 0:
    print("JPG file not found")
else:
    print("Total JPG Files moved:", count)
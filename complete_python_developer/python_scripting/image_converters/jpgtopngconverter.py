# program to convert the jpg to png. Take the source and the target folder from the user
import os
from PIL import Image, ImageFilter
import pdb


TARGET_FORMAT = 'png'

#read input
source_folder = input("Please enter the source folder: ")
target_folder = input("Please enter the target folder: ")
print(source_folder)
print(target_folder)

# Get a list of the files in the directory
files = os.listdir(source_folder)

if files:
    targetdir_path = target_folder.replace('\\','')
    os.makedirs(target_folder,exist_ok=True)

# print the names of all files
for file in files:
    filePath = f'randompics\{file}'
    print(f'FilePath: {filePath}')
    img = Image.open(filePath)
    writefilepath = f'{target_folder}\{file.replace('jpg',TARGET_FORMAT)}'
    print(f'WriteFile Path: {writefilepath}')
    img.save(writefilepath, TARGET_FORMAT)
    

import PyPDF2
import sys
import os

# read the path of the folder that has the pdf files
folder_path = input("Enter the path of the folder that has the pdf files: ")
os.chdir(folder_path)
print(os.getcwd())
contents = os.listdir(folder_path)
merger = PyPDF2.PdfMerger()
for item in contents:
    if item.endswith('.pdf'):
        merger.append(item)
        print(item)
merger.write('appended_version.pdf')

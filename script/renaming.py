import os
import argparse

# Renomme les images du dossier en entrée en leur attribuant des numéros à partir de 0
# Usage : python renaming.py -f <chemin du dossier en entrée>


def process_file(filepath,nb):
    dirname = os.path.dirname(filepath)
    try:
        os.rename(filepath,os.path.join(os.path.dirname(filepath),f"{nb}.jpg"))
    except FileExistsError as f:
        print(f)


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True,
	help="folder that contains images")
args = vars(ap.parse_args())
folder_path = args["folder"]
if os.path.exists(folder_path):
    for index,file_name in enumerate(os.listdir(folder_path)):
            file_path = os.path.join(folder_path, file_name)
            process_file(file_path,index)
    print("All file renamed!")
else:
    print("Folder path does not exist:", folder_path)

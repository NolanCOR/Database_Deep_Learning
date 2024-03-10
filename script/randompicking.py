import os
import argparse
import random
import shutil

# Répartit aléatoirement les images du dossier en entrée dans les dossiers en sortie selon les proportions indiquées
# Usage : python randompicking.py -i <chemin du dossier en entrée> -o <chemins des dossiers en sortie, séparés par des espaces> -n <nombre d'images par dossier, séparés par des espaces>

# processImg : Fonction qui permet de copier une image d'un dossier d'entrée vers un dossier de sortie en changeant son nom
# Input : 
#        - inputPath :  dossier d'entrée
#        - outputPath : dossier de sortie
#        - filename : nouveau nom de l'image
        
def processImg(inputPath,outputPath,filename):
    print(f"Renaming : \n {inputPath}{filename}.jpg  \n to {outputPath}")
    shutil.copyfile(f"{inputPath}{filename}.jpg",f"{outputPath}{filename}.jpg")

# Parseur d'arguments  
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="folder that contains input images")
ap.add_argument("-o", "--outputs", required=True,
	help="folders that contain output images.",nargs='+', type=str)
ap.add_argument("-n", "--numbers", required=True,
	help="number of images in each folder.",nargs='+', type=int)
args = vars(ap.parse_args())

input_folder = args["input"]
output_folders = args["outputs"]
proportions = args["numbers"]


available = [x for x in range(len(os.listdir(input_folder)))] # Images encore disponible
for index,output_folder in enumerate(output_folders):
    # Vérifier si le dossier de sortie existe sinon le créer
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    print(len(os.listdir(input_folder)))
    nbImg = proportions[index]
    for i in range(nbImg):
        nbChosen = random.choice(available) # Choisi une image aléatoirement
        processImg(input_folder,output_folder,nbChosen)
        available.remove(nbChosen)
print("All done !")

        
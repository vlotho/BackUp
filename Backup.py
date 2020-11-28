# -*- coding: utf-8 -*-

from configparser import ConfigParser   # permet la lecture et l'importation des variables contenu dans le fichier ini
import tarfile                          # permet la compression des fichiers
import os, time                         # os effectue des manipulations système et time tout ce qui est lié au temps
import shutil                           # manipulation de fichiers
from InterfaceSaisie import *

# fonction gérant l'option compression de la sauvegarde
def make_compression(output_filename, source_dir):
    try:
        with tarfile.open(output_filename, "w:gz") as tar:   # crée le fichier en ecriture avec compression gz et l'assigne à la variable tar
            tar.add(source_dir, recursive=True, arcname=os.path.basename(source_dir)) # ajoute les fichiers donnés en paramètre à l'archive 
    except IOError:
        print("Levée lorsqu'une fonction système retourne une erreur liée au système, incluant les erreurs entrées-sorties telles que fichier non trouvé ou disque plein")

        
# fonction gérant l'option copie de la sauvegarde
def make_copie(source_dir, dest_dir):
    try:
        shutil.copytree(source_dir, dest_dir)  # copie de répertoire
    except IOError:
        print("Levée lorsqu'une fonction système retourne une erreur liée au système, incluant les erreurs entrées-sorties telles que fichier non trouvé ou disque plein")
        
def make_dir():
    if not os.path.exists(path_dest):
        os.makedirs(path_dest, exist_ok=True)
    else:
        pass
   
# Permet la compression ou la copie des répertoires à sauvegarder 
def backup():
    try:
        if compress_copie_select == "1":
            nom_fichier = VarNomSauvegarde+time.strftime("-%d-%m-%Y")+".tar.gz"  # met en forme le nom du fichier avec la date du jour
            make_compression(nom_fichier, path_source) # declanche la compression
            shutil.move(nom_fichier, path_dest) # déplace les fichiers dans le bon répertoire
        elif compress_copie_select == "2":
            nom_repertoire = VarNomSauvegarde+time.strftime("-%d-%m-%Y")
            make_copie(path_source, path_dest + '/' + nom_repertoire)
    except IOError:
         print("Levée lorsqu'une fonction système retourne une erreur liée au système, incluant les erreurs entrées-sorties telles que fichier non trouvé ou disque plein")

def rotation():
    try:
        for files in os.listdir(path_dest):   # parcours le répertoire de la sauvegarde et liste les fichiers dans la variable files
            files = os.path.join(path_dest, files)
            if os.stat(files).st_mtime < date_jour - (rotation*86400): # pour chaque fichier récupère la date de dernière modification dans l'objet stat
                os.remove(files)
    except IOError:
         print("Levée lorsqu'une fonction système retourne une erreur liée au système, incluant les erreurs entrées-sorties telles que fichier non trouvé ou disque plein")

# on crée un objet config parser et on lit le paramétrage .ini
# config = ConfigParser()
# config.read('parametrage.ini')
#
# for section in config.sections():
#     # récupération de tous les paramètres
#     NomDeLaSauvegarde = config.get(section, 'NomDeLaSauvegarde')
#     CheminDuContenuASauvegarder = config.get(section, 'CheminDuContenuASauvegarder')
#     RepertoireDeLaSauvegarde = config.get(section, 'RepertoireDeLaSauvegarde')
#     CompressionOuCopie = config.get(section, 'CompressionOuCopie')
#     Rotation = config.get(section, 'Rotation')
#     Rotation_float = float(Rotation)
date_jour = time.time()
make_dir()
backup()
rotation()
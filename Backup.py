# -*- coding: utf-8 -*-

from configparser import ConfigParser
import tarfile
import os
import platform
import subprocess
import crontab


# on crée un objet config parser et on lit le paramétrage .ini
config = ConfigParser()  
config.read('parametrage.ini')
    
# récupération de toutes les paramètres
NomDeLaSauvegarde = config.get('parametre', 'NomDeLaSauvegarde')
CheminDuContenuASauvegarder = config.get('parametre', 'CheminDuContenuASauvegarder')
RepertoireDeLaSauvegarde = config.get('parametre', 'RepertoireDeLaSauvegarde')
CompressionOuCopie = config.get('parametre', 'CompressionOuCopie')
FrequenceDeSauvegarde = config.get('parametre', 'FrequenceDeSauvegarde')
Rotation = config.get('parametre', 'Rotation')

def make_compression(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
        
def make_copie(dest_dir, source_dir):
    if platform.system() == 'Windows':
        subprocess.call(['copy', source_dir, dest_dir])
    elif platform.system() == 'Linux':
        subprocess.call(['cp', source_dir, dest_dir])
    
        
#def frequence(jesaispas):
    # création d'une tache cron qui s'exécutera toutes 5min 
    # la fonction vérifira la date des fichiers sauvegardés et en fonction
    # de la rotation écrasera la première sauvegarde
    
    
        
def backup():
#    try:
    if CompressionOuCopie == "Compression":
        make_compression(NomDeLaSauvegarde+".tar.gz", CheminDuContenuASauvegarder)        
    elif CompressionOuCopie == "Copie":
        make_copie(RepertoireDeLaSauvegarde, CheminDuContenuASauvegarder)

#    except:
#        print("ça fonctionne pas")

# sauvegarder tous les jours et tous les 3 jours écraser le premier jour de sauvegarde.   

backup()

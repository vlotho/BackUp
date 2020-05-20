# -*- coding: utf-8 -*-

from configparser import configparser
import tarfile
import os
import platform
import subprocess
import crontab

#NomDeLaSauvegarde = "SauvegardeTest"
#CheminDuContenuASauvegarder = "C:/Users/Gilles/Documents/Cubietruck+Case"
#RepertoireDeLaSauvegarde = "C:/Users/Gilles/Documents/ProjetPython-Openclassrooms/"
#CompressionOuCopie = "Copie"
#FrequenceDeSauvegarde = 1
#Rotation = 3

parser = configparser()
parser.read('parametrage.ini')

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
        
def frequence(jesaispas):
    cron = crontab(user='root')
    job = cron.new(command='python Backup.py')
    job.day.every(jesaispas)
    cron.write()
        
def backup():
#    try:
        if parser.get('parametre', 'CompressionOuCopie') == "Compression":
            make_tarfile(parser.get('parametre', 'NomDeLaSauvegarde')+".tar.gz", parser.get('parametre', 'CheminDuContenuASauvegarder'))        
        elif parser.get('parametre', 'CompressionOuCopie') == "Copie":
            if platform.system() == 'Windows':
                subprocess.call(['copy', parser.get('parametre', 'CheminDuContenuASauvegarder'), parser.get('parametre', 'RepertoireDeLaSauvegarde')])
            elif platform.system() == 'Linux':
                subprocess.call(['cp', parser.get('parametre', 'CheminDuContenuASauvegarder'), parser.get('parametre', 'RepertoireDeLaSauvegarde')])


#    except:
#        print("ça fonctionne pas")

# sauvegarder tous les jours et tous les 3 jours écraser le premier jour de sauvegarde.   

if frequence(parser.get('parametre', 'FrequenceDeSauvegarde')):
    backup()

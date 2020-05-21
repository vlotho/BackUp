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
        
        
def backup():
    with open(NomDeLaSauvegarde, "w") as NomDeLaSauvegarde:
        
backup()

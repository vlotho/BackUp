# -*- coding: utf-8 -*-


#import json
import tarfile
import os
import platform

NomDeLaSauvegarde = "SauvegardeTest"
CheminDuContenuASauvegarder = "C:\/Users\/Gilles\/Documents\/Cubietruck+Case"
RepertoireDeLaSauvegarde = "C:\/Users\/Gilles\/Documents\/ProjetPython-Openclassrooms\/"
CompressionOuCopie = "Copie"
FrequenceDeSauvegarde = 1
Rotation = 3
 
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
        
def backup():
#    try:
        if CompressionOuCopie == "Compression":
            make_tarfile(NomDeLaSauvegarde+".tar.gz", CheminDuContenuASauvegarder)        
        elif CompressionOuCopie == "Copie":
            if platform.system() == 'Windows':
                os.system("copy " +CheminDuContenuASauvegarder+" "+RepertoireDeLaSauvegarde)
            elif platform.system() == 'Linux':
                os.system("cp " +CheminDuContenuASauvegarder+" "+RepertoireDeLaSauvegarde)
        print("Répertoire sauvegardé")
#    except:
#        print("ça fonctionne pas")

backup()

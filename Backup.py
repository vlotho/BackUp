# -*- coding: utf-8 -*-

'''
   Conçut par Dalmas Gilles
   Pour le projet 6 - Participez à la vie de la communauté Open Source
   De la formation AIC d'OpenClassRooms
   
   La version de python utilisé est la 3.7.6

'''

from configparser import ConfigParser   # permet la lecture et l'importation des variables contenu dans le fichier ini
import tarfile                          # permet la compression des fichiers
import os, time                         # os effectue des manipulations système et time tout ce qui est lié au temps
import shutil                           # manipulation de fichiers


# fonction gérant l'option compression de la sauvegarde
def make_compression(output_filename, source_dir):
    try:
        with tarfile.open(output_filename, "w:gz") as tar:   # crée le fichier en ecriture avec compression gz et l'assigne à la variable tar
            tar.add(source_dir, recursive=True, arcname=os.path.basename(source_dir)) # ajoute les fichiers donnés en paramètre à l'archive 
    except NameError:
        print("La variable numerateur ou denominateur n'a pas été définie.")
    except AttributeError:
        print("Une référence ou une assignation d'attribut a échoué")
    except SyntaxError:
        print("Levée lorsque l'analyseur syntaxique rencontre une erreur de syntaxe.")
    except IOError:
        print("Levée lorsqu'une fonction système retourne une erreur liée au système, incluant les erreurs entrées-sorties telles que fichier non trouvé ou disque plein")
    except ImportError:
        print("Levée lorsque l'instruction import a des problèmes pour essayer de charger un module. Également levée lorsque Python ne trouve pas un nom dans from ... import.")
    except IndentationError:
        print("Erreur de syntaxe liées à une indentation incorrecte.")
    except TypeError:
        print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
    except ZeroDivisionError:
        print("La variable denominateur est égale à 0.")
        
# fonction gérant l'option copie de la sauvegarde
def make_copie(dest_dir, source_dir):
    try:
        shutil.copytree(source_dir, dest_dir)  # copie de répertoire
    except NameError:
        print("La variable numerateur ou denominateur n'a pas été définie.")
    except AttributeError:
        print("Une référence ou une assignation d'attribut a échoué")
    except SyntaxError:
        print("Levée lorsque l'analyseur syntaxique rencontre une erreur de syntaxe.")
    except IOError:
        print("Levée lorsqu'une fonction système retourne une erreur liée au système, incluant les erreurs entrées-sorties telles que fichier non trouvé ou disque plein")
    except ImportError:
        print("Levée lorsque l'instruction import a des problèmes pour essayer de charger un module. Également levée lorsque Python ne trouve pas un nom dans from ... import.")
    except IndentationError:
        print("Erreur de syntaxe liées à une indentation incorrecte.")
    except TypeError:
        print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
    except ZeroDivisionError:
        print("La variable denominateur est égale à 0.")
   
# Permet la compression ou la copie des répertoires à sauvegarder 
def backup():
    try:
        if CompressionOuCopie == "Compression":
            nom_fichier = NomDeLaSauvegarde+time.strftime("-%Y-%m-%d")+".tar.gz"  # met en forme le nom du fichier avec la date du jour
            make_compression(nom_fichier, CheminDuContenuASauvegarder) # declanche la compression
            shutil.move(nom_fichier, RepertoireDeLaSauvegarde) # déplace les fichiers dans le bon répertoire
        elif CompressionOuCopie == "Copie":
            nom_repertoire = NomDeLaSauvegarde+time.strftime("-%Y-%m-%d")
            make_copie(RepertoireDeLaSauvegarde+'/'+nom_repertoire, CheminDuContenuASauvegarder)

    except NameError:
        print("La variable numerateur ou denominateur n'a pas été définie.")
    except AttributeError:
        print("Une référence ou une assignation d'attribut a échoué")
    except SyntaxError:
        print("Levée lorsque l'analyseur syntaxique rencontre une erreur de syntaxe.")
    except IOError:
        print("Levée lorsqu'une fonction système retourne une erreur liée au système, incluant les erreurs entrées-sorties telles que fichier non trouvé ou disque plein")
    except ImportError:
        print("Levée lorsque l'instruction import a des problèmes pour essayer de charger un module. Également levée lorsque Python ne trouve pas un nom dans from ... import.")
    except IndentationError:
        print("Erreur de syntaxe liées à une indentation incorrecte.")
    except TypeError:
        print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
    except ZeroDivisionError:
        print("La variable denominateur est égale à 0.")


def rotation():
    try:
        for files in os.listdir(RepertoireDeLaSauvegarde):   # parcours le répertoire de la sauvegarde et liste les fichiers dans la variable files
            if os.stat(os.path.join(RepertoireDeLaSauvegarde, files)).st_mtime < date_jour - (Rotation_float*86400): # pour chaque fichier récupère la date de dernière modification depuis l'objet stat
                os.remove(os.path.join(RepertoireDeLaSauvegarde, files))
    except NameError:
        print("La variable numerateur ou denominateur n'a pas été définie.")
    except AttributeError:
        print("Une référence ou une assignation d'attribut a échoué")
    except SyntaxError:
        print("Levée lorsque l'analyseur syntaxique rencontre une erreur de syntaxe.")
    except IOError:
        print("Levée lorsqu'une fonction système retourne une erreur liée au système, incluant les erreurs entrées-sorties telles que fichier non trouvé ou disque plein")
    except ImportError:
        print("Levée lorsque l'instruction import a des problèmes pour essayer de charger un module. Également levée lorsque Python ne trouve pas un nom dans from ... import.")
    except IndentationError:
        print("Erreur de syntaxe liées à une indentation incorrecte.")
    except TypeError:
        print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
    except ZeroDivisionError:
        print("La variable denominateur est égale à 0.")
    

# on crée un objet config parser et on lit le fichier parametrage.ini
config = ConfigParser()  
config.read('parametrage.ini')

# récupération de tous les paramètres de chacune des sections
# la méthode sections() permet de récupérer les sections du fichier de configuration sous forme d’une liste
for section in config.sections():
    NomDeLaSauvegarde = config.get(section, 'NomDeLaSauvegarde')
    CheminDuContenuASauvegarder = config.get(section, 'CheminDuContenuASauvegarder')
    RepertoireDeLaSauvegarde = config.get(section, 'RepertoireDeLaSauvegarde')
    CompressionOuCopie = config.get(section, 'CompressionOuCopie')
    Rotation = config.get(section, 'Rotation')
    Rotation_float = float(Rotation)  # convertit la variable Rotation en float
    date_jour = time.time() # récupère la date du jour
    backup()
    rotation()

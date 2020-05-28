# Script de sauvegarde de fichiers locaux, comprennant 6 paramètres modifiable dans le fichier .ini

ces paramètres sont :
- Le nom du fichier de la sauvegarde
- Le chemin du repertoire à sauvegarder
- Le repertoire de destination de la sauvegarde
- Le mode de sauvegarde (en compression ou en copie)
- Et la rotation de la sauvegarde

Développé avec python en version 3.7.6

Ce script permet de sauvegarder facilement ses fichiers ou répertoires.
Il est entièrement paramétrable via le fichier paramétrage.ini et permet de faire plusieurs sauvegardes en simultané.

Le fichier paramétrage.ini se compose d'autant de section que l'on veut de sauvegarde.
Le nom de la sauvegarde doit être unique et différent de chacune des sections.
Le chemin du répertoire à sauvegarder est le chemin absolu du répertoire que l'on souhaite sauvegarder que ce soit sur Linux ou sur Windows.
Le répertoire de destination de la sauvegarde est également sous sa forme absolue.
Le script prend 2 modes soit en compression, au format gz, décompressible sous Windows avec l'utilitaire 7zip et en natif sous Linux, soit en copie ou le répertoire est intégralement recopié à l'endroit voulu.
Le dernier paramètre est la rotation de la sauvegarde et permet de stocker autant de sauvegarde que voulut.
La quatrième sauvegarde effectué efface la plus ancienne.

Le script peut être lancé soit de façon manuelle via le fichier Backup.py soit en tâche cron sur Linux ou par le planificateur de taches de Windows.

# Script de sauvegarde de fichiers locaux, comprennant 6 paramètres modifiable dans le fichier .ini

ces paramètres sont :
- Le nom du fichier de la sauvegarde
- Le chemin du repertoire à sauvegarder
- Le repertoire de destination de la sauvegarde
- Le mode de sauvegarde (en compression ou en copie)
- Et la rotation de la sauvegarde

Développé avec python en version 3.7.6

Ce script permet de sauvegarder facilement ses fichiers ou répertoires.
Il est entièrement paramétrable via un fichier paramétrage.ini et permet de faire plusieurs sauvegardes en simultané.

## Exemple de fichier ini:

[parametre]  
NomDeLaSauvegarde : Sauvegarde1  
CheminDuContenuASauvegarder : /chemin/du/repertoire/à/sauvegarder  
RepertoireDeLaSauvegarde : /repertoire/final/de/la/sauvegarde1  
CompressionOuCopie : Compression  
Rotation : 2  

[parametre-2]  
NomDeLaSauvegarde : Sauvegarde2  
CheminDuContenuASauvegarder : /chemin/vers/le/deuxieme/repertoire/à/sauvegarder  
RepertoireDeLaSauvegarde : /repertoire/final/de/la/sauvegarde2  
CompressionOuCopie : Copie  
Rotation : 3  

Le fichier paramétrage.ini se compose d'autant de section que l'on veut de sauvegarde.

__Le nom de la sauvegarde__ doit être unique et différent de chacune des sections.
__Le chemin du répertoire à sauvegarder__ est le chemin absolu du répertoire que l'on souhaite sauvegarder que ce soit sur Linux ou sur Windows.
__Le répertoire de destination de la sauvegarde__ est également sous sa forme absolue.
Le script prend __2 modes__ soit en compression, au format gz, décompressible sous Windows avec l'utilitaire 7zip et en natif sous Linux, soit en copie ou le répertoire est intégralement recopié à l'endroit voulu.
Le dernier paramètre est __la rotation de la sauvegarde__ et permet de stocker autant de sauvegarde que voulut.
La quatrième sauvegarde effectué efface la plus ancienne.

Le script peut être lancé soit de façon manuelle via le fichier Backup.py soit en tâche cron sur Linux ou par le planificateur de taches de Windows.

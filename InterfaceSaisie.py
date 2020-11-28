#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog, Toplevel
#import os

def NomSauvegarde():
    VarNomSauvegarde = save_entry.get()
    return save_entry

def AffichageBoiteSource():
    path_source = filedialog.askdirectory()
    path_select_source.config(text=path_source)
    return path_source

def AffichageBoiteDest():
    path_dest = filedialog.askdirectory()
    path_select_dest.config(text=path_dest)
    return path_dest

def LanceLaSauvegarde():
    empty = ""
    print(save_entry)
    print(path_source)
    print(path_dest)
    if save_entry == empty:
        window_entry_empty = Toplevel(window)

        window_entry_empty.title("Champs nom de la sauvegarde")

        texte = Label(window_entry_empty, text="A midi j'ai mangé de la moutarde")
        texte.pack()

    #cmd = os.path.join(os.getcwd(), "Backup.py")
    #os.system('{} {}'.format('python3', cmd))

# Création de la fenetre principale
window = Tk()

# personnalisation de la fenetre
window.title("BackUp")
window.geometry("800x400")
window.minsize(800, 400)
window.config(background='#4065A4')

# frame principale
frame = Frame(window, bg='#4065A4')

# affichage d'une image
width = 100
height = 100
image = PhotoImage(file="BackUp.png").zoom(5).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=N)

#################

# Création d'une sous boite
left_frame = Frame(frame, bg='#4065A4')

# Champs nom de la sauvegarde
save_title = Label(left_frame, text="Nom de la sauvegarde :", font=("Helvetica", 12), bg='#4065A4', fg='white')
save_title.grid(row=0, column=0, sticky=W)

# Champs "entrée" du nom de la sauvegarde
save_entry = Entry(left_frame, font=("Helvetica", 12), bg='#4065A4', fg='white', highlightthickness=0)
save_entry.grid(row=1, column=0, sticky=W)

#################

# Création d'une deuxième sous boite
middle_frame = Frame(left_frame, bg='#4065A4')

# Titre du champs "Chemin du repertoire source à sauvegarder"
path_title_source = Label(middle_frame, text="Selectionnez un repertoire à sauvegarder :", font=("Helvetica", 12), bg='#4065A4',
                   fg='white')
path_title_source.grid(row=0, column=0, sticky=W)

# Selection du repertoire
path_button_source = Button(middle_frame, text="Selectionner", font=("Helvetica", 12), bg='#4065A4', fg='white',
                     highlightthickness=0, command=AffichageBoiteSource)
path_button_source.grid(row=0, column=1, sticky=W)

# Affichage de la selection
path_select_source = Label(middle_frame, text="", font=("Helvetica", 12), bg='#4065A4', fg='white')
path_select_source.grid(row=1, column=0, sticky=W)

#################

# Titre du champs "Chemin du repertoire de destination à sauvegarder"
path_title_dest = Label(middle_frame, text="Selectionnez un repertoire de destination :", font=("Helvetica", 12), bg='#4065A4',
                   fg='white')
path_title_dest.grid(row=2, column=0, sticky=W)

# Selection du repertoire
path_button_dest = Button(middle_frame, text="Selectionner", font=("Helvetica", 12), bg='#4065A4', fg='white',
                     highlightthickness=0, command=AffichageBoiteDest)
path_button_dest.grid(row=2, column=1, sticky=W)

# Affichage de la selection
path_select_dest = Label(middle_frame, text="", font=("Helvetica", 12), bg='#4065A4', fg='white')
path_select_dest.grid(row=3, column=0, sticky=W)

#################

# Titre du champs "compression ou copie"
compress_copie_title = Label(left_frame, text="Souhaitez-vous compresser la sauvegarde dans le répertoire de destination ou \n seulement le copier :", font=("Helvetica", 12), bg='#4065A4',
                   fg='white')
compress_copie_title.grid(row=3, column=0, sticky=W)

# Selection du mode de sauvegarde
compress_copie_select = IntVar()

rdioOne = Radiobutton(left_frame, text='Compression',
                         variable=compress_copie_select, value=1, bg='#4065A4', fg='black', activebackground='#4065A4', activeforeground='white', bd=0, highlightthickness=0)
rdioTwo = Radiobutton(left_frame, text='Copie',
                         variable=compress_copie_select, value=2, bg='#4065A4', fg='black', activebackground='#4065A4', activeforeground='white', bd=0, highlightthickness=0)

rdioOne.grid(row=4, column=0, sticky=W)
rdioTwo.grid(row=5, column=0, sticky=W)

#################

# texte explicatif de la partie choix de la rotation
rotation_title = Label(left_frame, text='Veuillez selectionner la rotation du nombre de sauvegarde :', font=("Helvetica", 12), bg='#4065A4',
                   fg='white')
rotation_title.grid(row=6, column=0, sticky=W)

# Partie création d'un menu déroulant pour le choix de la rotation
# definition des parametres du widget OptionMenu
option_list = (1,2,3,4,5)
rotation = IntVar()
rotation.set(option_list[0])

rotation_menu = OptionMenu(left_frame, rotation, *option_list)
rotation_menu.config(font=("Helvetica", 12))
rotation_menu.grid(row=7, column=0, sticky=W)

#################

# bouton permettant l'envoi des données vers le fichier de traitement backup.py
execution = Button(left_frame, text="Executer la sauvegarde", font=("Helvetica", 12), bg='#4065A4', fg='white',
                     highlightthickness=0, command=LanceLaSauvegarde)
execution.grid(row=8, column=1, sticky=W)

#################

# Placement des sous boite par rapport à la frame principale
left_frame.grid(row=0, column=1, sticky=W)
middle_frame.grid(row=2, column=0, sticky=W)
#right_frame.grid(row=0, column=2, sticky=W)

# affichage de la frame
frame.pack(expand=YES)

# Affichage de la fenetre
window.mainloop()

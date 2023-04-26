# Programa en Python que renombra archivos de un directorio.
# El programa remplaza automáticamente los nombres de los archivos por una variante/nombre aleatoria.
# Programado por Eric V. Gramunt.

import os
import uuid
import tkinter as tk


class FileRenamerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Renamer Program by Eric V.")
        master.geometry("400x300")

        # Create a label widget to display the description
        self.desc_label = tk.Label(master,
                                   text="This program renames files in the current directory.\nNew names will be random UUIDs with original file extensions.")
        self.desc_label.pack(pady=10)

        # Create a button widget to start the file renaming
        self.rename_button = tk.Button(master, text="Start Rename", command=self.rename_files)
        self.rename_button.pack(pady=10)

        # Create an exit button widget to close the program
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(pady=10)

    def rename_files(self):
        folder_path = os.getcwd()
        for filename in os.listdir(folder_path):
            if os.path.isfile(filename) and filename != os.path.basename(__file__) and not filename.endswith('.exe'):
                file_extension = os.path.splitext(filename)[1]
                new_file_name = str(uuid.uuid4()) + file_extension
                os.rename(filename, os.path.join(folder_path, new_file_name))


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = FileRenamerGUI(root)
    root.mainloop()




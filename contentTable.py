from tkinter import messagebox
import customtkinter as ctk
from passwordManager import PasswordManager
from PIL import Image
from compilationForm import compilationForm


editIcon = ctk.CTkImage(light_image=Image.open("./data/icons/edit.png"))
deleteIcon = ctk.CTkImage(light_image=Image.open("./data/icons/delete.png"))
copyIcon = ctk.CTkImage(light_image=Image.open("./data/icons/copy.png"))
checkIcon = ctk.CTkImage(light_image= Image.open("./data/icons/check-mark.png"))


def refresh_table(App, password_manager, data, table_frame):
    global app 
    global passwordManager
    app = App
    passwordManager = password_manager
    for widget in table_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(table_frame, text="Domain",
            font=("Arial", 20, "bold"),
            anchor="w").grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    table_frame.grid_columnconfigure(0, weight=1)
    ctk.CTkLabel(table_frame, text="Username",
            font=("Arial", 20, "bold"),
            anchor="w").grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    table_frame.grid_columnconfigure(1, weight=1)  
    ctk.CTkLabel(table_frame, text="Password",
            font=("Arial", 20, "bold"),
            anchor="w").grid(row=0, column=2, padx=5, pady=5, sticky="ew")
    table_frame.grid_columnconfigure(2, weight=1)
    ctk.CTkLabel(table_frame, text="Ultima modifica",
            font=("Arial", 20, "bold"),
            anchor="w").grid(row=0, column=4, padx=5, pady=5, sticky="ew")
    table_frame.grid_columnconfigure(4, weight=1)

    for i, item in enumerate(data):
        ctk.CTkLabel(table_frame, text=item["domain"], anchor="w").grid(row=i+1, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkLabel(table_frame, text=item["username"], anchor="w").grid(row=i+1, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkLabel(table_frame, text=item["password"], anchor="w").grid(row=i+1, column=2, padx=5, pady=5, sticky="ew")
        ctk.CTkLabel(table_frame, text=item["timestamp"], anchor="w").grid(row=i+1, column=4, padx=5, pady=5, sticky="ew")

        copy_btn = ctk.CTkButton(table_frame, image=copyIcon, text="", width=50)
        copy_btn.configure(command=make_copyBtn(i, copy_btn))
        copy_btn.grid(row=i+1, column=3, padx=5)

        edit_btn = ctk.CTkButton(table_frame, image=editIcon, text="", width=50, command=lambda idx=i, tf=table_frame: edit_entry(idx, tf))
        edit_btn.grid(row=i+1, column=5, padx=5)

        delete_btn = ctk.CTkButton(table_frame, image=deleteIcon, text="", width=50, command=lambda idx=i, tf=table_frame: delete_entry(idx, tf))
        delete_btn.grid(row=i+1, column=6, padx=5)

def make_copyBtn(index, btn):
    return lambda: copy_entry(index, btn)

def copy_entry(index, btn):
    app.clipboard_clear()            
    app.clipboard_append(passwordManager.getCredentials(index)["password"])  
    app.update()

    btn.configure(image=checkIcon)
    app.after(2000, lambda: btn.configure(image=copyIcon))

def edit_entry(index, tf):
    compilationForm(app, passwordManager, False, index, tf)

def delete_entry(index, tf):
    if messagebox.askyesno("Conferma", "Eliminare definitivamente questo elemento?"):
        passwordManager.removeCredentials(index)
        data = passwordManager.getData()
        refresh_table(app, passwordManager, data, tf)

from tkinter import messagebox
import customtkinter as ctk
from passwordGenerator import password_generator
from PIL import Image
from passwordManager import PasswordManager


copyIcon = ctk.CTkImage(light_image=Image.open("./data/icons/copy.png"))
checkIcon = ctk.CTkImage(light_image= Image.open("./data/icons/check-mark.png"))


def compilationForm(app, passwordManager, adder, index, tf):

    add_win = ctk.CTkToplevel(app)
    add_win.geometry("400x500")
    if adder:
        
        add_win.title("Aggiungi Nuove Credenziali")
        domain = ""
        username = ""
        password = ""
    else:
        
        add_win.title("Modifica Credenziali")
        oldCredentials = passwordManager.getCredentials(index)
        domain = oldCredentials["domain"]
        username = oldCredentials["username"]
        password = oldCredentials["password"]

    
    add_win.update()
    add_win.grab_set() 

    ctk.CTkLabel(add_win, text="Dominio:").pack(pady=(20,5))
    domain_entry = ctk.CTkEntry(add_win, width=300)
    domain_entry.pack()
    domain_entry.insert(0, domain)
    if not adder:
        domain_entry.configure(state="readonly")

    ctk.CTkLabel(add_win, text="Username:").pack(pady=(20,5))
    username_entry = ctk.CTkEntry(add_win, width=300)
    username_entry.pack()
    username_entry.insert(0, username)

    ctk.CTkLabel(add_win, text="Password:").pack(pady=(20,5))
    password_entry = ctk.CTkEntry(add_win, width=300, show="*")
    password_entry.pack()
    password_entry.insert(0, password)

    suggested_pw = password_generator()
    ctk.CTkLabel(add_win, text="Password suggerita:", font=("Arial", 12, "italic")).pack(pady=(15,2))
    suggested_pw_entry = ctk.CTkEntry(add_win, width=300)
    suggested_pw_entry.pack()
    suggested_pw_entry.insert(0, suggested_pw)
    suggested_pw_entry.configure(state="readonly")

    copy_btn = ctk.CTkButton(add_win, image=copyIcon, text="", width=50)
    copy_btn.pack(pady=5)
    copy_btn.configure(command=lambda pwd=suggested_pw, btn=copy_btn: copy_suggestedpwd(app, pwd, btn))

    def save():
        domain = domain_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not domain or not username or not password:
            messagebox.showwarning("Attenzione", "Compila tutti i campi!")
            return
        if adder:
            passwordManager.addCredentials(domain, username, password)
        else:
            passwordManager.editCredentials(domain, username, password, index)
        from contentTable import refresh_table
        refresh_table(app, passwordManager, passwordManager.getData(), tf)
        add_win.destroy()
        
    save_btn = ctk.CTkButton(add_win, text="Salva", command=save)
    save_btn.pack(pady=20)


def copy_suggestedpwd(app, pwd, btn):
    app.clipboard_clear()            
    app.clipboard_append(pwd)  
    app.update()

    btn.configure(image=checkIcon)
    app.after(2000, lambda: btn.configure(image=copyIcon))
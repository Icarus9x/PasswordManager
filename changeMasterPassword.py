from tkinter import messagebox
import customtkinter as ctk
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA3_256
from passwordManager import PasswordManager

saltAuthn = bytes.fromhex("fd7ee76617164c2c9d49b245e7430816")

def changeMasterPwd(app, passwordManager, authnHash):
    ah = authnHash
    new_master = ctk.CTkToplevel(app)
    new_master.geometry("400x500")
    new_master.title("Modifica master password")
    new_master.update()
    new_master.grab_set()

    ctk.CTkLabel(new_master, text="Vecchia password").pack(pady=(20,5))
    oldpassword_entry = ctk.CTkEntry(new_master, width=300, show="*")
    oldpassword_entry.pack()

    ctk.CTkLabel(new_master, text="Nuova password").pack(pady=(20,5))
    newpassword_entry = ctk.CTkEntry(new_master, width=300, show="*")
    newpassword_entry.pack()

    ctk.CTkLabel(new_master, text="Conferma la nuova password").pack(pady=(20,5))
    confirmpassword_entry = ctk.CTkEntry(new_master, width=300, show="*")
    confirmpassword_entry.pack()


    
    def save():
        if PBKDF2(oldpassword_entry.get(), saltAuthn, 16, count=1000, hmac_hash_module=SHA3_256) != ah:
            messagebox.showwarning("Attenzione", "La vecchia password è errata!")
            return 
        if len(newpassword_entry.get())<8:
            messagebox.showwarning("Attenzione", "La password deve avere almeno 8 caratteri")
            return
        if newpassword_entry.get().isalnum():
            messagebox.showwarning("Attenzione", "La password deve contenere almeno un carattere speciale")
            return
        if confirmpassword_entry.get() != newpassword_entry.get():
            messagebox.showwarning("Attenzione", "Le password non coincidono!")
            return
        if oldpassword_entry.get() == newpassword_entry.get():
            messagebox.showwarning("Attenzione", "La nuova password deve essere diversa dalla vecchia")
            return 

        passwordManager.changeMasterPassword(newpassword_entry.get())
        
        authnHash= PBKDF2(newpassword_entry.get(), saltAuthn, 16, 1000, hmac_hash_module=SHA3_256)
        with open("./data/authnHash", "w") as file:
            file.write(authnHash.hex())

        new_master.destroy()

    save_btn = ctk.CTkButton(new_master, text="Salva", command=save)
    save_btn.pack(pady=20)


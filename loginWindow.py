  
from tkinter import messagebox
import customtkinter as ctk
from passwordManager import PasswordManager
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA3_256
from PIL import Image
from mainWindow import open_main_window
from setWindowIcon import set_window_icon


saltAuthn = bytes.fromhex("fd7ee76617164c2c9d49b245e7430816")


def login_window(authnHash, app):
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app.title("Accesso")
    app.geometry("600x400")
    set_window_icon(app)

    label = ctk.CTkLabel(app, text="Inserisci la master password:", font=("Arial", 22))
    label.pack(pady=20)

    password_entry = ctk.CTkEntry(app, placeholder_text="Password", show="*", font=("Arial", 22))
    password_entry.pack(pady=10)

    def authenticate():
        password = password_entry.get()
        loginHash = PBKDF2(password, saltAuthn, 16, count=1000, hmac_hash_module=SHA3_256)
        if loginHash == authnHash:
            app.destroy()
            open_main_window(PasswordManager(password), authnHash)
        else:
            messagebox.showerror("Errore", "Password errata!")

    login_button = ctk.CTkButton(app, text="Login", command=authenticate, font=("Arial", 22))
    login_button.pack(pady=10)

    
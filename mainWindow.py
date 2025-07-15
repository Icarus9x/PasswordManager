import customtkinter as ctk
from PIL import Image
from setWindowIcon import set_window_icon, resource_path
from compilationForm import compilationForm
from contentTable import refresh_table
from changeMasterPassword import changeMasterPwd

saltAuthn = bytes.fromhex("fd7ee76617164c2c9d49b245e7430816")


def open_main_window(passwordManager, authnHash):
    app = ctk.CTk()
    app.title("Password Manager")
    app.geometry("900x600")
    set_window_icon(app)
    app.grid_rowconfigure(1, weight=1)   
    app.grid_columnconfigure(0, weight=1)  

    

    backIcon = ctk.CTkImage(light_image=Image.open(resource_path("./data/icons/return.png")))
    plusIcon = ctk.CTkImage(light_image=Image.open(resource_path("./data/icons/add.png")))
    lockIcon = ctk.CTkImage(light_image=Image.open(resource_path("./data/icons/lock.png")))
    

    def reset_dashboard():
        refresh_table(app, passwordManager, passwordManager.getData(), table_frame)

    def search_by_domain():
        refresh_table(app, passwordManager,passwordManager.getCredentialsByDomain(domain_search.get()), table_frame)

    def search_by_username():
        refresh_table(app, passwordManager,passwordManager.getCredentialsByUsername(user_search.get()), table_frame)

    
    def add_entry():
        compilationForm(app, passwordManager, True, -1, table_frame)
    

    # --- NAV BAR ---
    nav_frame = ctk.CTkFrame(app)
    nav_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

    domain_search = ctk.CTkEntry(nav_frame, placeholder_text="Cerca per dominio", width=200)
    domain_search.grid(row=0, column=0, padx=5)
    ctk.CTkButton(nav_frame, text="Cerca", command=search_by_domain).grid(row=0, column=1, padx=5)

    user_search = ctk.CTkEntry(nav_frame, placeholder_text="Cerca per username", width=200)
    user_search.grid(row=0, column=2, padx=5)
    ctk.CTkButton(nav_frame, text="Cerca", command=search_by_username).grid(row=0, column=3, padx=5)

    add_button = ctk.CTkButton(nav_frame, image=plusIcon, text="", width=40, command=add_entry)
    add_button.grid(row=0, column=4, padx=5)

    back_button = ctk.CTkButton(nav_frame, image=backIcon, text="", width=40, command=reset_dashboard)
    back_button.grid(row=0, column=5, padx=5)

    change_pwd_btn = ctk.CTkButton(nav_frame, image=lockIcon, text="", width=40, command= lambda app=app, pm=passwordManager, authnHash=authnHash: changeMasterPwd(app, pm, authnHash))
    change_pwd_btn.grid(row=0, column=6, padx=5)

    # --- TABELLA ---
    table_frame = ctk.CTkFrame(app)
    table_frame.grid(row=1, column=0, sticky="nwe", padx=20, pady=10)  # sticky "nwe": nord + ovest + est

    refresh_table(app, passwordManager, passwordManager.getData(), table_frame)

    app.mainloop()
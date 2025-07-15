import loginWindow as lw
import passwordGenerator
import passwordManager
import mainWindow
import setWindowIcon
import changeMasterPassword
import compilationForm
import contentTable
import customtkinter as ctk


if __name__ == '__main__':
    with open("./data/authnHash", "r") as file:
        authnHash = file.read()
    app = ctk.CTk()
    authnHash = bytes.fromhex(authnHash)
    lw.login_window(authnHash, app)
    app.mainloop()
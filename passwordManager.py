from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA3_256
from Crypto.Util.Padding import pad, unpad
import json
from datetime import date

class PasswordManager:
    def __init__(self, masterPWD):
        self.iv = bytes.fromhex('37f5993b004769929e66b14e065b495f')
        self.salt = bytes.fromhex("ebbad5117e33dafe28ae991979e94282")
        self.key = PBKDF2(masterPWD, self.salt, 16, count=10000, hmac_hash_module=SHA3_256)

    
    def changeMasterPassword(self, newPassword):
        try:
            data = self.getData()
            self.key = PBKDF2(newPassword, self.salt, 16, count=10000, hmac_hash_module=SHA3_256)
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)

            data = json.dumps(data)
            
            ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))

            with open("./data/passwords", "wb") as file:
                file.write(ciphertext)
            return True
        except (ValueError, json.JSONDecodeError) as e:
            print("Errore durante la cifrazione:", e)
            return False
        

    def getData(self):

        try:
            decipher = AES.new(self.key, AES.MODE_CBC, self.iv)

            with open("./data/passwords", "rb") as file:
                ciphertext = file.read()

            decipherText = decipher.decrypt(ciphertext)

            decipherText = unpad(decipherText, AES.block_size)

            decipherText = json.loads(decipherText.decode())
            return decipherText
        except (ValueError, json.JSONDecodeError) as e:
            print("Errore durante la decifrazione:", e)
            return []
    
    def updateData(self, data):

        data = json.dumps(data)
        data = pad(data.encode(), AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        ciphertext = cipher.encrypt(data)
        with open("./data/passwords", "wb") as file:
            file.write(ciphertext)

    def getCredentialsByDomain(self, domain):
        data = self.getData()
        search = "".join(char for char in domain.lower().strip() if char.isalnum())
        results = [item for item in data 
                   if item["domain"].lower().strip() == search]
        return results
    
    def getCredentialsByUsername(self, username):
        data = self.getData()
        search = "".join(char for char in username.lower().strip() if char.isalnum())
        results = [item for item in data if "".join(char for char in item["username"].lower().strip() if char.isalnum()) == search]
        return results
    
    def getCredentials(self, index):
        data = self.getData()
        return data[index]

    def addCredentials(self, domain, username, password):
        data = self.getData()
        data.append({"domain" : domain, "username" : username, "password" : password, "timestamp" : date.today().strftime("%d-%m-%Y")})
        self.updateData(data)

    def editCredentials(self, domain, username, password, index):
        self.removeCredentials(index)
        self.addCredentials(domain, username, password)

    def removeCredentials(self, index):
        data  = self.getData()
        data.pop(index)
        self.updateData(data)
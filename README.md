# Password Manager
#### This is a user-friendly desktop python application that works on both Windows and Linux. The main purpose here is to keep an encrypted json file, so that the user doesn't need to remember all of theme.
#### In order to run use the command on the console: `python main.py`
### Services:
- Passwords accessible just by recalling the master password
  - ### Default master password: Geppetto2009!
  - Master password is changable by clicking the lock icon on the top right of the window
    
- The password for each domain can be modified and removed clicking the icons on the right
  - When the user is editing the password, they can't change the domain, but can update the username
  - When the password isn't updated for more than 6 months the date of the last update will turn red, in order to strongly suggest the user to change it
  - Random samples are kept there as an example, they can be easily removed
    
-  A new password (and username) for a new domain can be added by click the plus button
  
-  When adding or modifying a password a new window will open where a cryptographically secure randomly generated password will appear. It is strongly suggested to copy and paste that password instead of just coming up with one due to dictionary attacks, but the user here is free to choose
  
-  There are also two types of search bars, both working, one by domain, and one by username

### Notes:
- The GUI is made with Custom Tkinter
- The application is fully in Italian

# On the GUI: gugli, rafa, gabi
# # On the backend: joe, rodrigo, jose
import socket
import threading
from Login_form import Login_form
from Dickscord import Dickscord

# Instanciate the Login form object for the GUI
LoginForm = Login_form()
LoginForm.run()

# Port to connect to server
PORT = 8080  # The port used by the server

s = socket.socket()
s.connect((LoginForm.HOST, PORT))

# Send User and password to the server
msg = LoginForm.username +' '+ LoginForm.password
s.send(msg.encode())

# If connection accepted, deploy Message GUI
dickscord = Dickscord(s,LoginForm.username)


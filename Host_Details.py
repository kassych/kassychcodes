#kasscode
#extracting different values from Host
import socket
from getpass import getuser
from os import uname
# getting operating system
print (uname().nodename, uname().release)
# getting the interfaces available
print (socket.gethostbyname(str(uname().nodename)))
#getting username
print(getuser())






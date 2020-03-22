#Author: Sean Gao

import getpass

_username = "sean"
_password = "1234s"

username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")

print(username,password)

if _username == username and _password == password:
    print('''Welcome user {name} login'''.format(name = _username))
else:
    print("Invalid username or password!")

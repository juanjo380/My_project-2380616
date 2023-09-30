#My project CRUD ->
clients = 'Luis, Kevin, '

def create_client(client_name):
    global clients
    if client_name not in clients: #when the client not found
        _add_comma()
        clients += client_name
    else:
         print("Clent already exists {}:".format(client_name))

def _add_comma():
    global clients
    clients +=", "

def read_client():
    global clients
    pass
def update_client():
    global clients
    pass
def delete_client():
    global clients
    pass


def _print_welcome():
    print("WELCOME TO UNIVERSIDAD DEL VALLE - TULUA")
    print('*' * 100)
    print("What would you like to do today:")
    print("[C]reate client or user")
    print("[R]ead client or user")
    print("[U]pdate client or user")
    print("[D]elete client or user")

def _get_client_name(): #la funcion permite preguntar por el nombre del cliente
    return input("Type your name client:")

def _get_list_client_names():
     global clients
     print(clients)

if __name__ == '__main__':
    _print_welcome()
    option = input("Type otpion desired: ").upper()

    if option == "C":
        client_name = _get_client_name()
        create_client(client_name)
        _get_list_client_names

    elif option == 'R':
           client_name = _get_client_name
           _get_list_client_names
    
    elif option == 'U':
            client_name = _get_client_name
            _get_list_client_names

    elif option == 'D':
            client_name = _get_client_name
            _get_list_client_names
    else:
          print("Invalid command")
    
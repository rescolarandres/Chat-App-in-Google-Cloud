
import socket
import threading


def new_client(conn,addr,clients):
    # Function that threats new clients connections
    # Inputs:
    # conn : connection object from the socket
    # addr: address of the connectec client
    # clients: list with the current clients active
    #--------------------------------------

    # User and password settings are received from the client
    data = conn.recv(1024).decode()
    user = data.split()[0]
    passw = data.split()[1]

    if passw == 'chatappdis':
            
        print(f'Accepted connection from {user}:{addr}')
        # Send a message to the group with the new user
        for client in clients:
             client.send((f'{user} joined to the room...').encode())


        while True:
                # receive a message from the client with data set to max of 1024 bytes
                message = conn.recv(1024)

                #display received message with corresponding client address
                print(f'Received message from {user}: {message.decode()}')

                # The client exits the server when typing: 'exit'
                if message.decode().lower() == "exit":
                    # Remove the client from the list of active clients
                    clients.remove(conn)
                    break


                for client in clients:
                    # Send the message received to all the active clients in the server
                    response = f'{user}: {message.decode()}'.encode()
                    client.send(response)
    
    # print a message to indicate that the client has disconnected
    print(f'Connection from {addr} closed')

    # close the client socket
    conn.close()


HOST = '127.0.0.1'
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)
# Instanciate the socket object
ServerSocket = socket.socket()

ServerSocket.bind((HOST, PORT))
# Open the socket to listen action
ServerSocket.listen()

# Data to manage connections
thread_count = 0    # Counter of clients
clients = []    # List to store the clients active

while True:
        conn, addr = ServerSocket.accept()
        # Store connections and addresses in a dictionary
        clients.append(conn)

        # Open a new thread for each connection, instanciating the new_client function
        client_thread = threading.Thread(target = new_client, args=(conn, addr, clients))
        client_thread.start()
        
        


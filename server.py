import socket
from threading import Thread
ip_address="127.0.0.1"
port=8000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("What is server:  ",server)

server.bind((ip_address,port))
server.listen()

nicknames=[]
list_clients=[]

print("server has started.....")

def clinetthread(conn, clientname):
    conn.send("Welcome to this chatroom!".encode("utf-8"))
    while True:
        try:
            message=conn.recv(2048).decode("utf-8")
            print(message)
            if message:
                message_to_send="<"+addr[0]+"<"+message
                print(message_to_send)
            else:
                remove(conn)
                removenickname(clientname)

        except:
            continue

def remove(conn):
    if conn in list_clients:
        list_clients.remove(conn)

def removenickname(clientname):
    if clientname in nicknames:
        nicknames.remove(clientname)


def broadCast(msg,conn):
    for i in list_clients:
        if i!= conn:
            try:
                i.send(msg.encode("utf-8"))

            except: 
                remove(i)
while True: 
    conn,addr=server.accept()

    # Fernandez is data sending from server to client
    conn.send("Fernandez".encode("utf-8"))

    # nickname is data recived(decode) by server from client
    clientname=conn.recv(2048).decode("utf-8")

    # adding all the client connection to list_client
    list_clients.append(conn)

    # adding all nickname(client name ) to nickname list
    nicknames.append(clientname)

    message="{} joined!".format(clientname)
    print(message)
    print("what is conn: ",conn)
    print("what is addr: ",addr)
    print(addr[0]+"connected")
    broadCast(message, conn)

    new_thread=Thread(target=clinetthread,args=(conn, clientname))
    new_thread.start()
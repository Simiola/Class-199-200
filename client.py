import socket
from threading import Thread

nickname= input("Enter the nickname(client name: )")
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000

client.connect((ip_address,port))
print("Connected with the server:  ")

# using the below recive we are adding instructions what is msg we are reciving from the server
def recive():
    while True:
        try:
            message=client.recv(2048).decode("utf-8")
            print("what is message:  ",message)
            if message == "Fernandez":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
                continue
def write():
    while True:
        writemessage='{} {}'.format(nickname,input(''))
        client.send(writemessage.encode("utf-8"))



recive_thread= Thread(target=recive)
recive_thread.start()

write_thread=Thread(target=write)
write_thread.start()
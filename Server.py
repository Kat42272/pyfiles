import socket

host = 'localhost'
port = 8080

# socket.SOCK_STREAM for TCP connection, socket.SOCK_DGRAM for UDP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

sock.listen(1)
print("The Server is running and is listening to client request.")
conn, address = sock.accept()

message = "Hey, there is something important for you."
conn.send(message.encode())

conn.close()

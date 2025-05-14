import socket
s = socket.socket()
host = socket.gethostname()
port = 123
s.bind((host, port))
s.listen(3)
while True:
    connection, address = s.accept()
    # Take the message as input
    message = bytes(input('Enter your message: '), 'utf-8')
    # Send the message
    connection.send(message)
    print('Message sent!')
    # Receive the message
    message = str(connection.recv(1024), 'utf-8')
    print('Message received:', message)
    # Close the connection
    connection.close()
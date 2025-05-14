import socket
s = socket.socket()
host = socket.gethostname()
port = 123
s.connect((host, port))
# Receive the message
message = str(s.recv(1024), 'utf-8')
print('Message received:', message)
# Take the message as input
message = bytes(input('Enter your message: '), 'utf-8')
# Send the message
s.send(message)
print('Message sent!')
s.close()
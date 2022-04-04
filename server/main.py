import socket

# create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket listen
server_socket.bind(('localhost', 8080))
server_socket.listen(5)
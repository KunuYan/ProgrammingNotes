import sys
import socket
HOST, PORT = "localhost", 8080 # adress of the server

# we are just sending a string to the server, it would upper our strin and return it
data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# always use errors handling with your connection atttempts
try:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8")) # we encode our data
    received = str(sock.recv(1024), "utf-8") # we receive encoded data, so str it
finally:
    sock.close() # close socket once you do what was needed

print("Sent:{}".format(data))
print("Received: {}".format(received))

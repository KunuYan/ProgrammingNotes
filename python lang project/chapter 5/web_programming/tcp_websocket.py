# Transmission Control Protocal(TCP)/ Internet Protocol(IP)
# it a layer even lower than http and xml, it how data are transfert on the internet
# does not work on browser, (you know when u imagine those 1 & 0 travelling inside the tubes)
import socketserver
# a socketserver is a server that can accept socket connection
# basically the socket has to connect with the server each time to send request
# The soketserver waits for a connection request from client seckets, if a request is acepted,
# it creates a socket on the server for the client to connect to



# This class is initialize for each connection (keep in my the client don't connect forever, they request connection, do whatever and end connection)
class TCPHandler(socketserver.BaseRequestHandler):
    # we overide the default method, so that it does what we want
    # it runs automatically each time a connection is made
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data but upper case
        self.request.sendall(self.data.upper())


if __name__=='__main__':
    HOST, PORT = "localhost", 8080


# serve our server
server = socketserver.TCPServer((HOST, PORT), TCPHandler)
server.serve_forever()

# check tcp_client.py to see how a client code for a tcp server should look like
# some librabaries for networking with python: Twisted Tornado gevent
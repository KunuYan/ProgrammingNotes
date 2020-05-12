# XML‐Remote Procedure Call (XML‐RPC) is an older technology that some legacy system still use
# This is how data was once processed across the Internet, using XML. We now use JSON
# xml-rpc is basically requests and httpserver, but reads xml instead
from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 8080))

def square(n):
    return n * n
    print("We've got a connection and are listening on port 8080...huzzah!")

server.register_function(square, "square")

server.serve_forever()

# once you start this process you can have a client connect to the server vient a proxy
# client code would look like this
'''
import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8080")
print("the square of 3 is %s" % proxy.square(3))
the square of 3 is 9

'''
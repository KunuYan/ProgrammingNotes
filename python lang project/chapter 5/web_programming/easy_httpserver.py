import socketserver, http.server


PORT = 8080

# set up a request handler
Handsy = http.server.SimpleHTTPRequestHandler

# set up my http deamon
httpd = socketserver.TCPServer(("", PORT), Handsy)


# now serve your the directory to the correct port so that it can be access in the browser
httpd.serve_forever()

# you can even spin up a quick http server with a simple python command
# goto the directory you want and type the command below with whatever port you choose
# python ‐m http.server 8000
# http module also has a http.client if you want to establish a proxy connection
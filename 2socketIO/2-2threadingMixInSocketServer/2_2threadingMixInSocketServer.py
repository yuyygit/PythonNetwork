# encoding: utf-8
import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0 #tell the kernel to pickup a port fynamyically
BUF_SIZE = 1024

def client(ip, port, message):
    '''A client to test threadingMixIn server'''
    #Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE)
        print "Client receive: %s" % response
    finally:
        sock.close()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    '''A example of threaded TCP request handler'''
    def handle(self):
        data = self.request.recv(1024)
        current_thread = threading.current_thread()
        response = "%s: %s" % (current_thread.name, data)
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """Nothing to add here, inherited everything necessary from parents"""
    pass

if __name__ == '__main__':
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address #retrieve ip address

    #Start a thread with the server -- one thread per request
    server_thread = threading.Thread(target= server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running on thread: %s" % server_thread.name

    #Run clinets
    client(ip, port, "Hello from Client 1")
    client(ip, port, "Hello from Client 2")
    client(ip, port, "Hello from Client 3")
    server.shutdown()
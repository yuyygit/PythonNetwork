# encoding: utf-8
import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0 #tells the kernel to pick a pot dynaically
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server'

class ForkingClient():
    '''A client to test forking server'''
    def __init__(self, ip, port):
        #Create a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server
        self.sock.connect((ip, port))
    def run(self):
        '''Client playing with the server'''
        currentProcessid = os.getpid()
        print 'PID %s Client Sending echo message to the server: "%s" ' % (currentProcessid, ECHO_MSG)
        sentDatalength = self.sock.send(ECHO_MSG)
        print "Sent: Client %d characters so far ..." % sentDatalength

        #Display server response
        response = self.sock.recv(BUF_SIZE)
        print "PID Client %s received %s " % (currentProcessid, response[5:])

    def shutdown(self):
        '''clean the client socket'''
        self.sock.close()
class ForkingServerRequestHandle(SocketServer.BaseRequestHandler):
    def handle(self):
        #Send the echo back to the client
        data = self.request.recv(BUF_SIZE)
        currentProcessid = os.getpid()
        response = '%s: %s' % (currentProcessid, data)
        print "Server sending response [currentProcessid: data] = %s " \
        % response
        self.request.send(response)
        # while True:
        #     pass
        return
class ForkingServer(SocketServer.ForkingMixIn,SocketServer.TCPServer):
    """Nothing to add here inheruted everthing necessary from parents"""
    pass
def main():
    #Launch the server
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandle)
    ip, port = server.server_address #retrive the port num
    server_thread = threading.Thread(target= server.serve_forever)
    server_thread.setDaemon(True) #don't hang on exit
    server_thread.start()
    print "Server loop running PID: %s " % os.getpid()

    #Launch the client
    client1 = ForkingClient(ip, port)
    client1.run()

    client2 = ForkingClient(ip, port)
    client2.run()

    client3 = ForkingClient(ip, port)
    client3.run()

    #Clean them up
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    client3.shutdown()
    server.socket.close()
if __name__ == '__main__':
    main()
    # while True:
    #     pass
        

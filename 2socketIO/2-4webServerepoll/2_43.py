# encoding: utf-8
import socket
import select
import argparse

# SERVER_HOST = 'localhost'
# EOL1 = b'\n\n'
# EOL2 = b'\n\r\n'

SERVER_HOST='localhost'

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'

SERVER_RESPONSE = b"""HTTP/1.1 200 OK\r\n Data: Mon, 1 Apr 2013 01:01:01\
GMT\r\nContent-Type: text/plain\r\nContent-Length: 25\r\n\r\n\
Hello from Epoll server!"""
SERVER_RESPONSE2 = b"""HTTP/1.1 200 OK \r\nDate: Mon, 1 Apr 2019 01:01:01 GMT\r\nContent-Type: text/plain\r\nContent-Length: 25\r\n\r\nHello from Epoll Server"""
# class EpollServer(object):
#     """A socket server using Epoll"""
#     def __init__(self, host=SERVER_HOST, port=0):
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#         self.sock.bind((host, port))
#         self.sock.listen(1)
#         self.sock.setblocking(0)
#         self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
#         print "Start Epoll server"
#         self.epoll = select.epoll()
#         self.epoll.register(self.sock.fileno(), select.EPOLLIN)
#     def run(self):
#         """Executes epoll server operation"""
#         try:
#             connections = {}; requests = {}; responses = {}
#             while True:
#                 events = self.epoll.poll(1)
#                 for fileno, event in events:
#                     if fileno == self.sock.fileno():
#                         connection, address = self.sock.accept()
#                         connection.setblocking(0)
#                         self.epoll.register(connection.fileno(), select.EPOLLIN)
#                         connections[connection.fileno()] = connection
#                         requests[connection.fileno()] = b''
#                         responses[connection.fileno] = SERVER_RESPONSE
#
#                     elif event & select.EPOLLIN:
#                         print "read event is happing"
#                         requests[fileno] += connections[fileno].recv(1024)
#                         if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
#                             self.epoll.modify(fileno,select.EPOLLOUT)
#                             print('-'*40 + '\n' + requests[fileno].decode()[:-2])
#                         print "read finish"
#                     elif event & select.EPOLLOUT:
#                         print "server start write..."
#                         # byteswritten = connections[fileno].send(responses[fileno])
#                         # a = {}
#                         # a = connections[fileno].send(responses[fileno])
#                         byteswritten = connections[fileno].send(responses[fileno])
#                         responses[fileno]=responses[fileno][byteswritten:]
#
#                         # byteswritten = connections[fileno].send(responses[fileno])
#                         # responses[fileno] = responses[fileno][byteswritten:]
#                         if len(responses[fileno]) == 0:
#                             self.epoll.modify(fileno, 0)
#                             connections[fileno].shutdown(socket.SHUT_RDWR)
#                     elif event & select.EPOLLHUP:
#                         self.epoll.unregister(fileno)
#                         connections[fileno].close()
#                         del connections[fileno]
#         finally:
#             self.epoll.unregister(self.sock.fileno())
#             self.epoll.close()
#             self.sock.close()

class EpollServer(object):
    """ A socket server using Epoll. """

    def __init__(self,host=SERVER_HOST,port=0):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Explain the function of the above.
        self.sock.bind((host,port))
        self.sock.listen(1)
        self.sock.setblocking(0)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        # Explain the function of the above.
        print "Start Epoll Server"
        self.epoll = select.epoll()
        self.epoll.register(self.sock.fileno(),select.EPOLLIN)
        #Return the socket’s file descriptor (a small integer). This is useful with select.select().
        # epoll.register(fd[, eventmask])
        #   Register a fd descriptor with the epoll object.

    def run(self):
        """Executes epoll server operation"""
        try:
            connections = {}; requests = {}; responses = {}
            while True:
                events = self.epoll.poll(1)
                # Wait for events. timeout in seconds (float)
                for fileno,event in events:
                    if fileno == self.sock.fileno():
                        #events has the style like: events=[(3,1)].
                        #The first is the fd of socket. The second is the state of socket.
                        #self.sock.fileno() return the fd of self.sock,which is the server sock.
                        #So, blow is deal with the request for server.

                        connection, address = self.sock.accept()
                        #create a sock connection to deal with the request.

                        connection.setblocking(0)

                        #Set blocking or non-blocking mode of the socket:
                        #if flag is 0, the socket is set to non-blocking,
                        #else to blocking mode. Initially all sockets are in blocking mode.

                        self.epoll.register(connection.fileno(),select.EPOLLIN)
                        #Register a fd descriptor with the epoll object.

                        connections[connection.fileno()] = connection
                        requests[connection.fileno()]=b''
                        responses[connection.fileno()]=SERVER_RESPONSE
                        # define the connection, requests, responses.

                    elif event & select.EPOLLIN:
                        # bitwise and of x and y
                        # deal with the EPOLLIN socked.

                        requests[fileno]+=connections[fileno].recv(1024)
                        #socket wihch created above recive data.

                        if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                            # the request is from the webbrowser the
                            # change the socket to be EPOLLOUT to rsponse back.

                            self.epoll.modify(fileno,select.EPOLLOUT)
                            #change the socket state to EPOLLOUT.
                            print('_'*40 + '\n' +requests[fileno].decode()[:-2])
                    elif event & select.EPOLLOUT:
                        print "server start write..."
                        # byteswritten = connections[fileno].send(responses[fileno])
                        # a = {}
                        # a = connections[fileno].send(responses[fileno])
                        byteswritten = connections[fileno].send(responses[fileno])
                        responses[fileno]=responses[fileno][byteswritten:]

                        # byteswritten = connections[fileno].send(responses[fileno])
                        # responses[fileno] = responses[fileno][byteswritten:]
                        if len(responses[fileno]) == 0:
                            self.epoll.modify(fileno, 0)
                            connections[fileno].shutdown(socket.SHUT_RDWR)
                        print "write finish ......"
                    elif event & select.EPOLLHUP:
                        self.epoll.unregister(fileno)
                        #epoll.unregister(fd)
                        #Remove a registered file descriptor from the epoll object.
                        connections[fileno].close()
                        del connections[fileno]
        finally:
            self.epoll.unregister(self.sock.fileno())
            self.epoll.close()
            self.sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket server Example with Epoll')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    server = EpollServer(host = SERVER_HOST, port= port)
    server.run()

# encoding: utf-8

import socket
import sys

def reuseSocketAddr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Get the old state of the SO_REUSERADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "Old sock state: %s " % old_state

    #Enable the SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "New sock state: %s " % new_state

    local_port = 8282

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    server.bind(('',local_port))
    server.listen(1)
    print("Lisetning on port: %s " % local_port)
    while True:
        try:
            connection, addr = server.accept()
            print "Connected by %s ： %s " % (addr[0], addr[1] )
        except KeyboardInterrupt:
            break
        except socket.error as msg:
            print " %s " % msg
if __name__ == '__main__':
    reuseSocketAddr()


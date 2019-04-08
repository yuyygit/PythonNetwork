# encoding: utf-8
import socket
import sys
import argparse

def handleSocketError():
    # setup argument parsing
    host = ''
    port = 0
    parser = argparse.ArgumentParser(description = 'Socket Error Examples')
    parser.add_argument('--host', action= "store", dest= "host", type= str, required = False)
    parser.add_argument('--port', action= "store", dest= "port", type= int, required = False)
    parser.add_argument('--file', action= "store", dest= "file", type= str, required = False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file


    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(20)

    except socket.error, e:
        print "Error creating socket : %s " % e
        sys.exit(1)
    # Second try-except block -- connect to given host/port
    try:
        print "port type : %s \r\nhost type : %s " % (type(port), type(host))
        s.connect((str(host), port))

    except socket.gaierror, e:
        print "Connect error: %s " % e
        sys.exit(1)
    # Thrid try-except block -- waitting to receive data from remote host
    try:
        s.sendall("Get %s HTTP/1.0\r\n\r\n" % filename)
    except socket.error, e:
        print "Error sending data: %s " % e
        sys.exit(1)
    while True:
        # Fourth try-except -- waiting to receive
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print "Error receiving data: %s " % e
            sys.exit(1)
        if not len(buf):
            break
        # write the received data
        sys.stdout.write(buf)
if __name__ == '__main__':
    handleSocketError()

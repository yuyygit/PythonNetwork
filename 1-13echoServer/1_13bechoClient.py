# encoding: utf-8
import socket
import sys
import argparse

host = 'localhost'

def echoClient(port):
    "A Simple echo client"
    #create a TCP/IP scoket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect the socket to the server
    server_address = (host, port)
    print "Connect to %s port %s " % server_address
    sock.connect(server_address)

    #send data
    try:
        message = "Test message. This will be echoed"
        print "Sending %s " % message
        sock.sendall(message.encode('utf-8'))
        #Look for the response
        amount_received = 0
        amount_excepted = len(message)
        while amount_received < amount_excepted:
            data = sock.recv(16)
            amount_received += len(data)
            print "Received: %s" % data

        # data = sock.recv(1024)
        # print "Received: %s" % data
    except socket.errno as e:
        print "Socket error %s " % e
    except Exception as e:
        print "Other exception：%s " % str(e)
    finally:
        print "Closing connection to the server"
        sock.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Socket server example')
    parser.add_argument('--port', action= 'store', dest= 'port', type = int, required = True)
    given_args = parser.parse_args()
    port = given_args.port
    echoClient(port)
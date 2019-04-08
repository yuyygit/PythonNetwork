# encoding: utf-8
import socket

def find_sever_name():
    protocolname = 'tcp'
    for port in [80,25]:
        print "Port: %s => services name: %s " %(port , socket.getservbyport(port, protocolname))
    print "Port: %s => services name: %s " % (53, socket.getservbyport(53,'udp'))

if __name__ == '__main__':
    find_sever_name()
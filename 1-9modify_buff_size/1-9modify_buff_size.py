# encoding: utf-8
import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modifyBuffSize():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get the size of the socket's buffer
    buffsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [Before]: %d " % buffsize

    # tcp级别
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    buffsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [After]: %d " % buffsize

if __name__ == '__main__':
    modifyBuffSize()

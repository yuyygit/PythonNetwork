# encoding: utf-8
import socket

def test_socket_modes():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(1)
    server.settimeout(5)
    server.bind(('192.168.0.3',0))
    socketAddress = server.getsockname()
    print "Trivial Server launched on socket: %s " % str(socketAddress)

    while True:
        server.listen(1)


if __name__ == '__main__':
    test_socket_modes()
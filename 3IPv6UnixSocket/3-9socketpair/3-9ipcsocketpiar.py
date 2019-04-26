# encoding: utf-8
import socket
import os

BUFSIZE = 1024

def test_socketpair():
    """ Test Unix socketpair"""
    parent, child = socket.socketpair()
    pid = os.fork()

    try:
        if pid:
            print "@Parent sending message..."
            print "Now pid is: %s" % pid
            child.close()

            parent.sendall("hello from parent!")
            response = parent.recv(BUFSIZE)
            print "Response from child:", response
            parent.close()
            pid_parent = os.getpid()
            print "Parent PID is: %s" % pid_parent
        else:
            print "@Child, waiting for message from parent"
            print "Now pid is: %s" % pid
            parent.close()
            message = child.recv(BUFSIZE)
            print "Message from parent:", message
            child.sendall("Hello from child")
            child.close()
            pid_child = os.getpid()
            print "Child PID is: %s" % pid_child

    except Exception as err:
        print "Error: %s " % err

if __name__ == '__main__':
    test_socketpair()
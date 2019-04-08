# encoding: utf-8
import socket
import struct

def convert_integer():
    adata = '1234'
    ndata = socket.inet_aton(adata)
    # ndata = struct.unpack
    print "Original: %s => Long host byte order： %s Network byte order: %s "\
        % (adata, socket.ntohl(struct.unpack('!L',ndata)[0]), socket.htonl(struct.unpack('!L',ndata)[0]))
    print "Original: %s => Short host byte order: %s Network byte order: %s "\
        % (adata, socket.ntohs(struct.unpack('!I',ndata)[0]), socket.htons(struct.unpack('!I',ndata)[0]))
if __name__ == '__main__':
    convert_integer()
#encoding:utf-8

import socket
import thread

def print_my_infomation():
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)
    print "host name is : %s" % hostName
    print "Local IP address is : %s" % ipAddress
def get_remote_info():

    '''
    每个DNS都会有自己对应的 连接，在访问不存在的页面使会返回这个连接
    :return:
    '''
    remoteHost = 'www.pytgo.org'
    try:
        print "Remote IP address is : %s " % socket.gethostbyname(remoteHost)
    except socket.error as err_msg:
        print "%s : %s" % (remoteHost, err_msg)

    # print "Remote IP address is : %s " % socket.gethostbyname('www.baidu.com')


if __name__ == '__main__':
    print_my_infomation()
    get_remote_info()

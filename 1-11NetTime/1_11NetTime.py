# encoding: utf-8
import ntplib
from time import ctime

def get_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('0.cn.pool.ntp.org')
    print ctime(response.tx_time)

if __name__ == '__main__':
    get_time()
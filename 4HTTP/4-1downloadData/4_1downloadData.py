# encoding: utf-8
import argparse
import httplib

REMOTE_SERVER_HOST = 'www.python.org'
REMOTE_SERVER_PATH = '/'

class HTTPClient(object):
    def __init__(self, host):
        self.host = host
    def fetch(self, path):
        http = httplib.HTTP(self.host)

        #Prepare header
        http.putrequest("GET", path)
        http.putheader("User-Agent", __file__)
        # http.putheader("User-Agent", "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
        http.putheader("HOST", self.host)
        http.putheader("Accept", "*/*")
        http.endheaders()

        try:
            errcode, errmsg, headers = http.getreply()
        except Exception as e:
            print "Client failed error code: %s  message: %s  headers: %s" % (errcode, errmsg, headers)
        else:
            print "Got homeage from %s" % self.host

        file = http.getfile()
        return file.read()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HTTP Client Example')
    parser.add_argument('--host', action="store", dest="host", default=REMOTE_SERVER_HOST)
    parser.add_argument('--path', action="store", dest="path", default=REMOTE_SERVER_PATH)
    given_args = parser.parse_args()
    host, path = given_args.host, given_args.path
    client = HTTPClient(host)
    print client.fetch(path)
    # client.fetch(path)

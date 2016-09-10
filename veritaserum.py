import requests
import urllib.parse
import socket

class Veritaserum(object):
    def __init__(self, url):
        self.original_url = url
        self.url = self.parse_url(url)
        self.hostname = self.url[1]

    def parse_url(self, url):
        return urllib.parse.urlsplit(url)

    def process(self):
        self.ip = self.process_dns()
        self.tcp = self.process_tcp()
        self.http = self.process_http()
        self.https = self.process_https()
        return self.get_response()

    def process_http(self):
        if self.tcp == None:
            return None
        url = self.url._replace(scheme='http')
        response = None
        try:
            return requests.get(url.geturl())
        except:
            return None

    def process_https(self):
        url = self.url._replace(scheme='https')
        response = None
        try:
            return requests.get(url.geturl())
        except:
            return None

    def process_tcp(self):
        if self.ip == None:
            return None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, 80))
            s.send(MESSAGE)
            return True
        except:
            return False

    def process_dns(self):
        try:
            return socket.gethostbyname(self.hostname)
        except e:
            return None

    def parse_response(self, res):
        if res == None:
            return None

        return {
            'headers': res.headers,
            'body': res.text,
            'status': res.status_code
        }

    def get_response(self):
        return {
            'tcp': self.tcp,
            'ip': self.ip,
            'http': self.parse_response(self.http),
            'https': self.parse_response(self.https)
        }

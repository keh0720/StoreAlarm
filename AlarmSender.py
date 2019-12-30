import requests


class AlarmSender:
    def __init__(self, url, body):
        self.url = url
        self.body = body
        self.header = {'Content-Type': 'application/json; charset=utf-8'}

    def set_url(self, url):
        self.url = url

    def set_body(self, body):
        self.body = body

    def send(self):
        res = requests.post(self.url, headers=self.header, data=self.body)
        return res

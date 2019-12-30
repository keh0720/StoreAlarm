class StoreItem:
    def __init__(self, time, site, subject, author, status, url):
        self.time = time
        self.site = site
        self.subject = subject
        self.author = author
        self.status = status
        self.url = url

    def to_string(self):
        item = ""
        if self.time:
            item += self.time + " "
        if self.site:
            item += self.site + " "
        if self.subject:
            item += self.subject + " "
        if self.author:
            item += self.author + " "
        if self.status:
            item += self.status + " "
        if self.url:
            item += self.url

        return item

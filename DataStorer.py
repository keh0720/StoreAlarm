import sqlite3 as sql
import StoreLogger

log = StoreLogger.log


class DataStorer:
    def __init__(self):
        print("DataStorer init")
        self.conn = sql.connect('store_data')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS store_data 
                                (time text , site text, subject text, 
                                author text, status text, url test, isAlarm bool)''')
        store_data = self.cursor.execute("SELECT * FROM store_data")
        for item in store_data:
            log.debug("Sended item " + item[0] + "/" + item[1] + "/" + item[2] + "/" + item[3] +
                      "/" + item[4] + "/" + item[5])

    def insert(self, target, data):
        for item in data:
            self.cursor.execute("INSERT INTO store_data VALUES (?,?,?,?,?,?,?)",
                                (item.time, target, item.subject, item.author, item.status, item.url, False))
            log.debug("insert item " + item.time + "/" + target + "/" + item.subject + "/" + item.author + "/" +
                      item.status + "/" + item.url + "/" + str(False))
            self.conn.commit()

    def select_all(self):
        store_data = self.cursor.execute("SELECT time, site, subject, author FROM store_data")
        list_store_data = {}
        for item in store_data:
            list_store_data[item[0] + '/' + item[1] + '/' + item[3]] = item[2]
        return list_store_data

    def update_status(self, time, site):
        self.cursor.execute("UPDATE store_data SET isAlarm = 1 WHERE time=? AND site=?", (time, site))
        log.debug("update status " + time + "/" + site)
        self.conn.commit()

    def __del__(self):
        print("DataStorer destroy")
        self.cursor.close()
        self.conn.close()

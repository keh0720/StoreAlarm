import errno
import sys
import time
import json

import StoreCrawler
import StoreLogger
from AlarmSender import AlarmSender
from DataStorer import DataStorer

log = StoreLogger.log

try:
    if sys.argv[1]:
        keyword = sys.argv[1]
except IndexError:
    log.error("please input keyword")
    sys.exit(errno.EINVAL)

log.info("Started StoreAlarm application")

url_clien = "https://www.clien.net"
url_clien_used = "https://www.clien.net/service/board/sold?&od=T31&po="
url_slack = "https://hooks.slack.com/services/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"
site_clien = "clien"
isPage = True

storer = DataStorer()

while True:
    clien = StoreCrawler.get_store_data(site_clien, url_clien_used, 0, 2)
    data = storer.select_all()

    for item in clien:
        if not data.get(item.time + '/' + item.site + '/' + item.author):
            if keyword in item.subject:
                storer.insert(site_clien, [item])

                str_body = item.site + " / " + item.time + " / [" + item.status + \
                    "] <" + url_clien + item.url + "|" + item.subject + ">"
                body = {"text": str_body}
                sender = AlarmSender(url_slack, json.dumps(body).encode('utf-8'))
                res = sender.send()
                log.debug("Found new item : " + item.subject)
                if res.status_code == 200:
                    log.debug("Success send message to Slack")
                    storer.update_status(item.time, item.site)

    time.sleep(60)

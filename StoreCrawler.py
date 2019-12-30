import requests
import StoreLogger
from bs4 import BeautifulSoup
from StoreItem import StoreItem

log = StoreLogger.log


def get_store_data(site, url, start, end):
    list_store_item = []

    for i in range(start, end):
        req = requests.get(url + str(i))

        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        list_content = soup.select('.list_content > .list_item')

        for item in list_content:
            status = item.select('div.list_title > a > .category_fixed')[0].text
            subject = item.select('div.list_title > a > span.subject_fixed')[0].text
            item_url = item.select('div.list_title > a')[0].get('href')
            author = item.get('data-author-id')
            time = item.select('.list_time > span > span')[0].text

            store_item = StoreItem(time, site, subject, author, status, item_url)
            list_store_item.append(store_item)

            log.debug("crawled item : " + store_item.to_string())

    return list_store_item


# get_store_data("clien", "https://www.clien.net/service/board/sold?&od=T31&po=", 0, 1)

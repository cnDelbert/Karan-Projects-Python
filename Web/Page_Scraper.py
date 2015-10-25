# -*- coding: utf-8 -*-
__author__ = 'Delbert'

"""
Page Scraper - Create an application which connects to a site and pulls out all links, or images, and saves them to a list. Optional: Organize the indexed content and don’t allow duplicates. Have it put the results into an easily searchable index file.
"""

from bs4 import BeautifulSoup
import requests

def request_content(addr):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate:",
        "Accept-Language": "en-US,zh-CN;q=0.8,zh;q=0.5,en;q=0.3",
        "Cache-Control": "max-age=0:",
        "Connection": "keep-alive",
        "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
        "Host": "docs.python-requests.org",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0"
    }
    r = requests.get(addr, headers=headers)
    return r.content


def main():
    addr = input("A url address is needed:\t")
    if not addr.startswith("http://"):
        addr += "http://" + addr

    content = request_content(addr)



if __name__ == "__main__"
    main()
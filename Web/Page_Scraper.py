# -*- coding: utf-8 -*-
__author__ = 'Delbert'

"""
Page Scraper - Create an application which connects to a site and pulls out all links, or images, and saves them to a list. Optional: Organize the indexed content and don’t allow duplicates. Have it put the results into an easily searchable index file.
"""
"""
Tips: Only static HTML would be parsed, and contents loaded by AJAX would not be captured.
"""

from bs4 import BeautifulSoup
import requests


def summary(links, images, domain=""):
    if domain:
        domain = domain + "/" if not domain.endswith("/") else domain
    print("Links in the page:")
    for link in links:
        if "javascript:" in link or "void()" in link or "void(0)" in link:
            continue
        elif link.startswith("//"):
            print("http:" + link)
        elif link.startswith("http"):
            print(link)
        else:
            print(domain + link)

    print("Images in the page:")
    for img in images:
        if img.startswith("//"):
            print("http" + img)
        elif img.startswith("http"):
            print(img)
        else:
            print(domain + img)


def parse_links(a_tag):
    links = list()
    for a in a_tag:
        links.append(a.get("href"))
    return links

def parse_imgs(img_tag):
    imgs = list()
    for img in img_tag:
        imgs.append(img.get("src"))
    return imgs


def parse_content(content):
    soup  = BeautifulSoup(content, "html.parser")
    print(soup.prettify())
    a_tag = soup.find_all("a")
    img_tag  = soup.find_all("img")
    links = parse_links(a_tag)
    imgs  = parse_imgs(img_tag)
    return links, imgs

def request_content(addr):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate:",
        "Accept-Language": "en-US,zh-CN;q=0.8,zh;q=0.5,en;q=0.3",
        "Cache-Control": "max-age=0:",
        "Connection": "keep-alive",
        "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0"
    }
    r = requests.get(addr, headers=headers)
    return r.content


def main():
    addr = input("A url address is needed:\t")
    if not addr.startswith("http"):
        addr = "http://" + addr
    content = request_content(addr)
    links, images = parse_content(content)
    summary(links, images, addr)


if __name__ == "__main__":
    main()
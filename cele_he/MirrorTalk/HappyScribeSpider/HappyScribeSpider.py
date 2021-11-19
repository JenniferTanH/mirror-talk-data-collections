import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re
import csv
import ssl
import SingleURLSpider

base_url = "https://www.happyscribe.com/public/search?keywords="
base_href = "https://www.happyscribe.com"
def getURL(search: str):
    search.replace(" ", "+")
    return base_url + search

def getHref(href: str):
    return base_href + href


def getData(start_url: str):
    link_list = []
    html = SingleURLSpider.RequestURL(start_url)

    # 指定html.parser进行解析
    soup = BeautifulSoup(html, 'html.parser')

    for item in soup.find_all('a', class_="hsp-card-episode"):
        # print(type(item))
        # print(item.attrs['href'])
        # print(getHref(item.attrs['href']))
        link_list.append(getHref(item.attrs['href']))

    data = []
    for url in link_list:
        data.append(SingleURLSpider.SpiderSingleURL(url))

    return data

def HappyScribeSpider(search:str):
    return getData(getURL(search))


# def main():
#     search = "Kanye"
#     data = HappyScribeSpider(search)
#     for i in data[0]:
#         print(i)
#     # print(data[0][12])
#
# if __name__ == "__main__":
#     main()
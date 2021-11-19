import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re
import csv
import ssl

# findSentence = re.compile(r'<div class="hsp-paragraph"(.*)</div>')


def dataProcess(str: str):
    idx = 0
    while(str[idx] == ' '):
        idx += 1
    str = str[idx:]

    return str

def getData(start_url: str):
    data = []
    html = RequestURL(start_url)

    # 指定html.parser进行解析
    soup = BeautifulSoup(html, 'html.parser')

    for item in soup.find_all('p', class_="hs-font-positive base hsp-paragraph-words"):
        str = dataProcess(item.string)
        # print(str)
        data.append(str)

    # print(len(data))
    print("Data from url:", start_url, "received")
    return data


def RequestURL(url: str):
    # 伪装一下，避免 418 anti-spider
    head = {
        "User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_15_7) AppleWebKit / "
                      "537.36(KHTML, likeGecko) Chrome / 92.0.4515.159Safari / 537.36"
    }

    request = urllib.request.Request(url, headers=head)
    html = ""

    # 提供SSL证书，避免 [SSL: CERTIFICATE_VERIFY_FAILED], 并作为参数传入 urlopen
    context = ssl._create_unverified_context()
    try:
        response = urllib.request.urlopen(request, context=context)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print("Failed because:", end="")
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    # print(html)
    return html

def SpiderSingleURL(url):
    return getData(url)

# def main():
#     start_url = "https://www.happyscribe.com/public/the-joe-rogan-experience/1554-kanye-west"
#     SpiderSingleURL(start_url)
#
#
# if __name__ == "__main__":
#     main()

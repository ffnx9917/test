from curl_cfi import requests
from bs4 import BeautifulSoup

# 目標 URL，可以換成你要抓取的網站
URL = "https://www.google.com"

def crawl():
    try:
        # 發送 HTTP GET 請求
        response = requests.get(URL)

        # 確保請求成功
        if response.status_code == 200:
            # 使用 BeautifulSoup 解析網頁內容
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string

            print(f"網站的標題是: {title}")
        else:
            print(f"無法抓取網頁，狀態碼: {response.status_code}")
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    crawl()

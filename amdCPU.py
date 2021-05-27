from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "do_it_django_prj.settings")

import django
django.setup()

# BlogData를 import해옵니다
from single_pages.models import amdCpu

def amd_cpu():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome('c:/temp/chromedriver.exe', options=options)

    browser.get('https://search.shopping.naver.com/search/all?catId=50001620&frm=NVSHCAT&origQuery=amd%20cpu&pagingIndex=1&pagingSize=40&productSet=total&query=amd%20cpu&sort=rel&timestamp=&viewType=list')

    while True:

        SCROLL_PAUSE_TIME = 2

        # 화면 최하단으로 스크롤 다운
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 페이지 로드를 기다림
        time.sleep(SCROLL_PAUSE_TIME)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        last_height = new_height

        # 새로운 높이가 이전 높이와 변하지 않았을 경우 스크롤 종료
        if new_height == last_height:
            break

        # 스크롤 다운이 된다면 스크롤 다운이 된 후의 창 높이를 새로운 높이로 갱신
        last_height = new_height

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    product_name = soup.select('div.basicList_title__3P9Q7 > a')
    product_price = soup.select('span.price_num__2WUXn')

    data = {}
    price = []
    i = 0

    for j in product_price:
        a = j.get_text('', strip=True)
        price.append(a)

    for item in product_name:
        data[item.text] = price[i]
        i = i + 1
    return data

# 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':
    amd_cpu = amd_cpu()
    for t, p in amd_cpu.items():
        amdCpu(product_title=t, product_price=p).save()
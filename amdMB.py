from bs4 import BeautifulSoup
from selenium import webdriver
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "do_it_django_prj.settings")

import django
django.setup()

# BlogData를 import해옵니다
from single_pages.models import amdMB

def amd_MB():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome('c:/temp/chromedriver.exe', options=options)

    browser.get('http://search.danawa.com/dsearch.php?query=%EC%95%94%EB%93%9C%20%EB%A9%94%EC%9D%B8%EB%B3%B4%EB%93%9C&originalQuery=%EC%95%94%EB%93%9C%20%EB%A9%94%EC%9D%B8%EB%B3%B4%EB%93%9C&previousKeyword=%EC%95%94%EB%93%9C%20%EB%A9%94%EC%9D%B8%EB%B3%B4%EB%93%9C&cate_c1=861&cate_c2=875&cate_c3=969&volumeType=allvs&page=1&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=113990&defaultPhysicsCategoryCode=861%7C873%7C960%7C0&defaultVmTab=2647&defaultVaTab=1960&tab=main')

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    product_name = soup.select('p.prod_name > a')
    product_price = soup.select('p.price_sect > a > strong')

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
    amd_MB = amd_MB()
    for t, p in amd_MB.items():
        amdMB(product_title=t, product_price=p).save()
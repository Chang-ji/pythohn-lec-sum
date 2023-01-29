from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

chrome = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(chrome, 10)

category = {
    "cpu": "873",
    "메인보드": "875",
    "메모리": "874",
    "그래픽카드": "876",
    "ssd": "32617",
    "케이스": "879",
    "파워": "880",
}

category_css = {
    c: "dd.category_" + category[c] + " a" for c in category
}


def find_present(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))


def finds_present(css):
    find_present(css)
    return chrome.find_elements_by_css_selector(css)


def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))


def finds_visible(css):
    find_visible(css)
    return chrome.find_elements_by_css_selector(css)


def go_to_category(category_name):
    find_visible(category_css[category_name]).click()
    time.sleep(1)


def choose_option(text, order):
    print("---------")
    print(text)
    print("---------")
    options = finds_visible(f"div.search_option_item:nth-child({order}) label.item_checkbox")
    for i in range(len(options)):
        print(f"{i + 1}. {options[i].get_attribute('innerText')}")
    choice = input("-> ")
    options[int(choice) - 1].click()
    return int(choice) - 1


def parse_products():
    products = []
    for p in finds_visible("div.scroll_box tr[class^=productList_]"):
        name = p.find_element_by_css_selector("p.subject a").text
        try:
            price = p.find_element_by_css_selector("span.prod_price").text
        except:
            continue
        products.append((name, price))
    return products


chrome.get(
    "http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_lw_esti")

# CPU 카테고리로 이동해요
go_to_category("cpu")
# 안내문구와 함께 첫번째 있는 선택 메뉴를 보여주고 선택한대로 클릭해요
choose_option("제조사를 골라주세요", 1)
# 선택된 대로 반영된 상품의 리스트를 출력해요
print(parse_products())

# 메인보드 카테고리로 이동해요
go_to_category("메인보드")
# 제조사 선택
choose_option("제조사를 골라주세요", 1)
# 제품 분류
choose_option("제품 분류를 골라주세요", 2)
# 선택된 대로 반영된 상품의 리스트를 출력해요
print(parse_products())


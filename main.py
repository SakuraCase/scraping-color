from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import random
import time
import json

# 待機時間
WAIT = 5

IN_PATH = "./img"
TMP_PATH = "./tmp"
URL = "https://lab.syncer.jp/Tool/Image-Color-Picker/"

def getColor(driver):
    path = os.path.abspath(IN_PATH)
    files = os.listdir(IN_PATH)

    html = driver.get(URL)

    for file in files:
        input_file = driver.find_element_by_xpath("//input[@class='di5']").send_keys(path + "/" + file)
        time.sleep(WAIT)
        color_code = driver.find_element_by_id("ct5").get_attribute('value')

        with open('/'.join([TMP_PATH, file.replace('.png',".txt")]), 'w') as f:
            f.write(color_code)


def outputHTML():
    files = os.listdir(TMP_PATH)
    head = '<!DOCTYPE html><html lang="ja" style="overflow-x: auto;"><head><meta charset="utf-8" /><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css"><title>title</title></head><body><section class="section"><div class="container">\n'
    footer = '</div></section></body>'

    colors = []
    for file in files:
        with open('/'.join([TMP_PATH, file])) as f:
            for line in f:
                colors.append(line.replace('\n', ''))

    content = ''
    for color in sorted(set(colors)):
        content += '<div style="background-color:' + color + '">' + color + '</div>\n'

    with open("index.html", 'w') as f:
        f.write(head + content + footer)


if __name__ == '__main__':
    # 初期設定
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,1024')
    driver = webdriver.Chrome(options=options)

    # getColor(driver)
    outputHTML()
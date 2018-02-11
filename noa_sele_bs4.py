#python3
#noa_sele_test.py
# -*- coding: utf-8 -*-
import selenium.webdriver
import bs4
import pprint
import sys
import re

rservation_day = sys.argv[1]
rservation_time = sys.argv[2]

username = "0095848"
password = "1112"
URL = "https://noah1.lan.jp/web/login.php"

webdriver = selenium.webdriver
browser = webdriver.Chrome()

browser.get(URL)
#sevice ace ログイン実施
login_username = browser.find_element_by_name("f_codeno")
login_username.send_keys(username)
login_password = browser.find_element_by_name("f_password")
login_password.send_keys(password)
login_password.send_keys('\n')

#振替予約の画面を表示
browser.find_element_by_css_selector('[href="./reserv/reserv_date.php"]').click()

#予約日程を指定
javascript_rservation_day  = "javascript:go_next('" + rservation_day + "')"
browser.execute_script(javascript_rservation_day)

#BeautifulSoupで対象の時間の予約ボタンを取得
#テーブル全体を取得
html = browser.page_source
soup = bs4.BeautifulSoup(html, "html.parser")
tr = soup.select('tr')
count=0
result_item = ""
for item_bs4 in tr:
    item = str(item_bs4)
    count+=1
    pattern = re.compile(r"%s" % rservation_time)
    match = pattern.search(item)
    if match is None:
        result = False
    else:
        result_item = item
        result = True
        break

split_item = result_item.split('<tr')

#対象のレコードのみ取得
count2 = 0
result_item2 = ""
for item2 in split_item:
    count2 += 1
    pattern2 = re.compile(r"%s" % rservation_time)
    match2 = pattern.search(item2)
    if match2 is None:
        result2 = False
    else:
        result_item2 = item2
        result2 = True
        break


if result2:
    print('空いてます')
else:
    print('満員でした')
    sys.exit()


#対象のHTML行のみ取得
splitline_item2 = result_item2.splitlines()

count3 = 0
result_item3 = ""
for item3 in splitline_item2:
    count3 += 1
    if "javascript" in item3:
        result_item3 = item3
        result3 = True
        break
    else:
        result3 = False
        print('満員でした')
        sys.exit()

#対象のjavascript文のみ取得
splitdq_item3 = result_item3.split('\"')

count4 = 0
result_item4 = ""
for item4 in splitdq_item3:
    count4 += 1
    if "javascript" in item4:
        result_item4 = item4
        result4 = True
        break
    else:
        result4 = False

if result4 == 'False':
    sys.exit()

#予約ボタンクリック
browser.execute_script(result_item4)

#予約確認ボタンクリック
browser.find_element_by_name("送　信").click()
print('予約できました。')

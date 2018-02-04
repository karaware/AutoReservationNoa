#python3
#noa_sele_test.py
# -*- coding: utf-8 -*-
import selenium.webdriver
import bs4
import pprint

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
browser.execute_script("javascript:go_next('2018-02-05')")

#BeautifulSoupで対象の時間の予約ボタンを取得
#テーブル全体を取得
html = browser.page_source
soup = bs4.BeautifulSoup(html)
tr = soup.select('tr')
count=0
result_item = ""
for item_bs4 in tr:
    item = str(item_bs4)
    count+=1
    if "横田" in item:
        result_item = item
        result = True
        break
    else:
        result = False
#print(result)
#print(count)
#print('---')
#print(result_item)
#print('---')
split_item = result_item.split('<tr')
#pprint.pprint(split_item)

#対象のレコードのみ取得
count2 = 0
for item2 in split_item:
    count2 += 1
    if "横田" in item2:
        result_item2 = item2
        result2 = True
        break
    else:
        result2 = False
#print(result2)
#print(count2)
#print('---')
#print(result_item2)
#print('---')

#対象のHTML行のみ取得
splitline_item2 = result_item2.splitlines()
#pprint.pprint(splitline_item2)

count3 = 0
for item3 in splitline_item2:
    count3 += 1
    if "javascript" in item3:
        result_item3 = item3
        result3 = True
        break
    else:
        result3 = False
        print('満員でした')
#print(result3)
#print(count3)
#print('---')
#pprint.pprint(result_item3)
#print('---')

#対象のjavascript文のみ取得
splitdq_item3 = result_item3.split('\"')
#pprint.pprint(splitdq_item3)

count4 = 0
for item4 in splitdq_item3:
    count4 += 1
    if "javascript" in item4:
        result_item4 = item4
        result4 = True
        break
    else:
        result4 = False
print(result4)
print(count4)
print('---')
pprint.pprint(result_item4)
print('---')
print(type(result_item4))

#予約ボタンクリック
browser.execute_script(result_item4)

#参考
#browser.execute_script("javascript:go_next('2018-02-05')")

#予約確認ボタンクリック
browser.find_element_by_name("送　信").click()







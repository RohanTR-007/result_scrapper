from gpa_cal import gpa, grade
from spread_sheet import write_sheet
import time
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import xlwt
from xlwt import Workbook
from bs4 import BeautifulSoup

head = ['SUB-CODE', 'SUBJECT-NAME', 'TOTAL-CREDITS',
        'TOTAL-MARKS', 'GRADE-LETTER', 'GRADE-POINT', 'EARNED-CREDITS']

browser = webdriver.Chrome()
l = int(179)
h = int(180)
# for i in range(177, 180):
print("usn = ", l)
while (l <= h):
    # filling usn
    url = "https://results.vtu.ac.in/JFEcbcs23/index.php"
    browser.get(url)
    # browser.maximize_window()
    usn_ele = browser.find_element(By.NAME, "lns")

    usn = f'1by20is{l}'
    usn_ele.send_keys(usn)


# getting img
    img_ele = browser.find_elements(By.TAG_NAME, 'img')
    print(img_ele[1].get_attribute('src'))
    with open('captcha_src.png', 'wb') as file:
        file.write(img_ele[1].screenshot_as_png)

# fill
    capt_ele = browser.find_element(By.NAME, "captchacode")

    capt = input('enter captcha')
    while (len(capt) < 6):
        print('Cpathca should contain 6 characters')
        print('Re-enter the captcha')
        capt = input('enter captcha')
    capt_ele.send_keys(capt)
# submit
    submit = browser.find_element(By.ID, 'submit')
    submit.click()
    try:
        WebDriverWait(browser, 5).until(EC.alert_is_present())
# switch_to.alert for switching to alert and accept
# If captcha is invalid it runs again for same usn
        a = browser.switch_to.alert
        print(a.text)
        a.accept()
        scrape = False
        continue
    except:
        print("No alert")
        scrape = True

    if (scrape):
        soup = BeautifulSoup(browser.page_source, "html5lib")
# Scrapping of name and usn
    USN = soup.find(
        'td', {'style': 'padding-left:15px;text-transform:uppercase'}).text.strip(' : ')
    NAME = soup.find('td', {'style': 'padding-left:15px'}).text.strip(' :')

    TableRows = soup.findAll('div', {'class': 'divTableRow'})
# Creating a table
    marks = []
    for i in TableRows:
        cells = i.findAll('div', {'class': 'divTableCell'})
        tmp = []
        for k in range(0, len(cells)):
            tmp.append(cells[k].text.strip())
        if (tmp not in marks):
            marks.append(tmp)

# Refactoring with only required data
    del (marks[0])
    del (marks[len(marks)-1])

# To store gpa details & its calculation
    gpa_table = []
    print(f'{NAME} | {USN}')
    gp = gpa(marks)
    sgpa = gp[1]/gp[2]
    # print(f'Earned Credits : {gp[1]}')
    # print(f'Total Credits {gp[2]}')
    # print(f'SGPA = {gp[1]/gp[2]}')

# witing into sheet
    
    write_sheet(USN, NAME, gp[0], gp[1], gp[2], sgpa)

    l += 1
browser.quit()

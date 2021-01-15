import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from _collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s_items = input("Enter search keywords: ")
s_location = input("Enter location: ")

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument('start-maximized')
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()


driver = webdriver.Chrome()
driver.get("https://www.google.com")
s_bar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
s_bar.send_keys(s_items, ' in ', s_location)
s_bar.send_keys(Keys.ENTER)
print('Key word entered...')
sleep(2)

driver.find_element_by_class_name('wUrVib').click()
print('On details page...')
sleep(1)
data_dict = defaultdict(list)
def get_data_fun():
    sleep(1)
    for item_name in driver.find_elements_by_class_name('dbg0pd'):
        data_dict['Name'].append(item_name.find_element_by_tag_name('div').text)
        item_name.click()
        sleep(1)
        # name_flag = False
        # address_flag = False
        c_no_flag = False
        link_flag = False

        # Phone No extraction
        detail_cont = driver.find_element_by_class_name('ifM9O')
        for span in detail_cont.find_elements_by_tag_name('span'):
            if span.get_attribute('role') == "link":
                # phone_nums.append(span.text)
                c_no_flag = True
                data_dict['ContactNo'].append(span.text)
        if c_no_flag == False:
            data_dict['ContactNo'].append('Not found.')

        # Address extraction
        data_dict['Address'].append(driver.find_element_by_class_name('LrzXr').text)

        #  Website links extractions
        links_cont = driver.find_element_by_class_name('SPZz6b')
        for website_link in links_cont.find_elements_by_tag_name('a'):
            if website_link.find_element_by_tag_name('div').text == 'Website':
                link_flag = True
                data_dict['Link'].append(website_link.get_attribute('href'))
                # print(website_link.get_attribute('href'))

        if link_flag == False:
            data_dict['Link'].append('Not Found')

    # return data_dict

def to_csv_fun():
    # data_dict = get_data_fun()
    # c_time = time.ctime()[11:16]
    table_data = pd.DataFrame(data_dict, index=range(1, (len(data_dict['Name']) + 1)))
    table_data.to_csv(f'{s_items}_in_{s_location}.csv')
    # print(f"File '{s_items}_in_{s_location}_{c_time}.csv' is generated...")


def main():
    print("This is main function.")
    next_but_flag = True
    while next_but_flag:
        sleep(2)
        td_list = []
        get_data_fun()
        table = driver.find_element_by_class_name('AaVjTc')
        for td in table.find_elements_by_tag_name('td'):
            td_list.append(td.text)
        print(td_list)
        if td_list.pop() == 'Next':
            print("Check Point 1")
            for button in table.find_elements_by_class_name('d6cvqb'):
                if button.text == 'Next':
                    print('Check Point 2')
                    next_but_link = button.find_element_by_tag_name('a').click()
                    break
        else:
            next_but_flag = False
            print("Check Point 3")
            # if button.text == '':
            #     print('None')
            # elif button.text == 'Next':
            #     print("next")
            #     next_but_link = button.find_element_by_tag_name('a')
            # elif button.text == 'Previous':
            #     print('previous')
            # elif button.text != 'Next':
            #     print('Next end')
            # if button.text == 'Next':
            #     # if button.find_element_by_tag_name('a').get_attribute('id') == 'pnnext':
            #     next_but_flag = True
            #     next_but_link = button.find_element_by_tag_name('a')
            #     print('C1')
            #     break
            # elif button.text == 'Previous':
            #     print('This is middle.')
            #     break
            # else:
            #     print('This is a False flag')
            #     next_but_flag = False

            # if button.text == 'Next' and button.find_element_by_tag_name('a').get_attribute('id') == 'pnnext':
            #     next_but_flag = True
            #     next_but_link = button.find_element_by_tag_name('a')
            #     # button.find_element_by_tag_name('a').click()
            # elif button.text == 'Previous' and button.find_element_by_tag_name('a').get_attribute('id') == 'pnprev':
            #     next_but_flag = True
            #
            # elif button.text != 'Next' and button.find_element_by_tag_name('a').get_attribute('id') != 'pnnext':
            #     next_but_flag = False
            #     print('False')

        # if next_but_flag:
        #     get_data_fun()
        #     next_but_link.click()
        #     sleep(1)
        # else:
        #     print('All pages are done. Alhamdulillah!')
        # sleep(2)

    to_csv_fun()


main()
print('\n\n----Code completed----')


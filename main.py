import requests
import pandas as pd
from bs4 import BeautifulSoup
from _collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s_items = 'female attire shops'  #input("Enter search keywords: ")
s_location = 'karachi'  #input("Enter location: ")

driver = webdriver.Chrome()
driver.get("https://www.google.com")
s_bar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
s_bar.send_keys(s_items, ' in ', s_location)
s_bar.send_keys(Keys.ENTER)
sleep(2)

driver.find_element_by_class_name('wUrVib').click()
sleep(1)
data_dict = defaultdict(list)

for item_name in driver.find_elements_by_class_name('dbg0pd'):
    data_dict['Name'].append(item_name.find_element_by_tag_name('div').text)
    item_name.click()
    sleep(1)
    # name_flag = False
    # address_flag = False
    c_no_flag = False

    # Phone No extraction
    detail_cont = driver.find_element_by_class_name('ifM9O')
    for span in detail_cont.find_elements_by_tag_name('span'):
        if span.get_attribute('role') == "link":
            # phone_nums.append(span.text)
            c_no_flag = True
            data_dict['ContactNo'].append(span.text)
    if c_no_flag == False:
        data_dict['ContactNo'].append('Contact No not found.')


    # phone_cont = driver.find_element_by_class_name('Z1hOCe')
    # for span in phone_cont.find_elements_by_tag_name('span'):
    #     print(span.text)
        # if span.get_attribute('aria-label'):
        #     print(span.get_attribute('aria-label'))

    #  Address extraction
    data_dict['Address'].append(driver.find_element_by_class_name('LrzXr').text)
    #  Website links extractions

    # links_cont = driver.find_element_by_class_name('SPZz6b')
    # for website_link in links_cont.find_elements_by_tag_name('a'):
    #     if website_link.find_element_by_tag_name('div').text == 'Website':
    #         print(website_link.get_attribute('href'))

#
# for item_add in driver.find_elements_by_class_name('rllt__details'):
#     for spans in item_add.find_elements_by_tag_name('span'):
#         other_data.append(spans.text)

# data_dict['ContactNo'] = phone_nums
# data_dict['Address'] = address
# data_dict['Name'] = item_names
# print(data_dict)

# compl_data = pd.DataFrame({
#     'Name': item_names,
#     'Adress': address,
#     'Contact No': phone_nums
# })
#
# print(compl_data)
# print(data_dict)
print(len(data_dict['Name']))
print(len(data_dict['ContactNo']))
print(len(data_dict['Address']))
table_data = pd.DataFrame(data_dict)
print(table_data)
table_data.to_csv('myData.csv')
print('\n\n----Code completed----')

# period_name = []
# description = []
# temprature = []
#
# for num in range(len(items)):
#     period_name.append(items[num].find(class_='period-name').get_text())
#     description.append(items[num].find(class_='short-desc').get_text())
#     temprature.append(items[num].find(class_='temp').get_text())
#
# weather_stuff = pd.DataFrame(
#     {
#         'Period' : period_name,
#         'Description' : description,
#         'Temprature' : temprature
#     })
# print(weather_stuff)
#
# weather_stuff.to_csv('Weather.csv')

#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp temp-high').get_text())
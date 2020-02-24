# -*- coding: utf-8 -*-

import requests
from lxml import html, etree
import random
from fake_useragent import UserAgent
import json
import pysnooper
import time
import csv
import sys
sys.path.append('..')
from proxy import proxy_list


def input_xpath():
    "input attributes"
    #scrapy path
    top_url = "https://www.bestbuy.com"
    url_detail = "https://www.google.com/search?q=apple+homepod+review&oq=apple+home+pod+&aqs=chrome.1.69i57j0l7.5075j0j7&sourceid=chrome&ie=UTF-8"
    id_list_xpath = "//div[@class='pla-ikpd__modal-content-container']/div[@class='cXr9rd']/div[@class='NYWkjc']/div[2]/div/text()"
    next_page_xpath = "//li[@class='page next']/a/@href"
    #xpath
    xpath_dic = {
        "rating_xpath": "//div[@class='c-ratings-reviews-v2 v-small']/i/@alt",
        "date_xpath": "//div[@class='disclaimer']/time/@title",
        "verified_reviews_xpath": "//div[@class='line-clamp']/p/text()",
    }
    #info output form match item numbers in xpath
    item_output = {
            "rating": "",
            "date": "",
            "verified_reviews": "",
            }
    return top_url, url_detail, id_list_xpath, xpath_dic, item_output, next_page_xpath

def __product():
    top_url, url_detail, id_list_xpath, xpath_dic, item_output, next_page_xpath = input_xpath()
    parse_data(top_url, id_list_xpath, url_detail, xpath_dic, item_output, next_page_xpath)

def parse_data(top_url, id_list_xpath, url_detail, xpath_dic, item_output, next_page_xpath, page=1):
    html_etree = html_request(url_detail)
    id_list = html_etree.xpath(id_list_xpath)
    print("id_list: ", id_list)
    print("len(id_list): ", len(id_list))
    id_xpaths = ["/li[@class='review-item'][%i]" % li_index+1 for li_index in range(len(id_list))]
    data = []
    for id_xpath in id_xpaths:
        item_output_dic = item_output.copy()
        for item_key, values_xpath in zip(item_output.keys(), xpath_dic.values()):
            item_xpath = id_xpath + values_xpath
            item_value = html_etree.xpath(item_xpath)
            item_dic = {item_key: item_value}       
            item_output_dic.update(item_dic)
        rating = item_output_dic['rating'][0].split(' ')[0]
        date = item_output_dic['date'][0]
        verified_reviews = ' '.join([elem for elem in item_output_dic['verified_reviews']])
        
        output_dic = {
            "rating": rating,
            "date": date,
            "verified_reviews": verified_reviews,
        }
        print(output_dic)
        data.append([rating, date, verified_reviews])
    with open('apple_homepod.csv', 'a+', newline='') as csv_file:
        spamwriter = csv.writer(csv_file)
        for data_row in data: 
            spamwriter.writerow(data_row)

    #next page
    nextpage_attempts = 1
    #attempt until get the xpath of next page
    while nextpage_attempts < 7:
        try:
            html_etree = html_request(url_detail)
            nextpage = html_etree.xpath(next_page_xpath)[0]
        except:   
            #rest 
            print("next page attempted: %i" % nextpage_attempts)
            print("Preparing for next attempt...")
            nextpage_attempts += 1
            delay = random.randint(60, 120) 
            time.sleep(delay)
            continue
        if nextpage:
            url_detail = top_url + nextpage 
            delay = random.randint(3, 10) #or (10, 20) to avoid block
            print("Finished page: %i" % page)
            page += 1
            print("scrapy delay %i seconds"%delay)
            time.sleep(delay)
            parse_data(top_url, id_list_xpath, url_detail, xpath_dic, item_output, next_page_xpath, page)
            break

    print("Accomplished Scrapy with %i pages and %i reviews in total" % (page, 10*page))

def html_request(url_detail):
    #return html request header, some web would ban coocikes
    user_agent = UserAgent().random
    HEADERS = {'User-Agent':user_agent,
                'Referer': "www.google.com"}
    proxies = proxy_list.get_proxy()
    attempts = 1
    while attempts < 50:
        try:
            session = requests.session()
            response = session.get(url_detail, headers=HEADERS, proxies=proxies, timeout=10)
            html_etree = etree.HTML(response.content.decode('utf-8'))    
            return html_etree

        except requests.exceptions.RequestException as e:
            print(e)
            print("HTML Request attempt: %i" % attempts)
            attempts += 1


def main():
    __product()

if __name__ == "__main__":
    main()
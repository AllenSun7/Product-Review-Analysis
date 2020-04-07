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
    #scrapy path
    top_url = "https://www.schooldigger.com"
    url_detail = "https://www.schooldigger.com/go/CA/cityrank.aspx?y=2005"
    id_list_xpath = "//div[@id='wrapper']/div[6]/div[@id='search-page-react-content']/div[@class='search-page-container map-on-left']/div[@id='search-page-list-container']/div[@id='grid-search-results']/ul[@class='photo-cards photo-cards_wow photo-cards_short']/li[40]/article[@id='zpid_45648816']/div[@class='list-card-info']/a[@class='list-card-link']/address[@class='list-card-addr']/text()"
    next_page_xpath = "//li[@class='a-last']/a/@href"
    #xpath
    xpath_dic = {
        "rating_xpath": "//i[@data-hook='review-star-rating']/span/text()",
        "date_xpath": "//span[@data-hook='review-date']/text()",
        "variation_xpath": "//a[@data-hook='format-strip']/text()",
        "verified_reviews_xpath": "//span[@data-hook='review-body']/span/text()",
    }
    #info output form match item numbers in xpath
    item_output = {
            "rating": "",
            "date": "",
            "variation": "",
            "verified_reviews": "",
            }
    return top_url, url_detail, id_list_xpath, xpath_dic, item_output, next_page_xpath

def __product():
    top_url, url_detail, id_list_xpath, xpath_dic, item_output, next_page_xpath = input_xpath()
    parse_data(top_url, id_list_xpath, url_detail, xpath_dic, item_output, next_page_xpath)

def parse_data(top_url, id_list_xpath, url_detail, xpath_dic, item_output, next_page_xpath, page=1):
    html_etree = html_request(url_detail)
    id_list = html_etree.xpath(id_list_xpath)
    # id_xpaths = ["//div[@id='%s']" % id_xpath for id_xpath in id_list]
    
    test_xpath = "//iv[@class='container'][2]/div[@class='row'][1]/div[@id='ctl00_ContentPlaceHolder1_RankHeader_divTitle']/h1[@id='ctl00_ContentPlaceHolder1_RankHeader_hTitle']/text()"
    test_xpath2 = "//div[@id='DataTables_Table_0_wrapper']/div/div[2]/table[@id='DataTables_Table_0']/tbody/tr[@class='odd'][1]/td[9]/text()"
    # test_xpath3 = "//div[@class='search-page-container map-on-left']/div[@id='search-page-list-container']/div[@id='grid-search-results']/div[@class='search-page-list-header']/h1[@class='search-title']/text()"
    # test_xpath4 = "//div[@id='wrapper']/div[6]/div[@id='search-page-react-content']/div[@class='search-page-container map-on-left']/div[@id='search-page-list-container']/div[@id='grid-search-results']/ul[@class='photo-cards photo-cards_wow photo-cards_short']/li[2]/article[@id='zpid_114314088']/div[@class='list-card-info']/div[@class='list-card-heading']/ul[@class='list-card-details']/text()"
    test_item = html_etree.xpath(test_xpath)
    test_item2 = html_etree.xpath(test_xpath2)
    # test_item3 = html_etree.xpath(test_xpath3)
    # test_item4 = html_etree.xpath(test_xpath4)
    data = []
    data.append(test_item)
    data.append(test_item2)
    # data.append(test_item3)
    # data.append(test_item4)
    print(data)

    # for id_xpath in id_xpaths:
    #     item_output_dic = item_output.copy()
    #     for item_key, values_xpath in zip(item_output.keys(), xpath_dic.values()):
    #         item_xpath = id_xpath + values_xpath
    #         item_value = html_etree.xpath(item_xpath)
    #         item_dic = {item_key: item_value}       
    #         item_output_dic.update(item_dic)
    #     rating = item_output_dic['rating'][0].split(' ')[0]
    #     date = item_output_dic['date'][0]
    #     color = item_output_dic['variation'][0].split(': ')[1]
    #     configuration = item_output_dic['variation'][1].split(': ')[1]
    #     verified_reviews = ' '.join([elem for elem in item_output_dic['verified_reviews']])
        
    #     output_dic = {
    #         "rating": rating,
    #         "date": date,
    #         "color": color,
    #         "configuration": configuration,
    #         "verified_reviews": verified_reviews,
    #     }
    #     print(output_dic)
    #     data.append([rating, date, color, configuration, verified_reviews])
    # with open('zillow_sf.csv', 'a+', newline='') as csv_file:
    #     spamwriter = csv.writer(csv_file)
    #     for data_row in data: 
    #         spamwriter.writerow(data_row)

    # #next page
    # nextpage_attempts = 1
    # #attempt until get the xpath of next page
    # while nextpage_attempts < 7:
    #     try:
    #         html_etree = html_request(url_detail)
    #         nextpage = html_etree.xpath(next_page_xpath)[0]
    #     except:   
    #         #rest 
    #         print("next page attempted: %i" % nextpage_attempts)
    #         print("Preparing for next attempt...")
    #         nextpage_attempts += 1
    #         delay = random.randint(60, 120) 
    #         time.sleep(delay)
    #         continue
    #     if nextpage:
    #         url_detail = top_url + nextpage 
    #         delay = random.randint(3, 10) #or (10, 20) to avoid block
    #         print("Finished page: %i" % page)
    #         page += 1
    #         print("scrapy delay %i seconds"%delay)
    #         time.sleep(delay)
    #         parse_data(top_url, id_list_xpath, url_detail, xpath_dic, item_output, next_page_xpath, page)
    #         break

    # print("Accomplished Scrapy with %i pages and %i reviews in total" % (page, 10*page))


def html_request(url_detail):
    #return html request header, some web would ban coocikes
    user_agent = UserAgent().random
    HEADERS = {'User-Agent':user_agent,
                'Referer': "www.google.com"}
    # proxies = proxy_list.get_proxy()
    # response = requests.get(url_detail, headers=HEADERS, proxies=proxies)
    response = requests.get(url_detail, headers=HEADERS)
    html_etree = etree.HTML(response.content.decode('utf-8'))
    return html_etree

def main():
    for i in range(50):
        print("===========try %i ========" % i)
        __product()
        

if __name__ == "__main__":
    main()
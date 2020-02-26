from selenium import webdriver
from selenium.webdriver import ActionChains
import csv
import sys
import time

class GoogleInfo():
    def __init__(self, website, output_csv):
        self.website = website
        self.output_csv = output_csv

    #chromedriver click to view reviews and click to "more revirews"
    def scrapy_info(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome invisible
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=chrome_options)

        browser.get(self.website)
        print(browser.current_url)
        #reviews click 
        reviews_elements = browser.find_element_by_xpath("//div[@class='Ell0k']/button[@class='Y92sLc'][2]")
        ac = browser.find_element_by_xpath("//div[@class='Ell0k']/button[@class='Y92sLc'][2]")
        ActionChains(browser).move_to_element(ac).click(ac).perform()
        time.sleep(2)
        browser.switch_to_window(browser.window_handles[-1])
        
        #get the initial reviews
        with open(self.output_csv, 'a+', newline='') as csv_file:
            spamwriter = csv.writer(csv_file)
            spamwriter.writerow(["rating", "date", "shop", "title", "verified_reviews"])
        self.get_info(browser)
        
        #more reviews
        count = 2  
        while True: 
            #stop while "more reviews" button not exists
            try:
                ac = browser.find_element_by_xpath("//div[@class='pla-ikpd-modal-reviews__reviews-modal']/div[@class='Y2yoUb']/div[2]/button[@jsname='LrJMvf']")
                ActionChains(browser).move_to_element(ac).click(ac).perform()
            except Exception as e:
                print("<p>Error: %s</p>" % str(e))
                print("Finished srapy! Total pages: %i, reviews: %i" % (count, count*10))
                break
            else: 
                #get new info
                time.sleep(1)
                try:
                    self.get_info(browser, count)
                    print("At page: %i" % count)
                    count += 1
                except Exception as e:
                    print("<p>Error: %s</p>" % str(e))
                    continue

        #closh browser
        browser.close()
        #quit chromedriver
        browser.quit()

    #get info from list of div 
    def get_info(self, browser, count=1):
        #numbers of div lists
        #A div list contains ten new reviews
        div_list_new_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/*[@data-hveid='CAEQAA']"
        div_list_new = browser.find_elements_by_xpath(div_list_new_xpath)
        div_list_lenth = len(div_list_new)
        #numbers of new reviews 
        list_new_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[@data-hveid='CAEQAA'][%i]/*" % div_list_lenth
        list_new_x = browser.find_elements_by_xpath(list_new_xpath)
        data = []
        rating = ''
        date = ''
        shop = ''
        title = ''
        verified_reviews = ''
        for i in range(len(list_new_x)):
            #click if there is a button of more under reviews
            #get the xpath of the second div
            try:
                button_xpath= "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]//button[@class='nyiKk']" % (div_list_lenth, (i+1))
                ac = browser.find_element_by_xpath(button_xpath)
                ActionChains(browser).move_to_element(ac).click(ac).perform()
                reviews_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]/div[@jsname='xsCKlc']/div[2]" % (div_list_lenth, (i+1))
            #else get the xpath of the first div
            except:
                reviews_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]/div[@jsname='xsCKlc']/div[1]" % (div_list_lenth, (i+1))
            
            rating_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]//span[@class='fTKmHE99XE4__star fTKmHE99XE4__star-xs']" % (div_list_lenth, (i+1))
            title_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]/div[1]" % (div_list_lenth, (i+1))
            date_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]//span[@class='ezBMsc D9Q5ge']" % (div_list_lenth, (i+1))
            shop_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]//span[@class='D9Q5ge']" % (div_list_lenth, (i+1))
            try: 
                #get attribute value for rating
                rating = browser.find_element_by_xpath(rating_xpath).get_attribute("aria-label")
                rating = rating.split(' ')[1]
                #get text
                title = browser.find_element_by_xpath(title_xpath).text
                date = browser.find_element_by_xpath(date_xpath).text
                shop = browser.find_element_by_xpath(shop_xpath).text
                shop = shop.split(' on ')[1]
                verified_reviews = browser.find_element_by_xpath(reviews_xpath).text
            except Exception as e:
                print("<p>Error: %s</p>" % str(e))

            print(rating)
            print(title)
            print(date)
            print(shop)
            print(verified_reviews)
            data.append([rating, date, shop, title, verified_reviews])
            print("=================== reviews: %i ===================" % (i+1))
            print(self.output_csv)
            print("=================== review at page: %i ===================" % count)
        
        #write into csv file
        with open(self.output_csv, 'a+', newline='') as csv_file:
            spamwriter = csv.writer(csv_file)
            for data_row in data: 
                spamwriter.writerow(data_row)

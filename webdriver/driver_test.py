from selenium import webdriver
from selenium.webdriver import ActionChains

import sys
import time

def scrapy_info():
    chrome_options = webdriver.ChromeOptions()
    #chrome invisible
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get('https://www.google.com/search?safe=active&sxsrf=ALeKk00Iv5DVSTq8EEHkIs4aloKTrDpDXA%3A1582608611729&ei=47BUXt6NLMv4-gTFxLXwBA&q=apple+homepod+reviews&oq=apple+homepod+reviews&gs_l=psy-ab.3..0l3j0i22i30l6.18669.20227..20435...0.2..0.107.689.7j1......0....1..gws-wiz.......0i71j35i39j0i20i263j0i67.CDVwVnXlanc&ved=0ahUKEwiei_vA_OvnAhVLvJ4KHUViDU4Q4dUDCAs&uact=5')
    print(browser.current_url)
    #reviews click 
    reviews_elements = browser.find_element_by_xpath("//div[@class='Ell0k']/button[@class='Y92sLc'][2]")
    ac = browser.find_element_by_xpath("//div[@class='Ell0k']/button[@class='Y92sLc'][2]")
    ActionChains(browser).move_to_element(ac).click(ac).perform()
    time.sleep(2)
    browser.switch_to_window(browser.window_handles[-1])
    
    #get the initial reviews
    get_info(browser)
    #more reviews
    count = 1 
    while count < 20:
        count += 1
        ac = browser.find_element_by_xpath("//div[@class='pla-ikpd-modal-reviews__reviews-modal']/div[@class='Y2yoUb']/div[2]/button[@class='dbG8V']")
        ActionChains(browser).move_to_element(ac).click(ac).perform()
        time.sleep(1)
        get_info(browser, count)
    #closh browser
    browser.close()
    #quit chreomedriver
    browser.quit()


def get_info(browser, count=1 ):
    div_list_new_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/*[@data-hveid='CAEQAA']"
    div_list_new = browser.find_elements_by_xpath(div_list_new_xpath)
    list_new_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[@data-hveid='CAEQAA'][%i]/*" % len(div_list_new)
    list_new_x = browser.find_elements_by_xpath(list_new_xpath)
    for i in range(len(list_new_x)):
        #click if there is a button of more under reviews
        #get the xpath of the second div
        try:
            button_xpath= "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]//button[@class='nyiKk']" % (len(div_list_new), (i+1))
            ac = browser.find_element_by_xpath(button_xpath)
            ActionChains(browser).move_to_element(ac).click(ac).perform()
            reviews_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]/div[@jsname='xsCKlc']/div[2]" % (len(div_list_new), (i+1))
        #else get the xpath of the first div
        except:
            reviews_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]/div[@jsname='xsCKlc']/div[1]" % (len(div_list_new), (i+1))
        
        rating_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]//span[@class='fTKmHE99XE4__star fTKmHE99XE4__star-xs']" % (len(div_list_new), (i+1))
        title_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]/div[@class='hhrMEf']" % (len(div_list_new), (i+1))
        date_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]//span[@class='ezBMsc D9Q5ge']" % (len(div_list_new), (i+1))
        shop_xpath = "//div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[%i]/div[@class='VATqJc'][%i]//span[@class='D9Q5ge']" % (len(div_list_new), (i+1))
        #get attribute value for rating
        rating = browser.find_element_by_xpath(rating_xpath).get_attribute("aria-label")
        #get text
        title = browser.find_element_by_xpath(title_xpath).text
        date = browser.find_element_by_xpath(date_xpath).text
        shop = browser.find_element_by_xpath(shop_xpath).text
        reviews = browser.find_element_by_xpath(reviews_xpath).text
        print(rating)
        print(title)
        print(date)
        print(shop)
        print(reviews)
        print("=================== reviews: %i ===================" % (i+1))
        print("=================== review at page: %i ===================" % count)


def main():
    scrapy_info()

if __name__ == "__main__":
    main()
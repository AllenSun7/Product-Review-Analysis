from selenium import webdriver
from selenium.webdriver import ActionChains
import csv
import sys
import time

# chromedriver click to view reviews and click to "more revirews"
def scrapy_info():
    website = "https://www.realtor.com/realestateandhomes-search/San-Francisco_CA"
    chrome_options = webdriver.ChromeOptions()
    # chrome invisible
    # chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get(website)
    print(browser.current_url)
    # reviews click 
    test_xpath1 = "//header[@id='srp-header']/div[@class='jsx-1038062002 title-wrapper']/h1[@class='jsx-1038062002 ellipsis']"
    # test_xpath2 = "//ul[@class='photo-cards photo-cards_wow photo-cards_short']/li[1]//div[@class='list-card-type']"
    # test_xpath3 = "//div[@id='wrapper']/div[6]/div[@id='search-page-react-content']/div[@class='search-page-container map-on-left']/div[@id='search-page-list-container']/div[@id='grid-search-results']/div[@class='search-page-list-header']/h1[@class='search-title']"
    # test_xpath4 = "//div[@id='wrapper']/div[6]/div[@id='search-page-react-content']/div[@class='search-page-container map-on-left']/div[@id='search-page-list-container']/div[@id='grid-search-results']/ul[@class='photo-cards photo-cards_wow photo-cards_short']/li[2]/article[@id='zpid_114314088']/div[@class='list-card-info']/div[@class='list-card-heading']/ul[@class='list-card-details']"
    test_item1 = browser.find_element_by_xpath(test_xpath1).text
    # test_item2 = browser.find_element_by_xpath(test_xpath2).text
    # test_item3 = browser.find_element_by_xpath(test_xpath3).text
    # test_item4 = browser.find_element_by_xpath(test_xpath4).text
    data = []
    # data.append(test_item1)
    # data.append(test_item2)
    # data.append(test_item3)
    data.append(test_item1)
    print(data)
    
    # ac = browser.find_element_by_xpath("//div[@class='Ell0k']/button[@class='Y92sLc'][2]")
    # ActionChains(browser).move_to_element(ac).click(ac).perform()
    # time.sleep(2)
    # browser.switch_to_window(browser.window_handles[-1])
    
    # #get the initial reviews
    # with open(self.output_csv, 'a+', newline='') as csv_file:
    #     spamwriter = csv.writer(csv_file)
    #     spamwriter.writerow(["rating", "date", "shop", "title", "verified_reviews"])
    # self.get_info(browser)
    #closh browser
    browser.close()
    #quit chromedriver
    browser.quit()


def main():
    scrapy_info()

if __name__ == "__main__":
    main()
from selenium import webdriver
from selenium.webdriver import ActionChains

import sys
import time

chrome_options = webdriver.ChromeOptions()
#chrome invisible
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.google.com/search?q=apple+homepod+review&oq=apple+home+pod+&aqs=chrome.1.69i57j0l7.5075j0j7&sourceid=chrome&ie=UTF-8')
print(browser.current_url)
reviews_elements = browser.find_element_by_xpath("//div[@class='Ell0k']/button[@class='Y92sLc'][2]")
#reviews_elements.click()
ac = browser.find_element_by_xpath("//div[@class='Ell0k']/button[@class='Y92sLc'][2]")
ActionChains(browser).move_to_element(ac).click(ac).perform()
time.sleep(3)
browser.switch_to_window(browser.window_handles[-1])

test_xpath = "//div[@class='pla-ikpd__modal-content']/div[@class='pla-ikpd-modal-reviews__reviews-modal']/div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[1]/div[@class='VATqJc'][1]/div[@class='hhrMEf']"
test3_xpath = "//div[@class='pla-ikpd__modal-content']/div[@class='pla-ikpd-modal-reviews__reviews-modal']/div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[1]/div[@class='VATqJc'][1]//span[@class='ezBMsc D9Q5ge']"
#test3_xpath = "//div[@class='pla-ikpd__modal-content']/div[@class='pla-ikpd-modal-reviews__reviews-modal']/div[@class='Y2yoUb']/div[2]/div[@id='pla-ikpd__pla-dru']/div[1]/div[@class='VATqJc'][1]/div[2]/div[@id='_uAtUXprQA__O0PEP3rqK-AY1-full']"
print("=============test============")
test = browser.find_element_by_xpath(test_xpath).text
test3 = browser.find_element_by_xpath(test3_xpath).text
print(test)
print(test3)
print("=============test============")
#closh browser
browser.close()
#quit chreomedriver
browser.quit()

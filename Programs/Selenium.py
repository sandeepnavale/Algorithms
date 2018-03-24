from selenium import webdriver
from selenium.webdriver.chrome.options import Options

my_chrome_options = Options()
my_chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=my_chrome_options)
driver.get('https://www.linkedin.com/jobs/')
driver.find_element_by_xpath('//*[@id="keyword-search-box"]').send_keys("Developer")
driver.find_element_by_xpath('//*[@id="location-search-box"]').send_keys("Sydney")

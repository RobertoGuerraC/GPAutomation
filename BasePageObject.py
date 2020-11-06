from selenium import webdriver


# Inicialize with chrome
driver = webdriver.Chrome('C:/Users/rguerra/AppData/Local/Google/Chrome/Application/chromedriver')


# Wrapping methods of selenium
def get(url):
    driver.implicitly_wait(10)
    driver.get(url)

def find_element_by_xpath(location):
    driver.find_element_by_xpath(location)

def click(location):
    driver.find_element_by_xpath(location).click()

def send_keys(location, value):
    driver.find_element_by_xpath(location).send_keys(value)

def close():
    driver.close()

def screenshot(name):
    driver.save_screenshot(name+'.png')

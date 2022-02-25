from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--remote-debugging-port=9222") 
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver


def get_element(url: str, query: str, driver: webdriver.Chrome):
    driver.get(url)
    elements = driver.find_elements_by_xpath(query)
    results = [e.text for e in elements]
    return results
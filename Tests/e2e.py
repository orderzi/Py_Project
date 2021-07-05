from selenium import webdriver
from selenium.common.exceptions import *


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
driver = webdriver.Chrome('C:\chromedriver.exe', options=chrome_options)
# Run selenium on chrome without opening it

def test_scores_service(app_url):
    try:
        website_score = driver.get(app_url)
        website_score = int(driver.find_element_by_id('score').text)
    except WebDriverException:
        print('Site is not reachble')
        return False
    try:
        assert 1 <= website_score <= 1000, 'Value must be 1-1000'
        return True
    except AssertionError as msg:
        print(msg)
        return False

def main():
    call_test = test_scores_service('enter_url')
    if call_test:
        return True
    else:
        return False

if __name__ == '__main__':
    final = main()
    print(final)

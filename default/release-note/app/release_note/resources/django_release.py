import datetime
import requests
from release_note.model.release_item import ReleaseItem
from release_note.utils.functions import is_version_matched
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class DjangoRelease():
    def __init__(self):
        pass

    def get(self, min_version='', max_version=''):
        items = []

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--disable-dev-shm-usage")
        path='/chromedriver'

        response = requests.get("https://docs.djangoproject.com")
        response.raise_for_status()
        tree = BeautifulSoup(response.text, features="html.parser")
        url = tree.select('link')[0]['href']
        release_url = ( f'{url}/releases')
        release_response = requests.get(release_url)
        release_response.raise_for_status()
        release_tree = BeautifulSoup(release_response.text, features="html.parser")
        versions_tree = release_tree.select('li.toctree-l1')

        driver = webdriver.Chrome(path, chrome_options=chrome_options)
        for row in versions_tree:
            version = row.select_one('a')['href'].replace('/', '')
            if not is_version_matched(version, min_version=min_version, max_version=max_version):
                continue
            version_url = f'{release_url}/{version}'
            if version_url == 'https://docs.djangoproject.com/en/4.1//releases/1.2.5':
                break
            driver.get(version_url)
            date_str = driver.find_element(By.TAG_NAME, r'em')
            if date_str.text.find('Expected') != -1:
                continue
            else:
                link = version_url
                release_date = date_str.text.replace(',', '')
                release_date = datetime.datetime.strptime(release_date, "%B %d %Y")
            
            items.append(ReleaseItem(product_name="django", 
                        link=link, 
                        release_date=release_date, 
                        version=version))
        driver.close()
        return items



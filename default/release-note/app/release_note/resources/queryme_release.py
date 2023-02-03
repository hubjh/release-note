from bs4 import BeautifulSoup
import datetime
import requests
from release_note.model.release_item import ReleaseItem
from release_note.utils.functions import is_version_matched
import re

class QuerymeRelease():
    def __init__(self):
        pass

    def get(self, min_version='', max_version=''):
        release_date_list = []
        version_list = []
        url_list = []
        items = []
        
        response = requests.get("https://query.me/release-notes/")
        response.raise_for_status()
        tree = BeautifulSoup(response.text, features="html.parser")

        for row in tree.select('time'):
            if not row:
                continue
            release_date_list.append(row['datetime'])
            
        regex = re.compile('[\d+][.][\d+][.]?[\d+]?')

        for row in tree.select('a.card-body > h3'):
            if not row:
                continue
            row = regex.findall(row.text.strip())
            if not row:
                row = ['New']
            version_list.append(row[0])

        for row in tree.select('a.card-body'):
            if not row:
                continue
            link = row['href']
            url_list.append(f'https://query.me{link}')

        for idx in range(len(version_list)):
            version = version_list[idx]
            if not is_version_matched(version, min_version=min_version, max_version=max_version):
                continue

            release_date = datetime.datetime.strptime(release_date_list[idx], "%Y-%m-%d")
            link = url_list[idx]
            items.append(ReleaseItem(product_name="queryme", 
                        link=link, 
                        release_date=release_date, 
                        version=version))
        return items

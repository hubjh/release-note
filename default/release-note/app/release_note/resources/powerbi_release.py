# 2022/12/28 황준호
# 웹사이트의 내용이 바뀌면서 61줄에서 version = re.sub("[()]","", split_str[1]).strip() 부분에서 오류가 발생 수정
# 2023/1/30 황준호
# 웹사이트의 내용이 바뀌면서 17줄에서 selected_tags = tree.select('h2') 부분에서 오류가 발생 수정

from bs4 import BeautifulSoup
import datetime
import requests
from release_note.model.release_item import ReleaseItem
from release_note.utils.functions import is_version_matched
import re

def multiple_requests(input_url):
    response = requests.get(input_url)
    response.raise_for_status()
    tree = BeautifulSoup(response.text, features="html.parser")
    selected_tags = tree.select('h2[id]')

    return selected_tags

class PowerbiRelease():
    def __init__(self):
        pass

    def get(self, min_version='', max_version=''):
        items = []
        product_name = "powerbi"
        request_url = "https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-latest-update?tabs=powerbi-desktop"
        processed_tree = multiple_requests(request_url)

        url_piece = processed_tree[0]['id']
        split_str = processed_tree[0].string.split('Update')
        date_piece = split_str[0].strip()

        version = re.sub("[()]","", split_str[1]).strip()
        release_date = datetime.datetime.strptime(date_piece, "%B %Y")
        link = f'{request_url}#{url_piece}'
        
        items.append(ReleaseItem(product_name=product_name, 
                        link=link, 
                        release_date=release_date, 
                        version=version))

        request_url = "https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-latest-update-archive?tabs=powerbi-desktop"
        processed_tree = multiple_requests(request_url)

        for row in processed_tree:
            if not row:
                continue
            if row['id'] == 'feedback' :
                continue
            if row['id'] == "additional-resources-mobile-heading" :
                continue
            if row['id'] == "additional-resources-heading" :
                continue

            url_piece = row['id']
            split_str = row.string.split('Update')
            date_piece = split_str[0].strip()

            version = re.sub("[()]","", split_str[1]).strip()
            release_date = datetime.datetime.strptime(date_piece, "%B %Y")
            link = f'{request_url}#{url_piece}'
            items.append(ReleaseItem(product_name=product_name, 
                        link=link, 
                        release_date=release_date, 
                        version=version))
        return items
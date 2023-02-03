from bs4 import BeautifulSoup
import datetime
import requests
from release_note.model.release_item import ReleaseItem
from release_note.utils.functions import is_version_matched
import re

class TableauRelease():
    def __init__(self):
        pass

    def get(self, min_version='', max_version=''):
        items = []
        response = requests.get("https://www.tableau.com/support/releases/server")
        response.raise_for_status()
        tree = BeautifulSoup(response.text, features="html.parser")
        
        selected_tags = tree.select('td > a')

        for row in selected_tags:
            if not row:
                continue
            version = row.text.strip().split('\n')[0]
            url_piece = row['href'] 
            date_piece = row.select_one('span').string.strip().replace('Released ', '').replace(',', '')

            release_date = datetime.datetime.strptime(date_piece, "%b %d %Y")
            link = url_piece
            items.append(ReleaseItem(product_name="tableau", 
                        link=link, 
                        release_date=release_date, 
                        version=version))
        return items
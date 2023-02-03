from bs4 import BeautifulSoup
import datetime
import requests
from release_note.model.release_item import ReleaseItem
from release_note.utils.functions import is_version_matched
import re

class HiveRelease():
    def __init__(self):
        pass

    def get(self, min_version='', max_version=''):
        response = requests.get("https://hive.apache.org/downloads.html")
        response.raise_for_status()
        tree = BeautifulSoup(response.text, features="html.parser")
        items = []
        except_string = '/hcatalog_downloads.html'
        url_list = []    
        version_list = []
        release_date_list = []
        for row in tree.select('p > a')[:-1]:
            if not row:
                continue
                
            if row['href'] == except_string:
                continue
            else:
                url_list.append(row['href'])

        for row in tree.select('h3'):
            if not row:
                continue
            if row['id'] == '28-jan-2016--hive-parent-auth-hook-made-available':
                continue
            if row['id'] == 'march-2013-hcatalog-merges-into-hive':
                continue         

            date_time = row.text.split(':')[0].strip().replace(',' , '')
            
            if row.text.split(':')[1].strip().split(' ')[1].replace(',' , '') == '1.0.1': # version : 1.0.1, 1.1.1
                version_list.append(row.text.split(':')[1].strip().split(' ')[1].replace(',' , ''))
                version_list.append(row.text.split(':')[1].strip().split(' ')[2].replace(',' , ''))
                release_date_list.append(date_time)
                release_date_list.append(date_time)
            else:
                version_list.append(row.text.split(':')[1].strip().split(' ')[1].replace(',' , ''))
                release_date_list.append(date_time)

        for idx in range(len(version_list)):
            version = version_list[idx]
            if not is_version_matched(version, min_version=min_version, max_version=max_version):
                continue
                
            release_date = datetime.datetime.strptime(release_date_list[idx], "%d %B %Y")
            link = url_list[idx]
            items.append(ReleaseItem(product_name="hive", 
                        link=link, 
                        release_date=release_date, 
                        version=version))
        return items

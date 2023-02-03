import datetime
import requests
from release_note.model.release_item import ReleaseItem
from release_note.utils.functions import is_version_matched
import re

class KafkaRelease():
    def __init__(self):
        pass

    def get(self, min_version='', max_version=''):
        response = requests.get("https://archive.apache.org/dist/kafka/")
        response.raise_for_status()
        items = []

        html = response.text
        img_tag = '<img src="/icons/folder.gif" alt="[DIR]">'
        for row in html[html.find(img_tag):].split(img_tag):
            row = row.strip()
            if not row:
                continue
        
            if row.find('<a href="old_releases/">old_releases/</a>') != -1:
                break

            pieces = [p.strip() for p in row.split(" ") if p.strip()]
            version = re.findall("\>.*\<", pieces[1])[0][1:-2]
            release_date = datetime.datetime.strptime(pieces[2] + " " + pieces[3], "%Y-%m-%d %H:%M")

            if not is_version_matched(version, min_version=min_version, max_version=max_version):
                continue

            items.append(ReleaseItem(
                        product_name="kafka", 
                        link=f"https://archive.apache.org/dist/kafka/{version}/RELEASE_NOTES.html", 
                        release_date=release_date, 
                        version=version))

        return items

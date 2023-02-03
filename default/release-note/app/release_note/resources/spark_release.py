from bs4 import BeautifulSoup
import datetime
import requests
from release_note.model.release_item import ReleaseItem
from release_note.utils.functions import is_version_matched
import re

class SparkRelease():
    def __init__(self):
        pass

    def get(self, min_version='', max_version=''):

        response = requests.get("https://archive.apache.org/dist/spark/")
        response.raise_for_status()
        items = []

        tree = BeautifulSoup(response.text, features="html.parser")

        for row in tree.select('a[href^="spark"]'):
            row = f"{str(row)} {row.next_sibling.strip()}"
            row = row.strip()

            if not row:
                continue

            pieces = [p.strip() for p in row.split(" ") if p.strip()]
            version = re.findall("\>.*\<", pieces[1])[0][1:-2].split('-')[1]
            release_date = datetime.datetime.strptime(pieces[2] + " " + pieces[3], "%Y-%m-%d %H:%M")

            if not is_version_matched(version, min_version=min_version, max_version=max_version):
                continue

            items.append(ReleaseItem(
                        product_name="spark", 
                        link=f"https://spark.apache.org/releases/spark-release-{version}.html", 
                        release_date=release_date, 
                        version=version))

        return items
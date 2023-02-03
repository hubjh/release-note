import datetime
import requests
from bs4 import BeautifulSoup
from release_note.model.release_item import ReleaseItem
from release_note.utils.functions import is_version_matched

class PythonRelease():
    def __init__(self):
        pass

    def _parse_month(self, text):
        months = {
            "Jan.": "January",
            "Feb.": "February",
            "March": "March",
            "April": "April",
            "May": "May",
            "June": "June",
            "July": "July",
            "Aug.": "August",
            "Sept.": "September",
            "Oct.": "October",
            "Nov.": "November",
            "Dec.": "December"
        }
        
        for python_month, month in months.items():
            text = text.replace(python_month, month)
        return text
        
    def get(self, min_version='', max_version=''):
        
        response = requests.get("https://www.python.org/downloads/")
        response.raise_for_status()
        tree = BeautifulSoup(response.text, features="html.parser")
        items = []
        for row in tree.select(".download-list-widget")[0].select(".list-row-container li"):

            version = row.select(".release-number")[0].text.replace("Python", "").split()
            if not is_version_matched(version, min_version=min_version, max_version=max_version):
                continue

            release_date = datetime.datetime.strptime(self._parse_month(row.select(".release-date")[0].text), "%B %d, %Y")
            link = row.select(".release-enhancements > a")[0].get("href")
            version = version[0]
            items.append(ReleaseItem(product_name="python", 
                        link=link, 
                        release_date=release_date, 
                        version=version))

        return items
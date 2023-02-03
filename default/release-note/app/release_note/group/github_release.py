import requests
import datetime
import time
from release_note.model.release_item import ReleaseItem
from release_note.utils.functions import is_version_matched

class GithubRelease():
    def __init__(self, product_name, owner, repo):
        self._product_name = product_name
        self._owner = owner
        self._repo = repo

    def get(self, min_version, max_version):
        headers = {
            "Accept": "application/vnd.github+json",
        }
        username = 'Bearer'
        token = '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'
        page = 1
        loop = True
        all_response = []
        while loop:
            params ={
                'page' : page,
                'per_page': '100'
            }
            response = requests.get(f"https://api.github.com/repos/{self._owner}/{self._repo}/releases", params=params, headers=headers, auth=(username,token))
            response.raise_for_status()
            if len(response.json()) == 0:
                loop = False
            page += 1
            all_response.extend(response.json())
        items = []
        for item in all_response:
            if not is_version_matched(item["tag_name"], min_version=min_version, max_version=max_version):
                continue

            items.append(ReleaseItem(product_name=self._product_name, 
                        link=item["html_url"], 
                        release_date=datetime.datetime.strptime(item["published_at"], '%Y-%m-%dT%H:%M:%SZ'), 
                        version=item["tag_name"],
                        body=item["body"]))

        return items

# from release_note.group.github_release import GithubRelease
import datetime
import requests
from release_note.model.release_item import ReleaseItem
from release_note.utils.functions import is_version_matched
import re
# class HadoopRelease(GithubRelease):
#     def __init__(self):
#         super().__init__(product_name="hadoop", owner='apache', repo='hadoop')

# ========================

# def select_html_tag(html):
#     img_tag = '<img src="/icons/folder.gif" alt="[DIR]">'
#     return html[html.find(img_tag):].split(img_tag)

# def get_version(pieces):
#     return re.findall("\>.*\<", pieces[1])[0][1:-2].replace('hadoop-', '')
    
# def get_release_date(pieces):
#     return datetime.datetime.strptime(pieces[2] + " " + pieces[3], "%Y-%m-%d %H:%M")

# def get_link(version):
#     return f"https://archive.apache.org/dist/hadoop/common/{version}/RELEASENOTES.md"

# class HadoopRelease():
#     def __init__(self):
#         pass

#     def get(self, min_version='', max_version=''):
#         items = []
#         response = requests.get("https://archive.apache.org/dist/hadoop/common/")
#         response.raise_for_status()
#         html = response.text 
#         img_tag_selected_html = select_html_tag(html)
#         for row in img_tag_selected_html:
#             row = row.strip()
#             if not row:
#                 continue
#             if row.find('<a href="alpha/">alpha/</a>') != -1:
#                 continue
#             if row.find('<a href="beta/">beta/</a>') != -1:
#                 continue
#             if row.find('<a href="current/">current/</a>') != -1:
#                 continue
#             if row.find('<a href="current2/">current2/</a>') != -1:
#                 continue  
#             if row.find('<a href="stable/">stable/</a>') != -1:
#                 break
#             pieces = [p.strip() for p in row.split(" ") if p.strip()]
#             version = get_version(pieces)
#             release_date = get_release_date(pieces)
#             link = get_link(version)


#             if not is_version_matched(version, min_version=min_version, max_version=max_version):
#                 continue

#             items.append(ReleaseItem(
#                         product_name="hadoop", 
#                         link=f"https://archive.apache.org/dist/hadoop/common/{version}/RELEASENOTES.md", 
#                         release_date=release_date, 
#                         version=version))

#         return items

class HadoopRelease():
    def __init__(self):
        pass

    def get(self, min_version='', max_version=''):
        response = requests.get("https://archive.apache.org/dist/hadoop/common/")
        response.raise_for_status()
        items = []

        html = response.text

        img_tag = '<img src="/icons/folder.gif" alt="[DIR]">'

        for row in html[html.find(img_tag):].split(img_tag):
            row = row.strip()

            if not row:
                continue
            if row.find('<a href="alpha/">alpha/</a>') != -1:
                continue
            if row.find('<a href="beta/">beta/</a>') != -1:
                continue
            if row.find('<a href="current/">current/</a>') != -1:
                continue
            if row.find('<a href="current2/">current2/</a>') != -1:
                continue  
            if row.find('<a href="stable/">stable/</a>') != -1:
                break

            pieces = [p.strip() for p in row.split(" ") if p.strip()]
            version = re.findall("\>.*\<", pieces[1])[0][1:-2].replace('hadoop-', '')
            release_date = datetime.datetime.strptime(pieces[2] + " " + pieces[3], "%Y-%m-%d %H:%M")

            if not is_version_matched(version, min_version=min_version, max_version=max_version):
                continue

            items.append(ReleaseItem(
                        product_name="hadoop", 
                        link=f"https://archive.apache.org/dist/hadoop/common/{version}/RELEASENOTES.md", 
                        release_date=release_date, 
                        version=version))

        return items


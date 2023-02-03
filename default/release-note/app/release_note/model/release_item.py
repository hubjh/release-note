from dataclasses import dataclass
import datetime

@dataclass
class ReleaseItem():
    product_name: str
    version: str
    release_date: datetime.datetime
    link: str
    body: str = ""
    summary: str = ""
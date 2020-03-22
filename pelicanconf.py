#!/usr/bin/env python
# -*- coding: utf-8 -*- #
AUTHOR = "Saigon FGC"
SITENAME = "GBVS Sài Gòn"
SITEURL = ""

PATH = "content"

TIMEZONE = "Asia/Ho_Chi_Minh"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "gbvs-theme"

MENUITEMS = [
    ("Hướng dẫn game", "/category/huong-dan-game.html"),
]
CURRENT_YEAR = "2020"
JINJA_FILTERS = {
    "vnstrftime": lambda date: f"{date.day} tháng {date.month}, {date.year}",
}
STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}
FOOTER_TEXT = 'Làm bằng ♥ và hơi nhiều <a href="https://user-images.githubusercontent.com/1446315/77242828-64e4bc80-6c35-11ea-8a89-605489dad646.png">Georgia Max</a>'
TYPOGRIFY = True

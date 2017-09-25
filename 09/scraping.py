# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

"""
世界各国の国名の英語を抽出するスクリプト
"""


def main():
    url = "http://eigomoromoro.blog.fc2.com/blog-entry-29.html"
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, "html.parser")
    spans = soup.find_all("span", style="color:#006600")
    countries = [span.get_text() for span in spans]
    with open("countries.txt", "w") as f:
        f.write("\n".join(countries))


if __name__ == "__main__":
    main()

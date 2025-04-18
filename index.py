from bs4 import BeautifulSoup
import openpyxl
import requests
from urllib.parse import urljoin

res = requests.get("https://hsmkrt1996.com/")
soup = BeautifulSoup(res.text, "html.parser")
title = soup.find("title").text

robots_url = urljoin("https://www.google.com/", '/robots.txt')
robots_response = requests.get(robots_url)
robots_response.raise_for_status()
robots_content = robots_response.text

print(robots_content)

wb = openpyxl.Workbook()
wb.save(f"sitemap-{title}.xlsx")

print("実行が完了しました")

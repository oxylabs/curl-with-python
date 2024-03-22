import pycurl
from io import BytesIO
from bs4 import BeautifulSoup

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, "https://books.toscrape.com")
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
html = buffer.getvalue().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
# Extract data from the parsed HTML
title = soup.find("title")
print(title.text)

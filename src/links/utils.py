import requests
import lxml
from bs4 import BeautifulSoup
import re

def get_link_data(url):
     headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64",
          "Accept-Language": "en",
     }

     response = requests.get(url, headers=headers)
     

     soup = BeautifulSoup(response.text, "lxml")

     if url[0:21]=="https://www.amazon.in":
          name = soup.select_one(selector="#productTitle").getText()
          name = name.strip()

          price = soup.select_one(selector=".a-offscreen").getText()
          price = re.sub(",", "", price)
          price = float(price[1:])
     
     elif url[0:27]=="https://www.aliexpress.com":
          name = soup.select_one(selector=".product-title-text").getText()
          name = name.strip()

          price = soup.select_one(selector=".product-price-value").getText()
          price = re.sub(",", "", price)
          price = float(price[1:])

     else:
          name = soup.select_one(selector=".B_NuCI").getText()
          name = name.strip()

          price = soup.select_one(selector="._30jeq3._16Jk6d").getText()
          price = re.sub(",", "", price)
          price = float(price[1:])

     return name, price
import requests
from bs4 import BeautifulSoup
import smtplib
import Test

URL1 = 'https://www.emag.bg/smartfon-samsung-galaxy-a80-dual-sim-128gb-8gb-ram-4g-phantom-black-sm-a805fzkdrom/pd/DQQG6RBBM/?X-Search-Id=84b933fee97bc938d4a7&X-Product-Id=46276278&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view'

headers1 = {"User Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price1():
    page = requests.get(URL1, headers=headers1)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find("p", class_="product-new-price").get_text().strip()
    converted_price = int(price[0] + price[2:5])

    if converted_price < 1000:
        Test.send_mail(URL1)

    print(converted_price)


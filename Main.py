import requests
from bs4 import BeautifulSoup
import smtplib
import Test
import Additional_sites
import Additional_sites2_new

URL = 'https://www.technopolis.bg/bg/Mobilni-telefoni/Smartfon-GSM-SAMSUNG-GALAXY-A80-A805F-DS-BLACK/p/574270'

headers = {"User Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find("span", class_="price-value").get_text()
    converted_price = int(price[0] + price[2:5])

    if converted_price < 1000:
        Test.send_mail(URL)

    print(converted_price)

check_price()
Additional_sites.check_price1()
Additional_sites2_new.check_price2()
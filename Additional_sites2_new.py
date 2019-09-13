
from requests_html import HTML, HTMLSession
import Test

session = HTMLSession()
URL2 = 'https://www.technomarket.bg/telefoni/samsung-galaxy-a80-silver-a805-ds-09172607'
r = session.get('https://www.technomarket.bg/telefoni/samsung-galaxy-a80-silver-a805-ds-09172607')

def check_price2():
    new = r.html
    new.render()
    sel = '<div _ngcontent-serverapp-c24="" class="product-price-standard_price" style="margin-right: 20px;">1,199.-</div>'
    price = new.find(sel, first=True).text
    converted_price = int(price[0] + price[2:5])
    if converted_price < 1500:
        Test.send_mail(URL2)

    print(converted_price)





import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Mi-Smart-Band-Waterproof-up/dp/B07WLL998K/ref=sr_1_1?keywords=mi+band+4&qid=1582457400&sr=8-1'

headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:7].replace(',', ''))

    if converted_price < 2000:
        print('success')
        send_email()

    else:
        print('wait for a few days')

    print(converted_price + 10)


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('545nodeema@gmail.com', 'ayfdrhwaqlukdgsm')
    subject = 'The price went down from Utsav'
    body = 'Check the amazon link https://www.amazon.in/Mi-Smart-Band-Waterproof-up/dp/B07WLL998K/ref=sr_1_1?keywords=mi+band+4&qid=1582457400&sr=8-1'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'utsavcoolboy2010@gmail.com',
        'utsaveshan0206@gmail.com',
        msg
    )
    print('Hey, EMAIL has been sent')
    server.quit()


check_price()

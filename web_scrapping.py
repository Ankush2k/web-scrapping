import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL="https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/dp/B073Q5R6VR/ref=sr_1_1?keywords=laptops&qid=1567944491&refinements=p_89%3AApple&rnid=3837712031&s=gateway&sr=8-1"
#URL1="https://www.flipkart.com/apple-macbook-air-core-i5-5th-gen-8-gb-128-gb-ssd-mac-os-sierra-mqd32hn-a-a1466/p/itmevcpqqhf6azn3?pid=COMEVCPQBXBDFJ8C&srno=s_1_1&otracker=search&otracker1=search&lid=LSTCOMEVCPQBXBDFJ8C4V6AHG&fm=SEARCH&iid=4b8a9f30-d996-469c-a53e-259e9fc36b0b.COMEVCPQBXBDFJ8C.SEARCH&ppt=sp&ppn=sp&ssid=ynzx47x2bk0000001567944559688&qH=312f91285e048e09"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

def check_price():                                         //to check the price
 
    page = requests.get(URL,headers=headers)
    #page1 = requests.get(URL1,headers=headers)

    soup = BeautifulSoup(page.content,"html.parser")

    price = soup.find(id="priceblock_ourprice").get_text()
    cp = int(price[2:4])

    if cp < 60:
        send_mail()
    else:
        print("mail not sent since price is high :(")

def send_mail():                                            //to send mail
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("username","password")
    
    subject = "Hey price fell down!"
    body = "check the link https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/dp/B073Q5R6VR/ref=sr_1_1?keywords=laptops&qid=1567944491&refinements=p_89%3AApple&rnid=3837712031&s=gateway&sr=8-1"
    
    msg = f"Subject : {subject}\n\n{body}"
    
    server.sendmail(
        "from:mail_id",
        "to: mail_id",
        msg
    )
    
check_price()
#while(true):
#    check_price()
#    time.sleep(60*60*24)


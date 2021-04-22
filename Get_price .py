from bs4 import BeautifulSoup
import requests
import time
import smtplib
import ssl
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM


#Create a function to get price of a cryptocurrency
def get_crypto_price(coin):
 url ="https://www.google.com/search?q="+coin+"+price"
 HTML = requests.get(url)
 Soup = BeautifulSoup(HTML.text, 'html.parser')
 text = Soup.find("div",attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
 return text


#store the email addresses for the receiver , and the sender and store the senders password
receiver  =  'patelakshat337@gmail.com'
sender =  'akshatpatel029@gmail.com'
sender_password ='akshat#1010'
def send_email (sender, receiver, sender_password, text_price):
    
    msg = MM()
    msg['subject'] = "new crypto price alert !"
    msg['from']= sender
    msg['To']= receiver
#create the HTML for the message
    HTML = """
        <html>
         <body>
            <h1>new crypto price alert !</h1>
            <h2>"""+text_price+"""
            </h2>
          </body>
        </html>
        """

#create a html MIMEText object
    MTObj = MT(HTML, "html")
#Attach the 	MIMEText object
    msg.attach(MTObj)

#create the secure socket layer (SSL) context objecy
    SSL_context = ssl.create_default_context()
#create the secure simple mail Transfer protocol (SMTP) connection
    server = smtplib.SMTP_SSL(host="smtp.gmail.com",port=465, context=SSL_context)
#login to the email
    server.login(sender, sender_password)
#send the email
    server.sendmail(sender , receiver, msg.as_string())




#create a function to send the alert
def send_alert():
    last_price = -1
    while True:
        #choose the cryptocurrency/coin
        coin = 'bitcoin'
        price = get_crypto_price(coin)
        if price != last_price:
           print(coin.capitalize()+'price: ',price)
           price_text = coin.capitalize()+' is '+price
           send_email(sender, receiver , sender_password , price_text)
           last_price = price #update the last price
           time.sleep(3)
send_alert()
   




 


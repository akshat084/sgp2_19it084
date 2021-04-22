import os
import smtplib
import imghdr
from email.message import EmailMessage

import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import time


EMAIL_ADDRESS = os.environ.get('akshatpatel029@gmail.com')
EMAIL_PASSWORD = os.environ.get('akshat#1010')

msg = EmailMessage()

yf.pdr_override() # <== that's all it takes :-)
start =dt.datetime(2021,3,2)
now = dt.datetime.now()

stock="BTT1-INR"
TargetPrice=0.567

msg['Subject'] = 'Alert on '+ stock+'!'
msg['From'] = 'akshatpatel029@gmail.com'
msg['To'] = 'patelakshat337@gmail.com'

alerted=False

while True:

	df = pdr.get_data_yahoo(stock, start, now)
	currentClose=df["Adj Close"][-1]

	condition=currentClose>TargetPrice

	if(condition and alerted==False):

		alerted=True

		message=stock +" Has activated the alert price of "+ str(TargetPrice) +\
		 "\nCurrent Price: "+ str(currentClose)

		print(message)
		msg.set_content(message)

		files=[r"D:\cedar.xlsx"]

		for file in files:
			with open(file,'rb') as f:
				file_data=f.read()
				file_name="cedar.xlsx"

				msg.add_attachment(file_data, maintype="application",
					subtype='ocetet-stream', filename=file_name)


		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		    smtp.login('akshatpatel029@gmail.com', 'akshat#1010')
		    smtp.send_message(msg)

		    print("completed")
	else:
		print("No new alerts")
	time.sleep(60)

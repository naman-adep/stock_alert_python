import streamlit as st
from yahoo_fin import stock_info
import time
import pandas as pd 
from playsound import playsound

st.title("Stock Alert Notification")
ticker = st.text_input("Enter the ticker (e.g. CIPLA.NS)")

if st.button("Get current price"):
	curr_price = int(stock_info.get_live_price(ticker))
	st.markdown("Current price of stock is " + str(curr_price))

buy_price = st.text_input("Enter Buy price")
sell_price = st.text_input("Enter Sell price")

if st.button("Set Alert"):
	st.markdown("Stock Alert Monitoring is ON")
	while True:
		curr_price = int(stock_info.get_live_price(ticker))
		if curr_price < int(buy_price):
			st.markdown("BUY BUY BUY"+": Current price is " + str(curr_price))
			playsound("audio_buy.mp3")
			break
		elif curr_price > int(sell_price):
			st.markdown("SELL SELL SELL" + ": Current price is " + str(curr_price))
			playsound("audio_sell.mp3")
			break
		time.sleep(3)
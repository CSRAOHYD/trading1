
import streamlit as st

st.title("AI-Powered Trading Bot")

symbol = st.text_input("Stock/Option Symbol", "NIFTY17FEB24600CE")
trigger_price = st.number_input("Trigger Price=", value=13.0)
quantity = st.number_input("Quantity", value=75, step=1)

if st.button("Start Trading"):
    st.success(f"Monitoring {symbol} at trigger price {trigger_price}")

if st.button("Stop Trading"):
    st.warning("Trading Stopped!")

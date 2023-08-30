!pip3 install yfinance
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import plotly.express as px


st.set_page_config(page_title='Doc', page_icon=':bar_chart:', layout='wide')

today = datetime.datetime.now()
five_years_ago = today.year - 5
jan_1 = datetime.date(five_years_ago, 1, 1)
dec_31 = datetime.date(today.year, 12, 31)

d = st.sidebar.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(five_years_ago, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)


start_df = d[0].strftime('%Y-%m-%d')
try:
    end_df = d[1].strftime('%Y-%m-%d')
except:
    pass


title = st.sidebar.text_input('enter name company')
if title != '':
    traces = []
    df_yahoo = yf.download(title,
    start=str(start_df),
    end=str(end_df),
    progress=False)
    st.dataframe(df_yahoo.style.highlight_max(axis=0))
    fig = px.line(df_yahoo, x=df_yahoo.index, y='Close', title='Lineplot')
    st.plotly_chart(fig)




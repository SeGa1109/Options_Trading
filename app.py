import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

@st.cache_data
def data_load():
    owner = "SeGa1109"
    repo = "Exponency"
    headers = {"Authorization": "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",
            "accept": "application/vnd.github.v3.raw"}
    raw_url = f"https://raw.githubusercontent.com/SeGa1109/Exponency/main/FINPRRO/Scriplist.csv"
    df = pd.read_csv(raw_url)

    return df
df = data_load()
# ldir = fr"D:\Exponency\Git\Options_DataAnalysis\Options_Plot"
# os.chdir(ldir)
# df = pd.read_csv(fr"20Jan26.csv")
st.set_page_config(layout="wide")

expiry, script, interval,dateEntry = st.columns(4)

with expiry:
    expiryVal = st.selectbox('Expiry',['20Jan26'])

with script:
    scripVal = st.selectbox('Script',df['Scrip'].unique().tolist())

with interval:
    intervalVal = st.selectbox("interval",['1m','1d'])

with dateEntry:
    dateEntryVal = st.date_input("Select Date")

if st.button("Generate"):
    if intervalVal == '1m':
        print(df.dtypes)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], dayfirst=True)
        print(type(dateEntryVal))
        print(df.dtypes)
        plotdf = df[(df['Scrip'] == scripVal) & (df['Timestamp'].dt.date == dateEntryVal)]
        if not plotdf.empty:
            plotdf = plotdf.sort_values("Timestamp")
            print(plotdf)


            fig = go.Figure(
            go.Candlestick(
                x=plotdf["Timestamp"],
                open=plotdf["Open"],
                high=plotdf["High"],
                low=plotdf["Low"],
                close=plotdf["Close"],
                increasing_line_color="green",
                decreasing_line_color="red"
            )
        )

            fig.update_layout(xaxis_rangeslider_visible=True)


            st.plotly_chart(fig, use_container_width=True)
        else:st.text("No data available")
    if intervalVal == '1d':
        

        plotdf = df[(df['Scrip'] == scripVal)]
        plotdf['Timestamp'] = pd.to_datetime(plotdf['Timestamp'], dayfirst=True)
        plotdf = plotdf.set_index('Timestamp')
        plotdf = plotdf.resample('1D').agg({
                    'Open': 'first',     # first value of the day
                    'High': 'max',       # maximum value of the day
                    'Low': 'min',        # minimum value of the day
                    'Close': 'last',     # last value of the day
                    'Volume': 'sum'      # total volume of the day
                })


        
        plotdf = plotdf.dropna()
        if not plotdf.empty:
            plotdf = plotdf.sort_values("Timestamp")
            print(plotdf)

            fig = go.Figure(
            go.Candlestick(
                x=plotdf.index,
                open=plotdf["Open"],
                high=plotdf["High"],
                low=plotdf["Low"],
                close=plotdf["Close"],
                increasing_line_color="green",
                decreasing_line_color="red"
            )
        )

            fig.update_layout(xaxis_rangeslider_visible=False)


            st.plotly_chart(fig)



import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

@st.cache_data
def data_load(expiry):
    owner = "SeGa1109"
    repo = "Exponency"
    headers = {"Authorization": "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",
            "accept": "application/vnd.github.v3.raw"}
    raw_url = f"https://raw.githubusercontent.com/SeGa1109/Options_Trading/refs/heads/main/{expiry}.csv"
    df = pd.read_csv(raw_url)

    return df
# df = data_load()
# ldir = fr"D:\Exponency\Git\Options_DataAnalysis\Options_Plot"
# os.chdir(ldir)
# df = pd.read_csv(fr"20Jan26.csv")
st.set_page_config(layout="wide")
scriplist = ['24000CE','24000PE','24050CE','24050PE','24100CE','24100PE','24150CE','24150PE','24200CE','24200PE','24250CE','24250PE','24300CE','24300PE','24350CE','24350PE','24400CE','24400PE','24450CE','24450PE','24500CE','24500PE','24550CE','24550PE','24600CE','24600PE','24650CE','24650PE','24700CE','24700PE','24750CE','24750PE','24800CE','24800PE','24850CE','24850PE','24900CE','24900PE','24950CE','24950PE','25000CE','25000PE','25050CE','25050PE','25100CE','25100PE','25150CE','25150PE','25200CE','25200PE','25250CE','25250PE','25300CE','25300PE','25350CE','25350PE','25400CE','25400PE','25450CE','25450PE','25500CE','25500PE','25550CE','25550PE','25600CE','25600PE','25650CE','25650PE','25700CE','25700PE','25750CE','25750PE','25800CE','25800PE','25850CE','25850PE','25900CE','25900PE','25950CE','25950PE','26000CE','26000PE','26050CE','26050PE','26100CE','26100PE','26150CE','26150PE','26200CE','26200PE','26250CE','26250PE','26300CE','26300PE','26350CE','26350PE','26400CE','26400PE','26450CE','26450PE','26500CE','26500PE','26550CE','26550PE','26600CE','26600PE','26650CE','26650PE','26700CE','26700PE','26750CE','26750PE','26800CE','26800PE','26850CE','26850PE','26900CE','26900PE','26950CE','26950PE','27000CE','27000PE'
]
expiry, script, interval,dateEntry = st.columns(4)

with expiry:
    expiryVal = st.selectbox('Expiry',['20Jan26','03Feb26'])

with script:
    scripVal = st.selectbox('Script',scriplist)

with interval:
    intervalVal = st.selectbox("interval",['1m','1d'])

with dateEntry:
    dateEntryVal = st.date_input("Select Date")

if st.button("Generate"):
    df = data_load(expiryVal)
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

            col1,col2,col3 = st.columns([1, 3, 1])
            
            with col2:
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


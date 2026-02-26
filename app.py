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
    raw_url = f"https://raw.githubusercontent.com/SeGa1109/Options_Trading/refs/heads/main/{expiry}.parquet"
    df = pd.read_parquet(raw_url)

    return df
# df = data_load()
# ldir = fr"D:\Exponency\Git\Options_DataAnalysis\Options_Plot"
# os.chdir(ldir)
# df = pd.read_csv(fr"20Jan26.csv")

st.set_page_config(layout="wide")
scriplist = ['21000CE','21050CE','21100CE','21150CE','21200CE','21250CE','21300CE','21350CE','21400CE','21450CE','21500CE','21550CE','21600CE','21650CE','21700CE','21750CE','21800CE','21850CE','21900CE','21950CE','22000CE','22050CE','22100CE','22150CE','22200CE','22250CE','22300CE','22350CE','22400CE','22450CE','22500CE','22550CE','22600CE','22650CE','22700CE','22750CE','22800CE','22850CE','22900CE','22950CE','23000CE','23050CE','23100CE','23150CE','23200CE','23250CE','23300CE','23350CE','23400CE','23450CE','23500CE','23550CE','23600CE','23650CE','23700CE','23750CE','23800CE','23850CE','23900CE','23950CE','24000CE','24050CE','24100CE','24150CE','24200CE','24250CE','24300CE','24350CE','24400CE','24450CE','24500CE','24550CE','24600CE','24650CE','24700CE','24750CE','24800CE','24850CE','24900CE','24950CE','25000CE','25050CE','25100CE','25150CE','25200CE','25250CE','25300CE','25350CE','25400CE','25450CE','25500CE','25550CE','25600CE','25650CE','25700CE','25750CE','25800CE','25850CE','25900CE','25950CE','26000CE','26050CE','26100CE','26150CE','26200CE','26250CE','26300CE','26350CE','26400CE','26450CE','26500CE','26550CE','26600CE','26650CE','26700CE','26750CE','26800CE','26850CE','26900CE','26950CE','27000CE','27050CE','27100CE','27150CE','27200CE','27250CE','27300CE','27350CE','27400CE','27450CE','27500CE','21000PE','21050PE','21100PE','21150PE','21200PE','21250PE','21300PE','21350PE','21400PE','21450PE','21500PE','21550PE','21600PE','21650PE','21700PE','21750PE','21800PE','21850PE','21900PE','21950PE','22000PE','22050PE','22100PE','22150PE','22200PE','22250PE','22300PE','22350PE','22400PE','22450PE','22500PE','22550PE','22600PE','22650PE','22700PE','22750PE','22800PE','22850PE','22900PE','22950PE','23000PE','23050PE','23100PE','23150PE','23200PE','23250PE','23300PE','23350PE','23400PE','23450PE','23500PE','23550PE','23600PE','23650PE','23700PE','23750PE','23800PE','23850PE','23900PE','23950PE','24000PE','24050PE','24100PE','24150PE','24200PE','24250PE','24300PE','24350PE','24400PE','24450PE','24500PE','24550PE','24600PE','24650PE','24700PE','24750PE','24800PE','24850PE','24900PE','24950PE','25000PE','25050PE','25100PE','25150PE','25200PE','25250PE','25300PE','25350PE','25400PE','25450PE','25500PE','25550PE','25600PE','25650PE','25700PE','25750PE','25800PE','25850PE','25900PE','25950PE','26000PE','26050PE','26100PE','26150PE','26200PE','26250PE','26300PE','26350PE','26400PE','26450PE','26500PE','26550PE','26600PE','26650PE','26700PE','26750PE','26800PE','26850PE','26900PE','26950PE','27000PE','27050PE','27100PE','27150PE','27200PE','27250PE','27300PE','27350PE','27400PE','27450PE','27500PE'
]
expiry, script, interval,dateEntry = st.columns(4)

with expiry:
    expiryVal = st.selectbox('Expiry',['03Oct24','10Oct24','17Oct24','24Oct24','31Oct24','07Nov24','14Nov24','21Nov24','28Nov24','05Dec24','12Dec24','19Dec24','26Dec24','02Jan25','09Jan25','16Jan25','23Jan25','30Jan25','06Feb25','13Feb25','20Feb25','27Feb25','06Mar25','13Mar25','20Mar25','27Mar25','03Apr25','09Apr25','17Apr25','24Apr25','30Apr25','08May25','15May25','22May25','29May25','05Jun25','12Jun25','19Jun25','26Jun25','03Jul25','10Jul25','17Jul25','24Jul25','31Jul25','07Aug25','14Aug25','21Aug25','28Aug25','02Sep25','09Sep25','16Sep25','23Sep25','30Sep25','07Oct25','14Oct25','20Oct25','28Oct25','04Nov25','11Nov25','18Nov25','25Nov25','02Dec25','09Dec25','16Dec25','23Dec25','30Dec25','06Jan26','13Jan26','20Jan26','27Jan26','03Feb26','10Feb26'
])

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


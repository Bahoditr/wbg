import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Add Title
st.title("Use Pygwalker In Streamlit")

# Import your data
df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")

#df = pd.read_excel("https://raw.githubusercontent.com/Bahoditr/wbg/03ec3936577188897d8a805121e397cb779f392a/raw_data.xlsx")

# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)

# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)

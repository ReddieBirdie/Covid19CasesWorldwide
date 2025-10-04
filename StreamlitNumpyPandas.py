import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
from click import confirm


def load_data():
    data = pd.read_csv("/Users/redsparrow/Downloads/covid19.csv")
    return data

def processedData(data):
    data1 = data.melt(id_vars=["Province/State","Country/Region","Lat","Long"],var_name="Date",value_name="Confirmed")
    data1["Date"]=pd.to_datetime(data1["Date"])
    return data1

def CountryPick(data):
    x = data["Country/Region"].unique()
    option = st.sidebar.selectbox("Choose a country",x)
    return option

def FilterCountry(data,choice):
    output = data[data["Country/Region"] == choice]
    return output

def twoDimPlot(data,countryInfo):
    figure = px.line(data, x="Date", y="Confirmed", title=f'Covid cases in {countryInfo}')
    st.plotly_chart(figure)

def threeDimPlot(data,countryInfo):
    figure = px.scatter_3d(data,x="Date",y="Lat",z="Long",color="Confirmed",title=f"3d plot for covid cases in {countryInfo}")
    st.plotly_chart(figure)

def main():
    #Loading the data
    st.title("Covid data visualisation app")
    raw_data = load_data()
    new_data = processedData(raw_data)
    st.sidebar.header('options')
    var = st.sidebar.checkbox("Show raw data")
    country = CountryPick(new_data)
    if var:
        st.write(raw_data)
    else:
        st.subheader("Proccessed Data")
        st.write(new_data)

    user_choice = FilterCountry(new_data,country)
    st.write(user_choice)
    if st.button("2 dimentional plot"):
        twoDimPlot(user_choice,country)
    if st.button("3 dimentional plot"):
        threeDimPlot(user_choice, country)
main()

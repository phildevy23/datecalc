import streamlit as st
import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import date

st.title('How old will i be?')

default_dob = date(1988,5,23)
future_date = date(2074,5,11)

col1, col2 = st.columns(2)

with col1:
    dob = st.date_input("Your DOB", value =default_dob, min_value = date(1900,1,1),max_value = date.today())

with col2:
    future_date = st.date_input("Future Date", value=future_date, min_value = date(1900,1,1), max_value = date(2200,1,1))

diff = relativedelta(future_date,dob)

if dob > future_date:
    st.error("Time Travel not supported, pick a future date.")
else:
    st.success(f"if you were born on {dob}, you would be {diff.years} years, {diff.months} months and {diff.days} days old on {future_date}")

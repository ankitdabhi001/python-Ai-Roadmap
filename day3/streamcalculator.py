import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

min_date = date(1900, 1, 1)
max_date = date.today()

st.subheader("enter your birth  date")
bd=st.date_input("enter your date",key="dob", min_value=min_date, max_value=max_date)

st.subheader("enter current date")
cd=st.date_input("enter your date",key="current", value=date.today(), min_value=min_date, max_value=max_date)



if bd > cd:
    st.error("❌ Birth date cannot be in the future!")
else:
    age = relativedelta(cd, bd)
    total_days = (cd - bd).days

    st.success(f"🎉 You are {age.years} years, {age.months} months, and {age.days} days old!")
    st.info(f"🧮 Total days lived: {total_days:,} days")

    st.success(f"your running year is : {age.years+1} ")
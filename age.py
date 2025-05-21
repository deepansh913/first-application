import streamlit as st
import datetime as dat

st.title("Age Calculator")
st.subheader("Made by Deepansh Asati")
n = st.text_input("Enter your name")
st.text(f"Welcome {n}")
dob = st.date_input("Select your date of birth", min_value=dat.date(1900, 1, 1), max_value=dat.date.today() )

tod = dat.date.today()  # ✅ Corrected line

# Calculate age correctly
age = tod.year - dob.year - ((tod.month, tod.day) < (dob.month, dob.day))
st.write("Your age is:", age)

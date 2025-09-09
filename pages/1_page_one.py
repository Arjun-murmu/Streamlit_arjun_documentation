import streamlit as st
import datetime

# st.markdown("### Page 2 ❄️")
st.sidebar.markdown("### Page 1 ❄️")

st.title("📄Age Calculation")
st.write("Welcome to **Page One** of the app!")

# Example content
name = st.text_input("What is your name?")

min_date = datetime.date(1900, 1, 1)
max_date = datetime.date.today()
dob = st.date_input("Enter your date of birth : ",
                    min_value = min_date,
                    max_value = max_date,
                    value = datetime.date(2003, 9, 13))
if name:
    st.success(f"Hello {name}, nice to see you on Page One! 🎉")

if dob:
    st.write(f"#### Your date of birth is : {dob}.")

#age calculation
st.write("## Your age details : ")
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
#age
age = current_year - dob.year

today = max_date
# Age calculation
year = today.year - dob.year
month = today.month - dob.month
day = today.day - dob.day

if month < 0 or (month == 0 and day < 0):
    year -= 1
    month += 12
    if day < 0:
        month -= 1
        day += 30  # approx adjustment
curr = f"🎉 Hey, you’ve survived: **{year} years, {month} months, {day} days** on planet Earth!"
# st.write(f"Ohh 😀, You are {age} years : {curr} old.")
# details = st.success(curr)
st.write(f"### {curr}")

# Fun breakdown
st.info(f"🗓️ That’s about **{year * 12 + month} months** of life experience!")
st.write(f"📆 Or around **{year * 52} weeks** (give or take a few vacations 😉).")
st.write(f"☀️ Roughly **{year * 365} days** of sunrises and sunsets.")
st.write(f"⏰ That equals **{year * 365 * 24} hours** of existence.")
st.write(f"⌛ Which is **{year * 365 * 24 * 60} minutes** of scrolling memes.")
st.write(f"💥 And a whopping **{year * 365 * 24 * 60 * 60} seconds** of breathing since birth!")

st.balloons()

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

if add_selectbox == "Email":
    st.sidebar.write("📩murmuarjun88@gmail.com")
elif add_selectbox == "Home phone":
    st.sidebar.write("☎️ 955692****")
elif add_selectbox == "Mobile phone":
    st.sidebar.write("☎️ 955692****")
else:
    st.sidebar.write("")


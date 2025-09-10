import streamlit as st
import requests

st.sidebar.markdown("### Page 4 💵")
st.title("1. Live currency convert.")
st.write("###### Welcome to live currency converter.")
user_input_amount = st.number_input("Enter the amout in INR: ", min_value= 1)
targer_user_con = st.selectbox("Convert to : ",["USD","EUR","GBP","RUB","ALL","AUD","DJF"])

if st.button("Convert"):
    url = "https://v6.exchangerate-api.com/v6/63b5d8f5132abd556cb6a84a/latest/USD"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        usd_to_inr = data["conversion_rates"]["INR"]
        rate = data["conversion_rates"][targer_user_con]
        amount_in_usd = user_input_amount / usd_to_inr
        converted = rate * amount_in_usd
        st.success(f"{user_input_amount}  INR = {converted:.4f} {targer_user_con}")
    else:
        st.error("Filed to fetch convesion rate.")


st.title("2. Live one Currency to another Converter")

url = "https://v6.exchangerate-api.com/v6/63b5d8f5132abd556cb6a84a/latest/USD"
response = requests.get(url)
all_currency = []
if response.status_code == 200:
    data = response.json()
    all_currency = list(data["conversion_rates"].keys())
else:
    print("Failed to fetch currency data.")

user_original_currency = st.selectbox("Choose the currency:", all_currency, key="orig_currency")
user_target_currency = st.selectbox("Convert to:", all_currency, key="target_currency")

# Add a unique key for number_input
user_amount = st.number_input(f"Enter the amount in {user_original_currency}:", min_value=0.01, step=0.01, format="%.2f", key="amount_input")

if st.button("Convert", key="convert_button"):
    if user_original_currency == "USD":
        rate = data["conversion_rates"][user_target_currency]
        converted_amount = rate * user_amount
    else:
        url = f"https://v6.exchangerate-api.com/v6/63b5d8f5132abd556cb6a84a/latest/{user_original_currency}"
        response = requests.get(url)

        if response.status_code == 200:
            new_data = response.json()
            rate = new_data["conversion_rates"][user_target_currency]
            converted_amount = rate * user_amount
        else:
            st.error("Failed to fetch conversion rate.")
            converted_amount = None

    if converted_amount is not None:
        st.success(f"{user_amount} {user_original_currency} = {converted_amount} {user_target_currency}")

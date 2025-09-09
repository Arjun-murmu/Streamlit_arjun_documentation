import streamlit as st
import datetime
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Arjun's Blog",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="auto"
)

# Blog title and description

st.title("Arjun's Blog")
st.write("Welcome everyone🙏! This is a simple documentation of Streamlit, built with Streamlit.")
# st.subheader("Latest Posts")
st.write("###### Post 1: Introduction to Streamlit")
st.text("Streamlit is an open-source Python library that simplifies the creation and sharing of interactive web applications," \
" particularly for data science and machine learning projects. " \
"It allows users to transform Python scripts into dynamic web apps with minimal effort, " \
"eliminating the need for extensive knowledge of web development technologies like HTML, CSS, or JavaScript.")
st.write("###### Post 2: Building Interactive Web Apps")
st.text("Stay tuned for more updates!")

#difference between st.write and st.text
st.markdown("## Difference between st.text and st.write")
st.text("In Streamlit, both st.text() and st.write() are used to display content, but they differ in their flexibility and how they render the output.")

cText,cWrite = st.columns(2)

with cText:
    st.header("st.text")
    st.write(
        "- st.text() is used to show plain text on the screen."
        "\n- It displays text in a fixed-width style, like in a terminal or code editor."
        "\n- It does not support Markdown or any special formatting."
        "\n- Mostly used to show raw output, like terminal results or log messages."
        "\n- Example: st.text('Hello, World!')"
        "\n- Output: Hello, World!"
        "\n- Note: st.text() can only show simple text, not styled or formatted content."
    )
with cWrite:
    st.header("st.write")
    st.write(
        "- st.write() is a very flexible command that can show many types of content."
        "\n- It automatically detects the type of data and displays it in the right way."
        "\n- If you give it text, it can format it using Markdown (bold, italics, headings, etc.)."
        "\n- It can also show tables, charts (Matplotlib, Altair, Plotly), errors, and more."
        "\n- Makes your app look nicer and easier to read."
        "\n- Example: st.write('Hello, **World!**')"
        "\n- Output: Hello, World! (with 'World!' in bold)"
    )


st.write("### In summary : ")
st.write(
    "- Use `st.text()` when you need to display plain, unformatted text exactly as it is.\n"
    "- Use `st.write()` for a more flexible and powerful way to display content, especially when you want to leverage Markdown formatting or display complex data types."
)

#Choose your favorite language
st.markdown("## Choose your favorite programming language")
language = st.selectbox("Select a language:", ["Python", "JavaScript", "Java", "C++", "Ruby"])
st.write(f"Wow😍 You'r favorite language is : {language}.")
st.write("This selectbox is created using `st.selectbox()` function.")

click = st.button("Click Me!")
if click:
    st.success("Button Clicked!")
    st.write("This is a simple button click event.\n" \
    "button used `st.button()` function.\n" \
    "When the button is clicked, it triggers an event that can be handled in the code.\n" \
    "\n In this case, it displays a success message using `st.success()` and writes a message to the app using st.write().")


#checkbox
if st.checkbox("Show/Hide"):
    st.write("Checkbox is checked!")
    st.write("This content is now visible because the checkbox is checked.")
    st.write("Checkbox is created using `st.checkbox()` function.")
# # This is a sample Python script.

#radio button
st.markdown("## Radio Button Example")
status = st.radio("You're happy ? :", ("Yes", "No", "Just Okay"))
if status == "Yes":
    st.success(f"{status} i am happy😀!")
elif status == "No":
    st.error(f"{status} i am not happy😔!")
else:
    st.warning(f" i am {status}😀!")
st.write("You selected:", status)
st.write("Radio buttons syntax is `st.radio()`")

#Slider
st.markdown("## Slider Example")
age = st.slider("Select your age : ", 0, 100, 21)
st.write(f"hmm🤔, Your age is : {age}.")
st.write("This slider is created using `st.slider()` function.")

#Uncontrolled Input
st.markdown("## Uncontrolled Input Example")
name = st.text_input("Enter your name : ")
st.write(f"Hello👋 {name},  Welcome to my blog!")
st.write("This text input is created using `st.text_input()` function.")

number = st.number_input("Enter your lucky number range between(1-10): ", min_value=0, max_value=10, value=7, step=1)
st.write(f"wow🤩, Your lucky number is : {number}.")
st.write("This number input is created using `st.number_input()` function.")

#Date Input
st.markdown("## Date Input Example")
min_date = datetime.date(1900, 1, 1)
max_date = datetime.date.today()
dob = st.date_input("Enter your date of birth : ",
                    min_value = min_date,
                    max_value = max_date,
                    value = datetime.date(2003, 9, 13))
st.write(f"Your date of birth is : {dob}.")
st.write("This date input is created using `st.date_input()` function.")

# #Next page link
# st.markdown("## Next Page Link")
# st.markdown("[Go to Next Page >](./page_two.py)")

#image display
st.markdown("## Image Display Example")

image = Image.open("streamlit.png")
st.image(image, caption="streamlit Picture",width=400)
st.write("This image is displayed using `st.image()` function.")

#side bar
st.sidebar.title("About")
st.sidebar.info("This is a documentation app created by Arjun using Streamlit. Explore the interactive features and learn how it works")
name = st.sidebar.text_input("Enter your name : ")
st.sidebar.write(f"Hello 👋 {name}, welcome to this page!")

food = st.sidebar.selectbox("Select your favorite food:", ["Pizza", "Burger", "Pasta", "Salad", "Sushi"])
st.sidebar.write(f"Yummy🤤 You'r favorite food is : {food}.")
st.write("Slider is created using `st.sidebar.selectbox()` function.")

st.markdown("## Expander Example")
st.markdown("### Contact Information")
with st.expander("Contact"):
    st.write("You can reach me at:")
    st.write("""- Email:murmuarjun88@gmail.com
             \n- LinkedIn: [Arjun Murmu](https://www.linkedin.com/in/arjun-murmu-b672a8260/)
             \n - GitHub: [Arjun Murmu](https://github.com/Arjun-murmu)""")
    
st.write("This contact info is inside an expander using `st.expander()` function.")

vote = st.sidebar.radio("Do you like this documentation? ", ("Yes", "No","Improve it"))

if vote == "Yes":
    st.sidebar.success("Thank you 😄! Enjoy exploring the documentation!")
elif vote == "No":
    st.sidebar.error("Oh 😔, sorry to hear that. I’ll try to make it better.")
else:
    st.sidebar.warning("Thanks for your feedback! I’ll work on improving it.")

st.warning("* Note: This is a demo documentation app for learning purposes.")

st.sidebar.write("© 2025 Arjun's Documentation")  

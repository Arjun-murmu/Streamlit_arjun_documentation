import streamlit as st

# Define the pages
# Main page content
# st.markdown("# Main page 🎈")
# st.sidebar.markdown("# Main page 🎈")


main_page = st.Page("./main.py", title="Main Page", icon="💒")
about_me = st.Page("./pages/i_am.py", title="about me", icon="👨🏻‍💼")
page_1 = st.Page("./pages/1_page_one.py", title="age calculation", icon="🎈")
page_2 = st.Page("./pages/2_page_two.py", title="data analysis", icon="🎉")
page_3 = st.Page("./pages/3_page_three.py", title="table & graph", icon="📈")
page_4 = st.Page("./pages/4_page_four.py", title="convert currency", icon="💵")

# Set up navigation
pg = st.navigation([main_page, page_1, page_2,page_3,page_4,about_me])

# Run the selected page
pg.run()

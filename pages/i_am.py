import streamlit as st

st.sidebar.markdown("### About Me 👨🏻‍💼")

# Layout with two columns
col1, col2 = st.columns([2, 1])  # 2:1 ratio

with col1:
    st.subheader("About Myself")
    st.write(
        "Hello! My name is Arjun Murmu. I am a final-year B.Tech student in Computer Science and Engineering. "
        "I am passionate about learning new technologies, coding, and building projects. "
        "I also enjoy teaching and sharing knowledge with others."
    )

    st.subheader("Skills")
    st.write("Python, C++, SQL, HTML, CSS, " \
             "Excel,PowerPoint, MS Word")

    st.subheader("Teaching")
    st.write("I also teach students from classes 4 to 10 in my extra time, helping them understand concepts clearly.")

    st.subheader("Connect with me")
    st.markdown(
        """
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arjun-murmu-b672a8260/)
        [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github&logoColor=white)](https://github.com/Arjun-murmu)
        [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter&logoColor=white)](https://twitter.com/arjunmurmu)
        [![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white)](https://www.instagram.com/arjunmurmu78/)
        [![Facebook](https://img.shields.io/badge/Facebook-1877F2?logo=facebook&logoColor=white)](https://www.facebook.com/profile.php?id=100042330407115)
        [![Gmail](https://img.shields.io/badge/Gmail-D14836?logo=gmail&logoColor=white)](mailto:murmuarjun88@gmail.com)
        """
    )

with col2:
    st.image("./arjun.jpg", caption="Arjun Murmu", width=150)

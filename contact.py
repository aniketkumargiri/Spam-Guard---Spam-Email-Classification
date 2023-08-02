import streamlit as st

# User Feedback and Model Iteration
def contact_us():
    # Contact information
    st.write('<div class="contact">If you need any assistance, please reach out to me.</div>',unsafe_allow_html=True)
    st.write("Email:  [aniket.kumar.giri2707@gmail.com](mailto:aniket.kumar.giri2707@gmail.com)")
    st.write("Phone: [+91 9123997300](tel:+919123997300)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # Social media links
    # Handling Attachments and HTML Content
    st.write('<div class="connect">Connect with me.</div>',unsafe_allow_html=True)
    st.markdown(
        """
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/aniket-giri-b51b281a5/)
        [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter)](https://twitter.com/aniket_giri27)
        [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram)](https://www.instagram.com/anikthe_27/)
        [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)](https://github.com/aniketkumargiri)
        """,
        unsafe_allow_html=True
    )

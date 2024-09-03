import streamlit as st

st.header("Ask a Question")

contact_form = """
<form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Style/style.css")
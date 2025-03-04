import streamlit as st

 # pip install streamlit
 # streamlit run first_app.py

st.header("This is a header")
st.subheader("This is a subheader")
st.write("Streamlit is cool")
"Hello World"
st.markdown("Markdown")
st.button("Click me")
st.link_button("Go to gallery", 'https://www.google.com')


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# st.markdown("""
# <style>
# .demo {
#     font-size: 32px;
#     color: #d3a1a1;
#     background-color: #75b078;
#     font-family: 'Lato', sans-serif;
#     font-weight: bold;
# }
# </style>
# """, unsafe_allow_html=True)

st.markdown('<div class="demo">Hello</div>', unsafe_allow_html=True)

st.text_input("Enter your name")
st.chat_message("assistant").write("A Text by assistant")
st.chat_message("user").write("A Text by User")
st.chat_input("Type your message here")

# st.session_state

# with st.sidebar:
#     st.header("This is the sidebar")
#     st.button("A Button?")
#     st.file_uploader("Googoo Gaagaa")


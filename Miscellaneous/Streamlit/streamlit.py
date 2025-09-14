import streamlit as st 

st.title("Hello bhai!")
st.subheader("Brewed with streamlit")
st.text("easy to learn ")
st.write("choose your paths ")

chai = st.selectbox("Your fav chai: " , ["Masala chai", "Lemon chai","chai chai "])

st.write(f"you choose  {chai} excellect chai ")
st.success("Your chai is brewed")







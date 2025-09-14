import streamlit as st 

st.title("Chai taste poll")


col1, col2 = st.columns(2)

with col1:
    st.image("https://images.pexels.com/photos/5946623/pexels-photo-5946623.jpeg",width=200)
    st.header("Masala chai")
    vote1 = st.button("Vote Masala chai ")
    

with col2:
    st.image("https://images.pexels.com/photos/3904035/pexels-photo-3904035.jpeg", width=200)
    st.header("Adrak chai ")
    vote2 = st.button("Vote Adrak chai")
    
if vote1:
    st.success("Thanks for voting masala chai ")
    
elif vote2:
    st.success("Thanks for voting Adrak chai ")

name = st.sidebar.text_input("Enter you name ")
tea = st.sidebar.selectbox("Choose Your chai", ["Masala chai", "kesar", "Adrak"])

st.write(f"welcome {name} and your {tea} chai is getting ready")

with st.expander("Showing chai making Instruction"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve Hot         
    """
    )


st.markdown('### Welcom to chai APP')





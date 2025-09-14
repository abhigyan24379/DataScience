import streamlit as st 
st.title("Chai maker App")

if st.button("Make Chai"):
    st.success("Your chai brewed ")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai ")


tea_type = st.radio("Pick you chai base: ", ["Mike", "Water","suger"])


st.write("selected base ", tea_type)
flavour = st.selectbox("choose your  favour: ", ["tulsi", "elichi", "jagri"])

sugar = st.slider("Sugar level(spoon)", 0,5,1)

st.write("selected sugar level ", sugar)
cups = st.number_input("How many cups", min_value=1, max_value=10)

name = st.text_input("Enter you Name")
if name:
    st.write(f"Welcome {name}! your chai is on the way")

dob = st.date_input("Select your date of birth")
st.write(f"your date of birth is {dob}")



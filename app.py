import streamlit as st

# Title of the web app
st.title("💰 Tip Calculator")

# Input fields (replacing input())
bill = st.number_input("How much was the total bill?", min_value=0.0, step=0.01)
tip_percent = st.slider("What percentage tip would you like to give?", 0, 100, 15)
people = st.number_input("How many people are splitting the bill?", min_value=1, step=1)

# The Logic (same as your original code)
total_tip_amount = bill * (tip_percent / 100)
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

# The Output (replacing print())
if st.button("Calculate"):
    st.divider()
    st.subheader(f"Total Bill: ${total_bill:.2f}")
    st.success(f"Each person should pay: **${bill_per_person:.2f}**")
    

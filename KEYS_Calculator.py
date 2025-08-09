import streamlit as st

st.title("DALYs Reduction Estimator")

st.header("Enter Number of Graduates")

nh = st.number_input("Physicians", min_value=0, step=1)
nr = st.number_input("Researchers", min_value=0, step=1)
np = st.number_input("Drug Developers", min_value=0, step=1)

# Coefficients
hmod = -49.74
rmod = -89.90
pmod = -35.31

# Calculations
daly_h = hmod * nh
daly_r = rmod * nr
daly_p = pmod * np
total = daly_h + daly_r + daly_p

st.header("Estimated DALYs Avoided")
st.write(f"Physicians: {daly_h:,.2f}")
st.write(f"Researchers: {daly_r:,.2f}")
st.write(f"Drug Developers: {daly_p:,.2f}")
st.subheader(f"**Total: {total:,.2f} DALYs avoided**")


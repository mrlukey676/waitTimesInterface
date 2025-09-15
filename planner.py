import streamlit as st
import requests

try:
    RIDES = requests.get("http://192.168.1.224:8000/api/get-names").json()
except:
    st.error("Failed to retrieve ride names.")

st.set_page_config(page_title="Wait Times", layout="wide")
st.title("Ride Planner")

park = st.selectbox("Select a park", ("Magic Kingdom", "Epcot", "Disney's Hollywood Studios", "Disney's Animal Kingdom"))

if park == "Magic Kingdom":
    ride1 = st.selectbox("Select a ride", (ride for ride in RIDES["names"] if ride[0:2] == "MK"))
    ride2 = st.selectbox("Select a second ride", (ride for ride in RIDES["names"] if ride[0:2] == "MK"))
    ride3 = st.selectbox("Select a third ride", (ride for ride in RIDES["names"] if ride[0:2] == "MK"))
    ride4 = st.selectbox("Select a fourth ride", (ride for ride in RIDES["names"] if ride[0:2] == "MK"))
    ride5 = st.selectbox("Select a fifth ride", (ride for ride in RIDES["names"] if ride[0:2] == "MK"))
elif park == "Epcot":
    ride1 = st.selectbox("Select a ride", (ride for ride in RIDES["names"] if ride[0:2] == "EP"))
    ride2 = st.selectbox("Select a second ride", (ride for ride in RIDES["names"] if ride[0:2] == "EP"))
    ride3 = st.selectbox("Select a third ride", (ride for ride in RIDES["names"] if ride[0:2] == "EP"))
    ride4 = st.selectbox("Select a fourth ride", (ride for ride in RIDES["names"] if ride[0:2] == "EP"))
    ride5 = st.selectbox("Select a fifth ride", (ride for ride in RIDES["names"] if ride[0:2] == "EP"))
elif park == "Disney's Hollywood Studios":
    ride1 = st.selectbox("Select a ride", (ride for ride in RIDES["names"] if ride[0:2] == "HS"))
    ride2 = st.selectbox("Select a second ride", (ride for ride in RIDES["names"] if ride[0:2] == "HS"))
    ride3 = st.selectbox("Select a third ride", (ride for ride in RIDES["names"] if ride[0:2] == "HS"))
    ride4 = st.selectbox("Select a fourth ride", (ride for ride in RIDES["names"] if ride[0:2] == "HS"))
    ride5 = st.selectbox("Select a fifth ride", (ride for ride in RIDES["names"] if ride[0:2] == "HS"))
elif park == "Disney's Animal Kingdom":
    ride1 = st.selectbox("Select a ride", (ride for ride in RIDES["names"] if ride[0:2] == "AK"))
    ride2 = st.selectbox("Select a second ride", (ride for ride in RIDES["names"] if ride[0:2] == "AK"))
    ride3 = st.selectbox("Select a third ride", (ride for ride in RIDES["names"] if ride[0:2] == "AK"))
    ride4 = st.selectbox("Select a fourth ride", (ride for ride in RIDES["names"] if ride[0:2] == "AK"))
    ride5 = st.selectbox("Select a fifth ride", (ride for ride in RIDES["names"] if ride[0:2] == "AK"))

submitPlanBtn = st.button("Get Ride Plan")

if submitPlanBtn:
    st.markdown("Generating your ride plan. This may take up to 20 seconds...")
    response = requests.get(f"http://192.168.1.224:8000/api/plan?ride1={ride1}&ride2={ride2}&ride3={ride3}&ride4={ride4}&ride5={ride5}")
    if response.status_code == 200:
        plan = response.json()
        st.write("Your Ride Plan:")
        for ride in plan["plannedRides"]:
            st.markdown(f"**{ride["ridename"]}** - {ride["time"]}")
    else:
        st.error("Failed to retrieve ride plan.")

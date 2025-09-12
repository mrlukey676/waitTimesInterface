import streamlit as st
import requests

try:
    RIDES = requests.get("http://192.168.1.224:8000/api/get-names").json()
except:
    st.error("Failed to retrieve ride names.")

st.set_page_config(page_title="Wait Times", layout="wide")
st.title("Wait Times")

st.markdown("Interact with the Lukey Travel Wait Times API, [powered by Queue-Times.com](https://queue-times.com/)")

park = st.selectbox("Select a park", ("Magic Kingdom", "Epcot", "Disney's Hollywood Studios", "Disney's Animal Kingdom"))

if park == "Magic Kingdom":
    ridesSelect = st.selectbox("Select a ride", (ride for ride in RIDES["names"] if ride[0:2] == "MK"))
elif park == "Epcot":
    ridesSelect = st.selectbox("Select a ride", (ride for ride in RIDES["names"] if ride[0:2] == "EP"))
elif park == "Disney's Hollywood Studios":
    ridesSelect = st.selectbox("Select a ride", (ride for ride in RIDES["names"] if ride[0:2] == "HS"))
elif park == "Disney's Animal Kingdom":
    ridesSelect = st.selectbox("Select a ride", (ride for ride in RIDES["names"] if ride[0:2] == "AK"))

submitAvgWaitBtn = st.button("Get Average Wait Time")
submitBestTimeBtn = st.button("Get Best Time To Ride")
submitAvgDayWaits = st.button("Get Average Waits per day")
if submitAvgWaitBtn:
    response = requests.get(f"http://192.168.1.224:8000/api/get-avg-wait?ridename={ridesSelect}")
    if response.status_code == 200:
        wait = response.json()
        st.write(wait["averageWait"])
    else:
        st.error(f"An error occured!: {response.text}")

if submitBestTimeBtn:
    response = requests.get(f"http://192.168.1.224:8000/api/get-best-time?ridename={ridesSelect}")
    if response.status_code == 200:
        bestWorstTimes = response.json()
        st.markdown(f"The best times to ride this ride are: {', '.join(slot for slot in bestWorstTimes['bestTimes'])}.")
        st.markdown(f"You should avoid this ride around: {', '.join(slot for slot in bestWorstTimes['worstTimes'])}.")
    else:
        st.error(f"An error occured!: {response.text}")

if submitAvgDayWaits:
    response = requests.get(f"http://192.168.1.224:8000/api/get-avg-wait-per-day?ridename={ridesSelect}")
    if response.status_code == 200:
        avgDayWaits = response.json()
        for day in avgDayWaits["averageWaits"]:
            st.markdown(f"**{day}**: {avgDayWaits['averageWaits'][day]} minutes")
    else:
        st.error(f"An error occured!: {response.text}")
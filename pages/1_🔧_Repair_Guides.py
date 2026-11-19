# pages/1_🔧_Repair_Guides.py
import streamlit as st
from device_types import device_type_selector
from guides_data import GENERAL_GUIDES

st.title("🔧 Repair")
st.write("Choose your device type, then the problem you're having.")

device_type = device_type_selector("repair")

# Only show problems that apply to the chosen device type
problems = [
    name for name, guide in GENERAL_GUIDES.items()
    if device_type in guide["categories"]
]

if not problems:
    st.info(f"We don't have repair guides for {device_type} devices yet. Try a different device type.")
    st.stop()

problem = st.selectbox("What's the problem?", problems)
guide = GENERAL_GUIDES[problem]

st.subheader(problem)
st.write(f"**Symptoms:** {guide['symptoms']}")

st.markdown("**Steps:**")
for step_number, step in enumerate(guide["steps"], start=1):
    st.write(f"{step_number}. {step}")

st.warning(f"⚠️ Safety: {guide['safety']}")

st.markdown("**Video guides**")

# Only show videos that have a link added
videos = [video for video in guide.get("videos", []) if video.get("url")]

if videos:
    for video in videos:
        st.link_button(video["title"], video["url"])
        st.caption(f"Source: {video['source']}")
else:
    st.caption("No video links have been added for this problem yet.")

st.caption(
    "Video links open on the creator's site. Videos can change or be removed, "
    "so follow the steps above and stop if anything looks unsafe."
)
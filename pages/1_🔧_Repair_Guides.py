# pages/1_🔧_Repair_Guides.py
import streamlit as st
from device_types import device_type_selector
from did_you_know import show_did_you_know
from guides_data import GENERAL_GUIDES

st.title("🔧 Repair")
st.write("Choose your device type, then the problem you're having.")

# Side by side on laptops, stacked on phones
type_col, problem_col = st.columns(2)

with type_col:
    device_type = device_type_selector("repair")

# Only show problems that apply to the chosen device type
problems = [
    name for name, guide in GENERAL_GUIDES.items()
    if device_type in guide["categories"]
]

with problem_col:
    if problems:
        problem = st.selectbox("What's the problem?", problems)

# Tip for the chosen device type ("Other" has none)
show_did_you_know(device_type)

if not problems:
    st.info(f"We don't have repair guides for {device_type} devices yet. Try a different device type.")
    st.stop()

guide = GENERAL_GUIDES[problem]

with st.container(border=True):
    st.subheader(problem)
    st.write(f"**Symptoms:** {guide['symptoms']}")

    st.markdown("**Steps:**")
    st.markdown(
        "\n".join(
            f"{step_number}. {step}"
            for step_number, step in enumerate(guide["steps"], start=1)
        )
    )

    st.warning(f"⚠️ Safety: {guide['safety']}")

st.markdown("**Video guides**")

# Only show videos that have a link added
videos = [video for video in guide.get("videos", []) if video.get("url")]

if videos:
    # One column per video on laptops; they stack on phones
    video_cols = st.columns(len(videos))
    for col, video in zip(video_cols, videos):
        with col:
            st.link_button(video["title"], video["url"])
            st.caption(f"Source: {video['source']}")
else:
    st.caption("No video links have been added for this problem yet.")

st.caption(
    "Video links open on the creator's site. Videos can change or be removed, "
    "so follow the steps above and stop if anything looks unsafe."
)

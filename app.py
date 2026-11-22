# app.py
from pathlib import Path

import streamlit as st

# Must be the first Streamlit command in the app
st.set_page_config(page_title="E-ways", page_icon="♻️", layout="wide")


def load_css():
    """Add the styles in style.css to every page. Skipped if the file is missing."""
    css_file = Path(__file__).parent / "style.css"
    if css_file.exists():
        st.markdown(f"<style>{css_file.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


load_css()


def home():
    st.title("E-ways ♻️")
    st.write(
        "Repair what you can, reuse what still works, and reduce the waste you make. "
        "Use the sidebar to get started."
    )

    # One card per section. On phones the columns stack into a single column.
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.subheader("🔧 Repair")
            st.write("Search step-by-step troubleshooting guides for common devices.")
            st.page_link(repair_page, label="Go to Repair", icon="➡️")

    with col2:
        with st.container(border=True):
            st.subheader("🛒 Reuse")
            st.write("Buy or sell old electronics with other students.")
            st.page_link(reuse_page, label="Go to Reuse", icon="➡️")

    with col3:
        with st.container(border=True):
            st.subheader("♻️ Reduce")
            st.write("Find out whether a device should be repaired, resold, or recycled.")
            st.page_link(reduce_page, label="Go to Reduce", icon="➡️")


# Define each page once so we can use it for both navigation and links
home_page = st.Page(home, title="Home", icon="🏠", default=True)
repair_page = st.Page("pages/1_🔧_Repair_Guides.py", title="Repair", icon="🔧")
reuse_page = st.Page("pages/2_🛒_Community_Board.py", title="Reuse", icon="🛒")
reduce_page = st.Page("pages/3_♻️_Disposal.py", title="Reduce", icon="♻️")

# Hide the default links so we control where they appear
pg = st.navigation(
    [home_page, repair_page, reuse_page, reduce_page,],
    position="hidden",
)

# Sidebar content, in the order it should appear
st.sidebar.title("E-ways")
st.sidebar.page_link(home_page, label="Home", icon="🏠")
st.sidebar.page_link(repair_page, label="Repair", icon="🔧")
st.sidebar.page_link(reuse_page, label="Reuse", icon="🛒")
st.sidebar.page_link(reduce_page, label="Reduce", icon="♻️")

pg.run()

# app.py
import streamlit as st

# Must be the first Streamlit command in the app
st.set_page_config(page_title="E-ways", page_icon="♻️", layout="wide")


def home():
    st.title("E-ways ♻️")
    st.write(
        "Repair what you can, reuse what still works, and reduce the waste you make. "
        "Use the sidebar to get started."
    )

    col1, col2, col3 = st.columns(3)
    col1.subheader("Repair")
    col1.write("Search step-by-step troubleshooting guides for common devices.")

    col2.subheader("Reuse")
    col2.write("Buy or sell old electronics with other students.")

    col3.subheader("Reduce")
    col3.write("Find out whether a device should be repaired, resold, or recycled.")


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
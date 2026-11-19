# device_types.py
# Shared device categories and selector for the Repair, Reuse, and Reduce pages.

import streamlit as st

# These match the categories used by the Objective 2 calculator
DEVICE_TYPES = ["Phone", "Tablet", "Laptop", "Microcontroller", "Other"]

# Session key that stores the choice, so it carries across pages
SESSION_KEY = "device_type"


def device_type_selector(page_key):
    """
    Show the device type dropdown for one page and return the chosen type.
    page_key must be different on each page so Streamlit can tell the widgets apart.
    """
    current = st.session_state.get(SESSION_KEY, DEVICE_TYPES[0])
    if current not in DEVICE_TYPES:
        current = DEVICE_TYPES[0]

    choice = st.selectbox(
        "Device type",
        DEVICE_TYPES,
        index=DEVICE_TYPES.index(current),
        key=f"device_type_{page_key}",
    )

    # Remember the choice so the other pages start with the same device type
    st.session_state[SESSION_KEY] = choice
    return choice
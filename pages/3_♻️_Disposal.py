# pages/3_♻️_Disposal.py
import streamlit as st
from device_types import device_type_selector

st.title("♻️ Reduce")
st.write("Choose your device type, then answer a few questions to get a recommendation.")

device_type = device_type_selector("reduce")

# Device-specific advice shown with every recommendation
DEVICE_NOTES = {
    "Phone": "Phones contain lithium batteries. Never puncture or charge a swollen battery.",
    "Tablet": "Tablets contain large lithium-polymer batteries. Never puncture or charge a swollen battery.",
    "Laptop": "Laptops are heavy e-waste. Remove a damaged battery before recycling, and bring the device to an e-waste drop-off.",
    "Microcontroller": "Remove reusable parts such as headers and sensors before recycling the board.",
    "Other": "Check the device for batteries before you throw it away.",
}


def get_recommendation(device_type, powers_on, damaged, swollen, repair_cheap):
    """Return (style, title, message, note) based on the device type and answers."""
    note = DEVICE_NOTES.get(device_type, "")

    if swollen:
        return (
            "error",
            "Recycle immediately at a battery-safe drop-off.",
            "A swollen lithium battery is a fire risk. Keep the device away from flammable materials and do not charge it.",
            note,
        )

    if powers_on == "No" and damaged == "Yes":
        return (
            "error",
            "Recycle it.",
            "The device is probably beyond an easy repair. Use it for parts if you can, then recycle the rest.",
            note,
        )

    if powers_on == "Yes" and repair_cheap == "Yes":
        return (
            "success",
            "Repair it.",
            "A repair is cost-effective and keeps the device in use. Check the Repair page for guides.",
            note,
        )

    if powers_on == "Yes" and repair_cheap == "No":
        return (
            "info",
            "Sell it as-is on the Reuse board.",
            "The repair costs more than the device is worth to most buyers. Someone else may repair it or use it for parts.",
            note,
        )

    return (
        "warning",
        "Get a quote first.",
        "Check the repair price at a local shop or look up the part price online, then come back to this page.",
        note,
    )


powers_on = st.radio("Does the device power on?", ["Yes", "No"], horizontal=True)
physically_damaged = st.radio(
    "Is the device physically damaged (cracks, water damage, swelling)?",
    ["No", "Yes"],
    horizontal=True,
)
has_battery_swelling = st.checkbox("The battery is swollen or the device is hot when charging")
repair_cheap = st.radio(
    "Is the repair cheaper than 50% of the price of a similar used device?",
    ["Yes", "No", "Not sure"],
    horizontal=True,
)
has_personal_data = st.checkbox("The device still contains personal data I have not wiped")

st.markdown("---")

if st.button("Get recommendation", type="primary"):
    style, title, message, note = get_recommendation(
        device_type,
        powers_on,
        physically_damaged,
        has_battery_swelling,
        repair_cheap,
    )

    st.subheader("Recommendation")
    show = {
        "error": st.error,
        "success": st.success,
        "info": st.info,
        "warning": st.warning,
    }[style]
    show(f"**{title}**")
    st.write(message)

    if note:
        st.caption(f"{device_type}: {note}")

    if has_personal_data:
        st.warning(
            "🔐 **Before you sell, recycle, or donate:** wipe all personal data, "
            "sign out of accounts, and remove any SIM card or memory card."
        )
# pages/3_♻️_Disposal.py
import html

import pandas as pd
import streamlit as st
from device_types import device_type_selector
from ewaste_locations import (
    LOCATIONS,
    MAP_CENTER,
    MAP_ZOOM,
    STATUS_INFO,
    directions_url,
    status_label,
)

# The map needs folium and streamlit-folium (see requirements.txt).
# If they are not installed yet, the page falls back to Streamlit's built-in map.
try:
    import folium
    from streamlit_folium import st_folium
    FOLIUM_AVAILABLE = True
except ImportError:
    FOLIUM_AVAILABLE = False

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

    if style == "error":
        st.info("📍 Scroll down to find e-waste drop-off points in Batangas City.")


# ======================================================================
# 📍 E-WASTE DROP-OFF LOCATIONS IN BATANGAS CITY
# ======================================================================

def popup_html(location):
    """Build the text shown when a map marker is clicked."""
    info = STATUS_INFO[location["status"]]
    e = html.escape
    pin_note = " (approximate pin)" if location.get("coords_approximate") else ""
    return f"""
    <div style="font-family: sans-serif; font-size: 13px; width: 260px;">
        <div style="font-weight: 700; font-size: 14px; margin-bottom: 4px;">{e(location['name'])}</div>
        <div style="display:inline-block; background:{info['hex']}; color:#fff; border-radius:10px;
                    padding:1px 8px; font-size:11px; margin-bottom:6px;">{e(info['label'])}</div>
        <div><b>Address:</b> {e(location['address'])}{pin_note}</div>
        <div><b>Type:</b> {e(location['type'])}</div>
        <div><b>Accepted e-waste:</b> {e(location['accepted'])}</div>
        <div><b>Contact:</b> {e(location['contact'])}</div>
        <div><b>Hours:</b> {e(location['hours'])}</div>
        <div style="margin-top:4px; color:#555;"><i>{e(location['notes'])}</i></div>
        <div style="margin-top:6px;">
            <a href="{e(directions_url(location))}" target="_blank" rel="noopener">🧭 Get directions</a>
            &nbsp;·&nbsp;
            <a href="{e(location['source_url'])}" target="_blank" rel="noopener">Source</a>
        </div>
    </div>
    """


def build_folium_map(locations):
    """Create the interactive Folium map centered on Batangas City."""
    fmap = folium.Map(location=MAP_CENTER, zoom_start=MAP_ZOOM, tiles="OpenStreetMap", control_scale=True)
    for location in locations:
        info = STATUS_INFO[location["status"]]
        folium.Marker(
            location=[location["lat"], location["lon"]],
            tooltip=f"{location['name']} — {info['short']}",
            popup=folium.Popup(popup_html(location), max_width=300),
            icon=folium.Icon(color=info["color"], icon=info["icon"]),
        ).add_to(fmap)
    return fmap


st.markdown("---")
st.header("📍 E-Waste Drop-Off Locations in Batangas City")
st.write(
    "Use this map to find where you can bring unwanted electronics so they can be "
    "collected by authorized e-waste handlers. Click a marker for details and directions."
)

# Legend
legend_cols = st.columns(len(STATUS_INFO))
for col, (key, info) in zip(legend_cols, STATUS_INFO.items()):
    count = sum(1 for loc in LOCATIONS if loc["status"] == key)
    col.markdown(
        f"<span style='display:inline-block;width:12px;height:12px;border-radius:50%;"
        f"background:{info['hex']};margin-right:6px;'></span>"
        f"**{info['label']}** ({count})",
        unsafe_allow_html=True,
    )

status_filter = st.multiselect(
    "Show on map",
    options=list(STATUS_INFO.keys()),
    default=list(STATUS_INFO.keys()),
    format_func=lambda key: STATUS_INFO[key]["short"],
)
shown_locations = [loc for loc in LOCATIONS if loc["status"] in status_filter]

if not shown_locations:
    st.info("Pick at least one category to show on the map.")
elif FOLIUM_AVAILABLE:
    # returned_objects=[] stops the page from reloading when the map is clicked,
    # so the recommendation above stays on screen.
    st_folium(
        build_folium_map(shown_locations),
        height=460,
        use_container_width=True,
        returned_objects=[],
        key="batangas_ewaste_map",
    )
else:
    st.warning(
        "The interactive map needs two extra packages. Run "
        "`pip install -r requirements.txt`, then restart the app. "
        "A simple map is shown for now."
    )
    st.map(
        pd.DataFrame(
            {
                "lat": [loc["lat"] for loc in shown_locations],
                "lon": [loc["lon"] for loc in shown_locations],
                "color": [STATUS_INFO[loc["status"]]["hex"] for loc in shown_locations],
            }
        ),
        latitude="lat",
        longitude="lon",
        color="color",
        size=60,
        zoom=11,
    )

st.caption(
    "⚠️ Orange markers are proposed points for demonstration only — they do not accept "
    "e-waste yet. Pins marked approximate show the general area; the directions link "
    "searches Google Maps by place name. Always call ahead before bringing devices."
)

# ---------- Directory table ----------
st.subheader("🗂️ Drop-Off Point Directory")
directory = pd.DataFrame(
    [
        {
            "Location": loc["name"],
            "Status": STATUS_INFO[loc["status"]]["short"],
            "Accepted E-Waste": loc["accepted"] if loc["status"] == "verified" else (
                "Not a drop-off" if loc["status"] == "info_point" else "To be confirmed"
            ),
            "Address": loc["address"],
            "Directions": directions_url(loc),
            "Source": loc["source_url"],
        }
        for loc in LOCATIONS
    ]
)
st.dataframe(
    directory,
    hide_index=True,
    column_config={
        "Directions": st.column_config.LinkColumn("Directions", display_text="View Map"),
        "Source": st.column_config.LinkColumn("Source", display_text="Source"),
        "Accepted E-Waste": st.column_config.TextColumn("Accepted E-Waste", width="large"),
    },
)
st.caption("To add or update a location, edit the list in `ewaste_locations.py`.")

# ======================================================================
# ♻️ HOW E-WASTE COLLECTION WORKS
# ======================================================================
st.markdown("---")
st.header("♻️ How E-Waste Collection Works")

WORKFLOW = [
    ("1️⃣", "Select a device", "Identify the electronic device you want to dispose of, and check above whether it can still be repaired or resold."),
    ("2️⃣", "Find a drop-off point", "Check the map for a location that is verified and accepts your type of device."),
    ("3️⃣", "Prepare the device", "Remove personal data, SIM and memory cards, and follow the battery safety tips below."),
    ("4️⃣", "Drop off the device", "Bring it only to a confirmed, operational collection point during its open hours."),
    ("5️⃣", "Authorized collection", "An accredited e-waste collector picks up the collected devices for proper treatment and recycling."),
]

workflow_cols = st.columns(len(WORKFLOW))
for col, (number, title, text) in zip(workflow_cols, WORKFLOW):
    with col:
        with st.container(border=True):
            st.markdown(f"### {number}")
            st.markdown(f"**{title}**")
            st.caption(text)

st.info(
    "**About step 5:** Only the SM City Batangas bin is listed as a drop-off. SM states that "
    "collected items go to an accredited transporter and treater. The BSU points are proposals "
    "only. No collection partner has been arranged for them, and E-ways does not schedule pick-ups."
)

# ======================================================================
# SAFETY AND RESPONSIBLE DISPOSAL
# ======================================================================
st.markdown("---")
st.header("🛡️ Safety and Responsible Disposal")

safety_left, safety_right = st.columns(2)
with safety_left:
    with st.container(border=True):
        st.markdown("**🔐 Protect your data**")
        st.markdown(
            "- Back up your files, then do a full factory reset.\n"
            "- Sign out of all accounts (Apple ID, Google, social media).\n"
            "- Remove SIM cards and memory cards.\n"
        )
    with st.container(border=True):
        st.markdown("**🗑️ Dispose properly**")
        st.markdown(
            "- Never put electronics in regular household trash.\n"
            "- Call ahead to confirm the collection point accepts your device.\n"
            "- Use authorized collectors for hazardous electronic waste.\n"
        )
with safety_right:
    with st.container(border=True):
        st.markdown("**🔋 Handle lithium batteries safely**")
        st.markdown(
            "- Do not puncture, bend, crush, or heat a battery.\n"
            "- Tape over battery terminals before drop-off.\n"
            "- Keep batteries dry and away from metal objects.\n"
        )
    st.error(
        "**Swollen, leaking, or overheating battery?** Do not charge or transport it on your own. "
        "Place the device on a non-flammable surface away from anything that can burn, and contact "
        "a hazardous-waste handler or your barangay / City ENRO for instructions first."
    )

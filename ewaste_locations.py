# ewaste_locations.py
# Location data for the Batangas City e-waste map on the Reduce page.
#
# HOW TO UPDATE
#   Copy one dictionary in LOCATIONS, change the values, and save.
#   "status" must be one of the keys in STATUS_INFO below.
#
# HONESTY RULES (please keep these)
#   - Use "verified" ONLY when an official source (the program operator,
#     the LGU, or DENR-EMB) publicly lists the place as an e-waste drop-off.
#     Put that source in "source" and "source_url".
#   - Use "info_point" for offices that can give advice but are not drop-offs.
#   - Use "proposed" for any idea that is not running yet. Never list a
#     proposed point as accepting e-waste.
#   - Set "coords_approximate" to True unless you have checked the exact
#     pin on a map yourself.
#
# Research notes (checked November 2026):
#   - SM Supermalls lists an Electronic Waste Collection (EWC) bin at
#     SM City Batangas, 2F Cyberzone, in front of PowerMac Center. SM says
#     collected items go to an accredited transporter and treater.
#     https://www.smsupermalls.com/smcares/press-releases/sm-supermalls-rolls-out-sm-electronic-waste-collection-program
#   - No DENR-EMB accredited e-waste TSD facility open to the public inside
#     Batangas City was found. DENR advises households to store e-waste and
#     contact their barangay, which coordinates with the EMB regional office.
#   - The two BSU points are proposals only. Neither campus has agreed to host
#     a collection point yet, and coordinates come from Google Places listings.

# Center of Batangas City (PhilAtlas city coordinates)
MAP_CENTER = (13.7561, 121.0577)
MAP_ZOOM = 12

STATUS_INFO = {
    "verified": {
        "label": "Verified Drop-Off (publicly listed)",
        "short": "Verified",
        "color": "green",       # folium marker color
        "hex": "#2e7d32",       # used in the legend and fallback map
        "icon": "ok-sign",
    },
    "info_point": {
        "label": "Information Point — Not a Drop-Off",
        "short": "Info only",
        "color": "blue",
        "hex": "#1565c0",
        "icon": "info-sign",
    },
    "proposed": {
        "label": "Proposed Drop-Off Point — Not Yet Operational",
        "short": "Proposed",
        "color": "orange",
        "hex": "#ef6c00",
        "icon": "time",
    },
}

LOCATIONS = [
    {
        "name": "SM City Batangas – SM E-Waste Collection Bin",
        "address": "2nd Floor, Cyberzone area (in front of PowerMac Center), SM City Batangas, "
                   "Pallocan West, Batangas City, Batangas 4200",
        "type": "Mall drop-off bin (SM Electronic Waste Collection Program)",
        "status": "verified",
        "accepted": "Old or broken mobile phones, chargers, power cords, computer wiring, "
                    "commercial batteries, ink and toner cartridges, small gadgets "
                    "(keyboards, calculators, power banks, earphones). "
                    "Larger items: coordinate with mall administration.",
        "contact": "SM City Batangas mall administration / customer service desk",
        "hours": "Mall hours",
        "source": "SM Supermalls – Electronic Waste Collection Program",
        "source_url": "https://www.smsupermalls.com/environmental-programs-on-solid-waste-management-electronic-waste-collection",
        "lat": 13.7550,
        "lon": 121.0690,
        "coords_approximate": True,
        "directions_query": "SM City Batangas",
        "notes": "Listed by SM as an e-waste drop-off. Ask the information desk to confirm "
                 "the bin is still in place before your trip.",
    },
    {
        "name": "Batangas City Hall Complex – City ENRO (ask for guidance)",
        "address": "Batangas City Hall Complex, P. Burgos Street, Barangay 17, "
                   "Batangas City, Batangas 4200",
        "type": "City government office (Environment and Natural Resources Office)",
        "status": "info_point",
        "accepted": "Not a drop-off. Ask about scheduled e-waste collection drives "
                    "and how to surrender hazardous waste.",
        "contact": "Mayor's Action Center: (043) 723-1511",
        "hours": "Office hours",
        "source": "Batangas City Government website",
        "source_url": "https://batangascity.gov.ph/web/physical-geographical-aspects-2",
        "lat": 13.7559,
        "lon": 121.0597,
        "coords_approximate": True,
        "directions_query": "Batangas City Hall, P. Burgos Street, Batangas City",
        "notes": "DENR advises residents to keep e-waste at home and contact their barangay "
                 "or the local environment office, which coordinates with DENR-EMB.",
    },
    {
        "name": "BSU Pablo Borbon Main Campus – Proposed E-Waste Collection Point",
        "address": "12 Rizal Avenue, Poblacion, Batangas City, Batangas 4200",
        "type": "University campus (proposed e-waste collection point)",
        "status": "proposed",
        "accepted": "To be confirmed",
        "contact": "Not yet assigned (university administration to be contacted)",
        "hours": "Not operational",
        "source": "Google Maps listing: Batangas State University Pablo Borbon Main Campus",
        "source_url": "https://www.google.com/maps/search/?api=1&query=Batangas+State+University+Pablo+Borbon+Main&query_place_id=ChIJT-mKLmsFvTMRGgpwX-eldyQ",
        "lat": 13.7552,
        "lon": 121.0529,
        "coords_approximate": True,
        "directions_query": "Batangas State University Pablo Borbon Main Campus, Rizal Avenue, Batangas City",
        "notes": "Proposal only. The university has not agreed to host a collection point, "
                 "so do not bring devices here. Needs written approval from BSU before it can be listed as verified.",
    },
    {
        "name": "BSU Alangilan Campus – Proposed E-Waste Collection Point",
        "address": "Barangay Alangilan, Batangas City, Batangas 4200",
        "type": "University campus (proposed e-waste collection point)",
        "status": "proposed",
        "accepted": "To be confirmed",
        "contact": "Not yet assigned (university administration to be contacted)",
        "hours": "Not operational",
        "source": "Google Maps listing: Batangas State University Alangilan Campus",
        "source_url": "https://www.google.com/maps/search/?api=1&query=Batangas+State+University+Alangilan+Campus&query_place_id=ChIJAQAAAPEPvTMRHyGfViw8VW4",
        "lat": 13.7841,
        "lon": 121.0744,
        "coords_approximate": True,
        "directions_query": "Batangas State University Alangilan Campus, Batangas City",
        "notes": "Proposal only. The university has not agreed to host a collection point, "
                 "so do not bring devices here. Needs written approval from BSU before it can be listed as verified.",
    },
]


def directions_url(location):
    """
    Google Maps directions link.
    Uses exact coordinates when they were checked; otherwise searches by
    place name, which is more reliable than an approximate pin.
    """
    from urllib.parse import quote_plus

    if location.get("coords_approximate", True):
        destination = quote_plus(location["directions_query"])
    else:
        destination = f"{location['lat']},{location['lon']}"
    return f"https://www.google.com/maps/dir/?api=1&destination={destination}"


def status_label(location):
    return STATUS_INFO[location["status"]]["label"]
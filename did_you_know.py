# did_you_know.py
# "Did you know" tips shown on the Repair and Reuse pages.
#
# HOW IT WORKS
#   DID_YOU_KNOW is keyed by the device types in device_types.py.
#   "Other" has no entry on purpose, so no tip is shown for it.
#   The text shown in the app has no citations. The sources for each entry
#   are kept in the comment above it so the report can reference them.
#   Sources were matched to bullets by topic. Check them against the paper.

import streamlit as st

DID_YOU_KNOW = {
    # CELLPHONE
    # Sources:
    #   Bullet 1: Malmodin, J., Lövehagen, N., Bergmark, P., & Lundén, D. (2023).
    #             Renewable and Sustainable Energy Reviews, 183, 113422.
    #             CHECK: article 113422 is listed as Lövehagen, N., Malmodin, J.,
    #             Bergmark, P., & Matinfar, S. (2023), "Assessing embodied carbon
    #             emissions of communication user devices by combining approaches".
    #   Bullet 2: Bovea, M. D., Ibáñez-Forés, V., & Pérez-Belis, V. (2020).
    #             Waste Management, 102, 265–276.
    #             CHECK: their repair vs. replacement LCA paper is listed in the
    #             Journal of Environmental Management, 254, 109679 (2020).
    #   Bullet 3: Baldé, C. P., et al. (2024). The Global E-waste Monitor 2024. ITU and UNITAR.
    "Phone": [
        "Manufacturing a single smartphone generates approximately 50 kg CO₂e in embodied "
        "carbon emissions before the device ever reaches the end user.",
        "Repairing and reusing broken electronics before the end of their lifespan generally "
        "proves environmentally superior to replacement, preventing redundant production runs.",
        "Global e-waste is rising five times faster than documented recycling—reaching a record "
        "62 million tonnes in 2022—while squandering billions of dollars in strategically valuable "
        "resources when devices are dumped instead of properly recycled.",
    ],

    # TABLET
    # Sources:
    #   Bullet 1: Malmodin, J., Lövehagen, N., Bergmark, P., & Lundén, D. (2023).
    #             Renewable and Sustainable Energy Reviews, 183, 113422. (See CHECK under Phone.)
    #   Bullet 2: Bovea, M. D., Ibáñez-Forés, V., & Pérez-Belis, V. (2020).
    #             Waste Management, 102, 265–276. (See CHECK under Phone.)
    #             Baldé, C. P., et al. (2024). The Global E-waste Monitor 2024. ITU and UNITAR.
    "Tablet": [
        "Tablets carry double the embodied carbon footprint of a smartphone (100 kg CO₂e vs. "
        "50 kg CO₂e), driven by larger display assemblies and higher-capacity components.",
        "Extending a tablet's active life through component repair or secondhand resale "
        "outperforms replacement from a life cycle assessment standpoint and reduces the volume "
        "of discarded electronics contributing to the projected 82 million tonnes of global "
        "e-waste by 2030.",
    ],

    # LAPTOP
    # Sources:
    #   Bullet 1: Malmodin, J., Lövehagen, N., Bergmark, P., & Lundén, D. (2023).
    #             Renewable and Sustainable Energy Reviews, 183, 113422. (See CHECK under Phone.)
    #   Bullet 2: Bovea, M. D., Ibáñez-Forés, V., & Pérez-Belis, V. (2020).
    #             Waste Management, 102, 265–276. (See CHECK under Phone.)
    #             Baldé, C. P., et al. (2024). The Global E-waste Monitor 2024. ITU and UNITAR.
    "Laptop": [
        "Laptops have the largest embodied carbon footprint among portable personal devices at "
        "200 kg CO₂e—four times that of a smartphone.",
        "Life cycle assessments confirm that repairing and reusing functional hardware avoids the "
        "heavy environmental burden of replacement, whereas routing end-of-life units to formal "
        "recycling helps recover critical minerals—given that only 1% of rare-earth element demand "
        "is currently met by e-waste recycling.",
    ],

    # HARDWARE/MICROCONTROLLER DEVELOPMENT BOARDS (Arduino, ESP32)
    # Sources:
    #   Bullets 1 and 2: Nassajfar, M. N., et al. (2021). Sustainability, 13(21), 12126.
    "Microcontroller": [
        "Conventional printed circuit board (PCB) manufacturing relies on copper etching and "
        "chemical processing, where electricity generation and chemicals account for 41% and 25% "
        "of total global warming potential (GWP), respectively.",
        "Minimizing material consumption through reuse and increasing end-of-life (EoL) metal "
        "recycling rates significantly reduce the total environmental impact of PCB production "
        "and prevent persistent electronic waste in landfills.",
    ],
}


def show_did_you_know(device_type):
    """Show the tip card for one device type. Shows nothing if the type has no tip."""
    tips = DID_YOU_KNOW.get(device_type)
    if not tips:
        return

    with st.container(border=True):
        st.markdown("**💡 Did you know**")
        st.markdown("\n".join(f"- {tip}" for tip in tips))

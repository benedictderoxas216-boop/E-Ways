# guides_data.py
# Single source of truth for device repair information.
# To add a device, copy an existing entry and change the values.

DEVICES = {
    "iphone 13": {
        "brand": "Apple",
        "name": "iPhone 13",
        "category": "Phone",
        "repair_score": 5,
        "diy_difficulty": "Hard",
        "issues": [
            {
                "problem": "Battery degradation",
                "symptoms": "Drains quickly, shuts off at 20% or with no warning.",
                "steps": [
                    "Go to Settings > Battery > Battery Health & Charging.",
                    "If Maximum Capacity is below 80%, a battery replacement is likely needed.",
                    "Buy a reputable replacement battery and power off the phone before opening it.",
                    "Remove the two pentalobe screws at the bottom, then use a suction cup and plastic pry tool to lift the screen.",
                    "Disconnect the battery connector before removing the old battery.",
                ],
                "safety": "Lithium batteries can swell or catch fire when damaged. Do not puncture or bend a swollen battery. Take it to a recycling drop-off.",
            },
            {
                "problem": "Cracked screen",
                "symptoms": "Visible cracks, touch not responding in parts of the screen.",
                "steps": [
                    "Confirm the display itself is damaged and not just the glass cover.",
                    "Buy a display assembly that matches the model exactly.",
                    "Heat the edges of the screen gently to soften the adhesive.",
                    "Transfer the front camera and sensor cable from the old screen if your replacement does not include them.",
                ],
                "safety": "Broken glass can cut you. Wear gloves and wrap the screen in tape while working.",
            },
            {
                "problem": "Charging port failure",
                "symptoms": "Phone charges only at certain angles or not at all.",
                "steps": [
                    "Inspect the port with a flashlight for lint or debris.",
                    "Clean it carefully with a wooden or plastic toothpick. Never use metal.",
                    "If cleaning does not help, replace the lightning port flex cable.",
                ],
                "safety": "Unplug the phone before cleaning the port.",
            },
        ],
    },
    "arduino uno": {
        "brand": "Arduino",
        "name": "Arduino Uno R3",
        "category": "Microcontroller",
        "repair_score": 10,
        "diy_difficulty": "Easy",
        "issues": [
            {
                "problem": "Fried ATmega328P chip",
                "symptoms": "Board no longer uploads sketches, power LED is on but the board does not respond.",
                "steps": [
                    "Check the power LED and make sure the board is powered from USB.",
                    "Try loading a simple Blink sketch in the Arduino IDE.",
                    "If it still fails, remove the chip with a chip puller or a small flat screwdriver.",
                    "Carefully insert a new ATmega328P chip, or use a Uno bootloader programmer.",
                ],
                "safety": "Disconnect power before swapping chips. Avoid touching exposed pins with static charge.",
            },
            {
                "problem": "Broken USB port connector",
                "symptoms": "Board is loose in the port or does not connect to the computer.",
                "steps": [
                    "Look for cracked solder joints around the USB connector.",
                    "Reflow the solder joints with a soldering iron.",
                    "If the connector is torn off, replace the USB-B connector.",
                ],
                "safety": "Use a soldering iron in a ventilated area and wash your hands after handling solder.",
            },
        ],
    },
}

# General guides, organized by problem instead of by device.
# "categories" lists which device types each guide applies to.
# Add video links to "videos". Leave "url" empty to hide that entry.

GENERAL_GUIDES = {
    "Battery drains quickly": {
        "categories": ["Phone", "Tablet", "Laptop"],
        "symptoms": "The battery runs out much faster than it used to, or the device shuts off at a high percentage.",
        "steps": [
            "Check battery health in the device settings. A maximum capacity below about 80% usually means the battery is worn.",
            "Close background apps and turn off features you don't use, such as location or background refresh.",
            "If health is poor, replace the battery with a reputable part. Power off the device before opening it.",
        ],
        "safety": "Lithium batteries can swell or catch fire when damaged. Never puncture a swollen battery. Take it to a recycling drop-off.",
        "videos": [
            {"title": "Phone Battery replacement walkthrough", "url": "https://www.youtube.com/results?search_query=Android+phone+battery+replacement+step+by+step", "source": "Youtube"},
            {"title": "Laptop Battery replacement walkthrough", "url": "https://www.youtube.com/watch?v=JV8RMmrQ6pY", "source": "Remanac"},
            {"title": "General Battery replacement walkthrough", "url": "https://www.youtube.com/results?search_query=general+electronic+device+battery+replacement+walkthrough", "source": "Youtube"},
        ],
    },
    "Won't charge": {
        "categories": ["Phone", "Tablet", "Laptop"],
        "symptoms": "The device doesn't charge, charges only at certain angles, or the charging icon appears and disappears.",
        "steps": [
            "Try a different cable and power adapter that you know work.",
            "Inspect the charging port with a flashlight. Remove lint or debris with a wooden or plastic toothpick. Never use metal.",
            "If cleaning doesn't help, the port or its flex cable may need replacing.",
        ],
        "safety": "Unplug the device before cleaning the port. Use only the charger that came with the device or a certified replacement.",
        "videos": [
            {"title": "Phone Charging Troubleshoot", "url": "https://www.youtube.com/results?search_query=phone+not+charging+troubleshooting+step+by+step", "source": "Youtube"},
            {"title": "Laptop Charging Troubleshoot", "url": "https://www.youtube.com/results?search_query=laptop+not+charging+troubleshooting+repair", "source": "Youtube"},
            {"title": "Charging Port Repair", "url": "https://www.youtube.com/results?search_query=loose+phone+charging+port+repair", "source": "Youtube"},
        ],
    },
    "Cracked screen": {
        "categories": ["Phone", "Tablet"],
        "symptoms": "Visible cracks in the glass, or parts of the screen don't respond to touch.",
        "steps": [
            "Check whether only the glass is cracked or the display itself is damaged. If the display still works, a glass-only repair may be possible.",
            "If the display is damaged, buy a replacement that matches the exact model.",
            "Heat the edges gently to soften the adhesive before lifting the screen.",
        ],
        "safety": "Broken glass can cut you. Wear gloves and wrap the screen in tape while you work.",
        "videos": [
            {"title": "Phone Screen replacement walkthrough", "url": "https://www.youtube.com/results?search_query=smartphone+cracked+screen+repair+walkthrough", "source": "Youtube"},
            {"title": "Laptop Screen replacement walkthrough", "url": "https://www.youtube.com/results?search_query=laptop+LCD+screen+replacement+tutorial", "source": "Youtube"},
            {"title": "Screen replacement testing", "url": "https://www.youtube.com/results?search_query=phone+display+replacement+testing+touch+screen", "source": "Youtube"},
        ],
    },
    "Won't turn on": {
        "categories": ["Phone", "Tablet", "Laptop"],
        "symptoms": "The device shows no sign of power, even when plugged in.",
        "steps": [
            "Charge the device for at least 30 minutes with a known-good charger.",
            "Try a forced restart, following the method for your model.",
            "If it still doesn't respond, the battery, power button, or board may be faulty. Check whether a repair shop can diagnose it before buying parts.",
        ],
        "safety": "Do not charge a device with a swollen battery or visible damage.",
        "videos": [
            {"title": "Laptop Troubleshoot full guide", "url": "https://www.youtube.com/watch?v=_MOe71kBPOY", "source": "PC Monkey"},
            {"title": "Laptop Hard Reset", "url": "https://www.youtube.com/results?search_query=how+to+perform+laptop+hard+reset", "source": "Youtube"},
            {"title": "Diagnosing a Faulty Ram", "url": "https://www.youtube.com/results?search_query=how+to+diagnose+faulty+RAM+computer", "source": "Youtube"},
        ],
    },
    "Overheating": {
        "categories": ["Phone", "Tablet", "Laptop"],
        "symptoms": "The device gets very hot during normal use or charging, or shuts down to cool off.",
        "steps": [
            "Close heavy apps and remove any case while charging.",
            "On laptops, clean the air vents and fan with compressed air. Keep the device on a hard surface.",
            "If the device is still hot, or the battery is swollen, stop using it and seek professional help.",
        ],
        "safety": "A hot device with a swollen battery is a fire risk. Move it away from flammable materials and do not charge it.",
        "videos": [
            {"title": "iPhone Overheating repair", "url": "https://www.youtube.com/results?search_query=iphone+overheating+troubleshooting+repair", "source": "Youtube"},
            {"title": "Android Overheating repair", "url": "https://www.youtube.com/results?search_query=android+phone+overheating+troubleshooting+fix", "source": "Youtube"},
            {"title": "Laptop Overheating repair", "url": "https://www.youtube.com/results?search_query=how+to+fix+laptop+overheating+problem", "source": "Youtube"},
        ],
    },
    "Board or chip is damaged": {
        "categories": ["Microcontroller"],
        "symptoms": "The board no longer uploads sketches, the power LED is on but nothing responds, or a connector is loose.",
        "steps": [
            "Check the power LED and confirm the board is powered from USB.",
            "Upload a simple Blink sketch to test the board.",
            "If it still fails, inspect the connector solder joints with a magnifier. Reflow any cracked joints with a soldering iron.",
            "A damaged chip can be replaced, or the board can be salvaged for parts.",
        ],
        "safety": "Disconnect power before swapping chips. Use a soldering iron in a ventilated area and wash your hands after handling solder.",
        "videos": [
            {"title": "Microcontroller Diagnosis", "url": "https://www.youtube.com/results?search_query=how+to+diagnose+faulty+microcontroller", "source": "Youtube"},
            {"title": "Reprogramming Microcontrollers", "url": "https://www.youtube.com/results?search_query=microcontroller+reprogramming+using+programmer+tutorial", "source": "Youtube"},
            {"title": "Microcontroller PCB Fault Finding and Repair", "url": "https://www.youtube.com/results?search_query=microcontroller+PCB+fault+finding+and+repair", "source": "Youtube"},
        ],
    },
}
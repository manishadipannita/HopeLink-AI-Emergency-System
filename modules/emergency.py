# modules/emergency.py

import re


# =========================================================
# KEYWORDS
# =========================================================

KEYWORDS = {

    "Flood": [
        "flood",
        "flooded",
        "water everywhere",
        "trapped in water",
        "water entered",
        "bonna",
        "bonnay",
        "bonna hoise",
        "pani uthse",
        "pani dhukse",
        "panite atke",
        "পানি উঠেছে",
        "বন্যা",
        "বন্যায়",
        "পানিতে আটকে"
    ],

    "Fire": [
        "fire",
        "building fire",
        "house fire",
        "burning",
        "agun",
        "agun lagse",
        "agun lagche",
        "agun legeche",
        "আগুন",
        "আগুন লেগেছে",
        "আগুন লাগছে"
    ],

    "Earthquake": [
        "earthquake",
        "earth quake",
        "tremor",
        "building shaking",
        "bhumikompo",
        "ভূমিকম্প",
        "ভূমিকম্প হচ্ছে"
    ],

    "Accident": [
        "accident",
        "car accident",
        "road accident",
        "crash",
        "collision",
        "durghotona",
        "দুর্ঘটনা",
        "এক্সিডেন্ট"
    ],

    "Medical Emergency": [
        "medical emergency",
        "sick",
        "ill",
        "injured",
        "injury",
        "doctor",
        "hospital",
        "medicine",
        "medication",
        "treatment",
        "fever",
        "pain",
        "bleeding",
        "unconscious",
        "osustho",
        "osustho",
        "oshustho",
        "oshustho",
        "daktar",
        "doctor lagbe",
        "medicine lagbe",
        "osudh lagbe",
        "oshudh lagbe",
        "চিকিৎসা",
        "অসুস্থ",
        "অসুস্থ",
        "ডাক্তার",
        "ওষুধ",
        "রক্তপাত"
    ],

    "Blood Assistance": [
        "blood",
        "blood needed",
        "blood lagbe",
        "blood dorkar",
        "blood chai",
        "need blood",
        "blood donation",
        "blood donor",
        "rokto",
        "rokto lagbe",
        "rokto dorkar",
        "rokto chai",
        "rokto proyojon",
        "roktto",
        "রক্ত",
        "রক্ত লাগবে",
        "রক্ত দরকার",
        "রক্ত চাই",
        "রক্ত প্রয়োজন"
    ],

    "Food Assistance": [
        "food",
        "food needed",
        "need food",
        "food lagbe",
        "food dorkar",
        "food chai",
        "khabar",
        "khabar lagbe",
        "khabar dorkar",
        "khabar nai",
        "khabar nei",
        "khabar chai",
        "খাবার",
        "খাবার লাগবে",
        "খাবার দরকার",
        "খাবার নেই",
        "খাবার চাই"
    ],

    "Water Assistance": [
        "water needed",
        "need water",
        "water lagbe",
        "water dorkar",
        "water chai",
        "pani lagbe",
        "pani dorkar",
        "pani chai",
        "pani nei",
        "পানি লাগবে",
        "পানি দরকার",
        "পানি চাই",
        "পানি নেই"
    ],

    "Shelter Needed": [
        "shelter",
        "shelter needed",
        "need shelter",
        "place to stay",
        "place to live",
        "homeless",
        "no place to stay",
        "thakar jayga",
        "thakar jayga lagbe",
        "thakar jayga nai",
        "thakar jayga nei",
        "ashroy",
        "আশ্রয়",
        "থাকার জায়গা",
        "থাকার জায়গা লাগবে",
        "থাকার জায়গা নেই"
    ],

    "Volunteer Assistance": [
        "volunteer",
        "volunteers",
        "volunteer help",
        "need volunteer",
        "help me",
        "help needed",
        "need help",
        "i need help",
        "amar help lagbe",
        "amar help dorkar",
        "help lagbe",
        "help dorkar",
        "help chai",
        "amake help korun",
        "help koren",
        "help koro",
        "sahajjo",
        "sahajjo chai",
        "sahajjo lagbe",
        "sahajjo dorkar",
        "সাহায্য",
        "সাহায্য চাই",
        "সাহায্য লাগবে",
        "সাহায্য দরকার"
    ],

    "Rescue Assistance": [
        "rescue",
        "rescue needed",
        "need rescue",
        "save me",
        "trapped",
        "stuck",
        "atke gechi",
        "atke achi",
        "uddhar",
        "উদ্ধার",
        "উদ্ধার দরকার",
        "আটকে গেছি",
        "আটকে আছি"
    ],

    "Missing Person": [
        "missing person",
        "person missing",
        "lost person",
        "someone is missing",
        "nikhoj",
        "হারিয়ে গেছে",
        "নিখোঁজ"
    ]
}


# =========================================================
# CRITICAL / HIGH PRIORITY WORDS
# =========================================================

CRITICAL_WORDS = [
    "dying",
    "dead",
    "unconscious",
    "severe bleeding",
    "heavy bleeding",
    "can't breathe",
    "cannot breathe",
    "not breathing",
    "heart attack",
    "trapped",
    "fire",
    "explosion",
    "critical",
    "মারা যাচ্ছে",
    "অজ্ঞান",
    "অনেক রক্ত",
    "শ্বাস নিতে পারছে না",
    "শ্বাসকষ্ট",
    "হার্ট অ্যাটাক"
]

HIGH_WORDS = [
    "injured",
    "bleeding",
    "accident",
    "earthquake",
    "flood",
    "rescue",
    "emergency",
    "জরুরি",
    "দুর্ঘটনা",
    "আহত",
    "রক্তপাত"
]


# =========================================================
# TEXT NORMALIZATION
# =========================================================

def normalize_text(text):
    if not text:
        return ""

    text = str(text).lower().strip()

    text = re.sub(r"\s+", " ", text)

    return text


# =========================================================
# KEYWORD MATCH
# =========================================================

def contains_keyword(text, keyword):

    text = normalize_text(text)
    keyword = normalize_text(keyword)

    return keyword in text


# =========================================================
# DETECT NEEDS
# =========================================================

def detect_needs(text):

    text = normalize_text(text)

    detected = []

    for category, keywords in KEYWORDS.items():

        for keyword in keywords:

            if contains_keyword(text, keyword):

                if category not in detected:
                    detected.append(category)

                break

    # -----------------------------------------------------
    # Blood automatically means medical support
    # -----------------------------------------------------

    if "Blood Assistance" in detected:

        if "Medical Emergency" not in detected:
            detected.append("Medical Emergency")

    # -----------------------------------------------------
    # Medicine automatically means medical
    # -----------------------------------------------------

    if any(
        word in text
        for word in [
            "medicine",
            "medication",
            "medicine lagbe",
            "osudh",
            "oshudh",
            "ওষুধ"
        ]
    ):

        if "Medical Emergency" not in detected:
            detected.append("Medical Emergency")

    # -----------------------------------------------------
    # Help request
    # -----------------------------------------------------

    help_words = [
        "help",
        "help me",
        "need help",
        "amar help lagbe",
        "amar help dorkar",
        "help lagbe",
        "help dorkar",
        "help chai",
        "sahajjo",
        "সাহায্য"
    ]

    if any(word in text for word in help_words):

        if "Volunteer Assistance" not in detected:
            detected.append("Volunteer Assistance")

    # -----------------------------------------------------
    # Rescue situation
    # -----------------------------------------------------

    rescue_words = [
        "trapped",
        "stuck",
        "atke",
        "আটকে",
        "rescue",
        "উদ্ধার"
    ]

    if any(word in text for word in rescue_words):

        if "Rescue Assistance" not in detected:
            detected.append("Rescue Assistance")

    # -----------------------------------------------------
    # No specific need
    # -----------------------------------------------------

    if not detected:

        detected.append("General Emergency")

    return detected


# =========================================================
# PRIMARY CRISIS
# =========================================================

def determine_primary_crisis(needs):

    priority_order = [

        "Fire",
        "Earthquake",
        "Flood",
        "Accident",
        "Medical Emergency",
        "Rescue Assistance",
        "Blood Assistance",
        "Shelter Needed",
        "Food Assistance",
        "Water Assistance",
        "Volunteer Assistance",
        "Missing Person"
    ]

    for item in priority_order:

        if item in needs:
            return item

    return "General Emergency"


# =========================================================
# SEVERITY
# =========================================================

def determine_severity(text, needs):

    text = normalize_text(text)

    # Critical
    for word in CRITICAL_WORDS:

        if word in text:
            return "Critical"

    # High
    for word in HIGH_WORDS:

        if word in text:
            return "High"

    # Multiple needs
    if len(needs) >= 3:
        return "High"

    # Medical / rescue / blood
    if any(
        item in needs
        for item in [
            "Medical Emergency",
            "Blood Assistance",
            "Rescue Assistance"
        ]
    ):
        return "High"

    return "Medium"


# =========================================================
# EXPLANATION
# =========================================================

def generate_explanation(primary_crisis, needs):

    if primary_crisis == "Food Assistance":

        return (
            "The request appears to be mainly related to food assistance. "
            "HopeLink identified the need for food support."
        )

    if primary_crisis == "Blood Assistance":

        return (
            "The request indicates a need for blood or blood-donation support. "
            "Medical assistance may also be required."
        )

    if primary_crisis == "Medical Emergency":

        return (
            "The message indicates a possible medical or health-related need. "
            "Medical support may be required."
        )

    if primary_crisis == "Shelter Needed":

        return (
            "The request indicates that safe accommodation or shelter "
            "may be needed."
        )

    if primary_crisis == "Flood":

        return (
            "The message indicates a flood or water-related emergency. "
            "Rescue, shelter, food or water support may be required."
        )

    if primary_crisis == "Fire":

        return (
            "The message indicates a possible fire emergency. "
            "Immediate safety and emergency response may be required."
        )

    if primary_crisis == "Earthquake":

        return (
            "The message indicates a possible earthquake-related emergency. "
            "Safety assessment and emergency assistance may be required."
        )

    if primary_crisis == "Accident":

        return (
            "The message indicates a possible accident. "
            "Medical and emergency support may be required."
        )

    if primary_crisis == "Volunteer Assistance":

        return (
            "The person appears to be requesting general help or volunteer support."
        )

    return (
        "The message indicates a general request for emergency assistance. "
        "More specific information may be needed."
    )


# =========================================================
# REQUIRED SUPPORT
# =========================================================

def get_required_support(needs):

    support = []

    mapping = {
        "Food Assistance": "Food Support",
        "Water Assistance": "Water Support",
        "Blood Assistance": "Blood Donor / Blood Support",
        "Medical Emergency": "Medical Assistance",
        "Shelter Needed": "Shelter Support",
        "Volunteer Assistance": "Volunteer Assistance",
        "Rescue Assistance": "Emergency Rescue",
        "Flood": "Flood Response",
        "Fire": "Fire Emergency Response",
        "Earthquake": "Earthquake Response",
        "Accident": "Emergency Medical Support",
        "Missing Person": "Search & Support"
    }

    for need in needs:

        if need in mapping and mapping[need] not in support:

            support.append(mapping[need])

    if not support:

        support.append("Emergency Support")

    return support


# =========================================================
# MAIN ANALYSIS FUNCTION
# =========================================================

def analyze_emergency(text):

    text = normalize_text(text)

    if not text:

        return {
            "primary_crisis": "General Emergency",
            "detected_needs": ["General Emergency"],
            "severity": "Medium",
            "assessment": "No message provided",
            "explanation": "Please describe what kind of help is needed.",
            "required_support": ["Emergency Support"]
        }

    needs = detect_needs(text)

    primary = determine_primary_crisis(needs)

    severity = determine_severity(text, needs)

    explanation = generate_explanation(
        primary,
        needs
    )

    support = get_required_support(needs)

    return {
        "primary_crisis": primary,
        "detected_needs": needs,
        "severity": severity,
        "assessment": "Needs identified from your message",
        "explanation": explanation,
        "required_support": support
    }


# =========================================================
# AI RESPONSE
# =========================================================

def generate_response(analysis):

    if isinstance(analysis, dict):

        primary = analysis.get(
            "primary_crisis",
            "General Emergency"
        )

        needs = analysis.get(
            "detected_needs",
            []
        )

        severity = analysis.get(
            "severity",
            "Medium"
        )

    else:

        primary = "General Emergency"
        needs = []
        severity = "Medium"

    # -----------------------------------------------------
    # Food
    # -----------------------------------------------------

    if "Food Assistance" in needs:

        message = (
            "HopeLink identified a food assistance need. "
            "Please stay in a safe location while food support is arranged."
        )

    # -----------------------------------------------------
    # Blood
    # -----------------------------------------------------

    elif "Blood Assistance" in needs:

        message = (
            "HopeLink identified a blood assistance need. "
            "Please contact a hospital or verified blood-donation service "
            "as soon as possible."
        )

    # -----------------------------------------------------
    # Medical
    # -----------------------------------------------------

    elif "Medical Emergency" in needs:

        message = (
            "HopeLink identified a possible medical emergency. "
            "Please seek professional medical assistance immediately "
            "if the situation is serious."
        )

    # -----------------------------------------------------
    # Fire
    # -----------------------------------------------------

    elif primary == "Fire":

        message = (
            "Please move to a safe location away from the fire "
            "and contact local emergency services."
        )

    # -----------------------------------------------------
    # Flood
    # -----------------------------------------------------

    elif primary == "Flood":

        message = (
            "Please move to higher and safer ground if possible. "
            "Avoid moving through fast-flowing water."
        )

    # -----------------------------------------------------
    # Shelter
    # -----------------------------------------------------

    elif "Shelter Needed" in needs:

        message = (
            "HopeLink identified a shelter need. "
            "Please move to a safe temporary shelter if available."
        )

    # -----------------------------------------------------
    # Volunteer
    # -----------------------------------------------------

    elif "Volunteer Assistance" in needs:

        message = (
            "HopeLink identified a request for help. "
            "Volunteer or community assistance may be needed."
        )

    # -----------------------------------------------------
    # Rescue
    # -----------------------------------------------------

    elif "Rescue Assistance" in needs:

        message = (
            "A rescue situation may be involved. "
            "Stay as safe as possible and contact emergency responders."
        )

    else:

        message = (
            "Please stay safe. Emergency support may be required. "
            "Provide more details if possible."
        )

    return (
        f"{message}\n\n"
        f"Priority Level: {severity}"
    )


# =========================================================
# SAFETY TIPS
# =========================================================

def get_emergency_tips(primary_crisis):

    tips = {

        "Flood": [
            "Move to higher ground if possible.",
            "Avoid fast-moving water.",
            "Keep drinking water and essential medicines with you.",
            "Follow official emergency instructions."
        ],

        "Fire": [
            "Move away from the fire immediately.",
            "Do not use elevators during a building fire.",
            "Stay low if there is heavy smoke.",
            "Contact local emergency services."
        ],

        "Earthquake": [
            "Drop, cover and hold on.",
            "Stay away from windows.",
            "Do not use elevators.",
            "Move outside only when it is safe."
        ],

        "Medical Emergency": [
            "Seek professional medical assistance.",
            "Do not take unknown medication.",
            "Keep the patient in a safe position.",
            "Contact emergency medical services if necessary."
        ],

        "Accident": [
            "Move to a safe location if possible.",
            "Avoid unnecessary movement of seriously injured people.",
            "Call emergency medical assistance.",
            "Provide basic first aid only if you know how."
        ],

        "Shelter Needed": [
            "Move to a safe location.",
            "Stay with trusted people if possible.",
            "Keep important documents and medicines with you."
        ],

        "Food Assistance": [
            "Stay in a safe location.",
            "Use safe drinking water.",
            "Contact trusted community or humanitarian support."
        ],

        "Blood Assistance": [
            "Contact a hospital or verified blood bank.",
            "Provide the required blood group if known.",
            "Do not delay professional medical care."
        ],

        "Volunteer Assistance": [
            "Clearly describe what type of help is needed.",
            "Stay in a safe and accessible location.",
            "Avoid sharing unnecessary personal information."
        ]
    }

    return tips.get(
        primary_crisis,
        [
            "Stay calm and move to a safe location.",
            "Contact local emergency services if necessary.",
            "Follow official safety instructions."
        ]
    )


# =========================================================
# VOLUNTEER MATCH
# =========================================================

def match_volunteer(
    name,
    location,
    help_types,
    availability
):

    return {
        "name": name,
        "location": location,
        "help_types": help_types,
        "availability": availability,
        "status": "Registered"
    }

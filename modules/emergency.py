# modules/emergency.py

import re


# =========================================================
# KEYWORDS
# =========================================================

KEYWORDS = {

    "Flood": [
        "flood",
        "flooded",
        "flooding",
        "water everywhere",
        "trapped in water",
        "water entered",
        "water entered the house",
        "bonna",
        "bonnay",
        "bonna hoise",
        "bonna hoyeche",
        "pani uthse",
        "pani utheche",
        "pani dhukse",
        "pani dhukche",
        "panite atke",
        "পানি উঠেছে",
        "পানি ঢুকেছে",
        "বন্যা",
        "বন্যায়",
        "বন্যায়",
        "পানিতে আটকে"
    ],

    "Fire": [
        "fire",
        "building fire",
        "house fire",
        "burning",
        "burning house",
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
        "ground shaking",
        "bhumikompo",
        "ভূমিকম্প",
        "ভূমিকম্প হচ্ছে"
    ],

    "Accident": [
        "accident",
        "car accident",
        "road accident",
        "traffic accident",
        "crash",
        "collision",
        "durghotona",
        "দুর্ঘটনা",
        "এক্সিডেন্ট"
    ],

    "Medical Emergency": [
        "medical emergency",
        "medical help",
        "medical assistance",
        "injured",
        "injury",
        "injured person",
        "hurt",
        "badly hurt",
        "seriously injured",
        "sick",
        "ill",
        "patient",
        "doctor",
        "doctor needed",
        "doctor lagbe",
        "hospital",
        "hospital needed",
        "medicine",
        "medicine needed",
        "medicine lagbe",
        "medication",
        "treatment",
        "treatment needed",
        "fever",
        "pain",
        "severe pain",
        "bleeding",
        "heavy bleeding",
        "unconscious",
        "cannot breathe",
        "can't breathe",
        "breathing problem",
        "osustho",
        "oshustho",
        "oshustho",
        "daktar",
        "daktar lagbe",
        "osudh",
        "oshudh",
        "osudh lagbe",
        "oshudh lagbe",
        "চিকিৎসা",
        "চিকিৎসা দরকার",
        "অসুস্থ",
        "অসুস্থ",
        "আহত",
        "আঘাত",
        "ডাক্তার",
        "হাসপাতাল",
        "ওষুধ",
        "রক্তপাত",
        "শ্বাসকষ্ট"
    ],

    "Blood Assistance": [
        "blood",
        "blood needed",
        "blood assistance",
        "blood donor",
        "blood donation",
        "need blood",
        "need a blood donor",
        "blood lagbe",
        "blood dorkar",
        "blood chai",
        "blood proyojon",
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
        "রক্ত প্রয়োজন",
        "রক্ত প্রয়োজন"
    ],

    "Food Assistance": [
        "food",
        "food needed",
        "need food",
        "food assistance",
        "food support",
        "food lagbe",
        "food dorkar",
        "food chai",
        "khabar",
        "khabar lagbe",
        "khabar dorkar",
        "khabar chai",
        "khabar nai",
        "khabar nei",
        "খাবার",
        "খাবার লাগবে",
        "খাবার দরকার",
        "খাবার চাই",
        "খাবার নেই"
    ],

    "Water Assistance": [
        "water needed",
        "need water",
        "water assistance",
        "water support",
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
        "safe shelter",
        "place to stay",
        "place to live",
        "homeless",
        "no place to stay",
        "no place to live",
        "thakar jayga",
        "thakar jayga lagbe",
        "thakar jayga dorkar",
        "thakar jayga nai",
        "thakar jayga nei",
        "ashroy",
        "আশ্রয়",
        "আশ্রয়",
        "থাকার জায়গা",
        "থাকার জায়গা",
        "থাকার জায়গা লাগবে",
        "থাকার জায়গা দরকার",
        "থাকার জায়গা নেই"
    ],

    "Volunteer Assistance": [
        "volunteer",
        "volunteers",
        "volunteer help",
        "need volunteer",
        "need volunteers",
        "volunteer assistance",
        "help me",
        "help needed",
        "need help",
        "i need help",
        "i need some help",
        "please help",
        "amar help lagbe",
        "amar help dorkar",
        "amar help chai",
        "help lagbe",
        "help dorkar",
        "help chai",
        "help koren",
        "help korun",
        "amake help korun",
        "sahajjo",
        "sahajjo chai",
        "sahajjo lagbe",
        "sahajjo dorkar",
        "সাহায্য",
        "সাহায্য চাই",
        "সাহায্য লাগবে",
        "সাহায্য দরকার",
        "আমার সাহায্য দরকার",
        "আমার সাহায্য লাগবে"
    ],

    "Rescue Assistance": [
        "rescue",
        "rescue needed",
        "need rescue",
        "rescue assistance",
        "save me",
        "trapped",
        "stuck",
        "atke gechi",
        "atke achi",
        "atke asi",
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
        "missing",
        "nikhoj",
        "নিখোঁজ",
        "হারিয়ে গেছে",
        "হারিয়ে গেছে"
    ]
}


# =========================================================
# PRIORITY WORDS
# =========================================================

CRITICAL_WORDS = [
    "dying",
    "dead",
    "unconscious",
    "severe bleeding",
    "heavy bleeding",
    "cannot breathe",
    "can't breathe",
    "not breathing",
    "heart attack",
    "explosion",
    "critical",
    "মারা যাচ্ছে",
    "অজ্ঞান",
    "অনেক রক্তপাত",
    "শ্বাস নিতে পারছে না",
    "শ্বাসকষ্ট",
    "হার্ট অ্যাটাক"
]


HIGH_WORDS = [
    "injured",
    "injury",
    "bleeding",
    "accident",
    "earthquake",
    "flood",
    "fire",
    "rescue",
    "blood",
    "emergency",
    "জরুরি",
    "দুর্ঘটনা",
    "আহত",
    "রক্তপাত"
]


# =========================================================
# NORMALIZE TEXT
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
    # Blood = Medical too
    # -----------------------------------------------------

    if "Blood Assistance" in detected:

        if "Medical Emergency" not in detected:

            detected.append("Medical Emergency")


    # -----------------------------------------------------
    # Medicine = Medical
    # -----------------------------------------------------

    medicine_words = [
        "medicine",
        "medication",
        "medicine lagbe",
        "osudh",
        "oshudh",
        "ওষুধ"
    ]

    if any(word in text for word in medicine_words):

        if "Medical Emergency" not in detected:

            detected.append("Medical Emergency")


    # -----------------------------------------------------
    # Injury = Medical
    # -----------------------------------------------------

    injury_words = [
        "injured",
        "injury",
        "hurt",
        "badly hurt",
        "seriously injured",
        "আহত",
        "আঘাত"
    ]

    if any(word in text for word in injury_words):

        if "Medical Emergency" not in detected:

            detected.append("Medical Emergency")


    # -----------------------------------------------------
    # General help = Volunteer
    # -----------------------------------------------------

    help_words = [
        "help",
        "help me",
        "need help",
        "i need help",
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
    # Rescue
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
    # General emergency only if nothing detected
    # -----------------------------------------------------

    if not detected:

        detected.append("General Emergency")


    return detected


# =========================================================
# PRIMARY CRISIS
# =========================================================

def determine_primary_crisis(needs):

    # Specific emergency types first
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
        "Missing Person",
        "Volunteer Assistance"
    ]

    for crisis in priority_order:

        if crisis in needs:

            return crisis


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


    # Medical / blood / rescue
    if any(
        need in needs
        for need in [
            "Medical Emergency",
            "Blood Assistance",
            "Rescue Assistance"
        ]
    ):

        return "High"


    return "Medium"


# =========================================================
# MATCH STRENGTH
# =========================================================

def determine_match_strength(text, needs):

    text = normalize_text(text)

    if not text:

        return "Moderate"


    if "General Emergency" in needs:

        return "Moderate"


    # Strong when obvious specific keywords exist
    if len(needs) >= 2:

        return "Strong"


    if len(text.split()) <= 2:

        return "Good"


    return "Good"


# =========================================================
# EXPLANATION
# =========================================================

def generate_explanation(primary_crisis, needs):

    if primary_crisis == "Medical Emergency":

        return (
            "The message indicates a possible medical or "
            "health-related situation. Medical assistance "
            "may be required."
        )


    if primary_crisis == "Blood Assistance":

        return (
            "The message indicates a need for blood or "
            "blood-donation support. Medical assistance "
            "may also be required."
        )


    if primary_crisis == "Food Assistance":

        return (
            "The message indicates a need for food support. "
            "Food assistance may be required."
        )


    if primary_crisis == "Water Assistance":

        return (
            "The message indicates a need for clean drinking "
            "water or water-related support."
        )


    if primary_crisis == "Shelter Needed":

        return (
            "The message indicates a need for safe shelter "
            "or temporary accommodation."
        )


    if primary_crisis == "Volunteer Assistance":

        return (
            "The person appears to be requesting general "
            "help or volunteer support."
        )


    if primary_crisis == "Flood":

        return (
            "The message indicates a flood or water-related "
            "emergency. Rescue, shelter, food or water support "
            "may be required."
        )


    if primary_crisis == "Fire":

        return (
            "The message indicates a possible fire emergency. "
            "Immediate safety and emergency response may be required."
        )


    if primary_crisis == "Earthquake":

        return (
            "The message indicates a possible earthquake-related "
            "emergency. Safety assessment and emergency assistance "
            "may be required."
        )


    if primary_crisis == "Accident":

        return (
            "The message indicates a possible accident. "
            "Medical and emergency support may be required."
        )


    if primary_crisis == "Rescue Assistance":

        return (
            "The message indicates a possible rescue situation. "
            "Emergency responders may be required."
        )


    return (
        "HopeLink analyzed the message but could not identify "
        "a specific emergency category. More details may help."
    )


# =========================================================
# REQUIRED SUPPORT
# =========================================================

def get_required_support(needs):

    support = []

    mapping = {

        "Medical Emergency":
            "Medical Assistance",

        "Blood Assistance":
            "Blood Donor / Blood Support",

        "Food Assistance":
            "Food Support",

        "Water Assistance":
            "Water Support",

        "Shelter Needed":
            "Shelter Support",

        "Volunteer Assistance":
            "Volunteer Assistance",

        "Rescue Assistance":
            "Emergency Rescue",

        "Flood":
            "Flood Response",

        "Fire":
            "Fire Emergency Response",

        "Earthquake":
            "Earthquake Response",

        "Accident":
            "Emergency Medical Support",

        "Missing Person":
            "Search & Support"
    }


    for need in needs:

        if need in mapping:

            support_item = mapping[need]

            if support_item not in support:

                support.append(support_item)


    if not support:

        support.append("Emergency Support")


    return support


# =========================================================
# MAIN ANALYSIS
# =========================================================

def analyze_emergency(text):

    text = normalize_text(text)

    if not text:

        return {
            "type": "General Emergency",
            "primary_crisis": "General Emergency",

            "needs": [
                "General Emergency"
            ],

            "detected_needs": [
                "General Emergency"
            ],

            "severity": "Medium",

            "match_strength": "Moderate",

            "explanation":
                "Please describe what kind of help is needed.",

            "required_help": [
                "Emergency Support"
            ],

            "required_support": [
                "Emergency Support"
            ]
        }


    # Detect needs
    needs = detect_needs(text)


    # Primary crisis
    primary = determine_primary_crisis(needs)


    # Severity
    severity = determine_severity(
        text,
        needs
    )


    # Match
    match_strength = determine_match_strength(
        text,
        needs
    )


    # Explanation
    explanation = generate_explanation(
        primary,
        needs
    )


    # Required support
    required_support = get_required_support(
        needs
    )


    # -----------------------------------------------------
    # IMPORTANT:
    # Return BOTH old and new key names.
    # This keeps other modules compatible.
    # -----------------------------------------------------

    result = {

        # Old app.py compatibility
        "type": primary,

        "needs": needs,

        "required_help": required_support,


        # New structure
        "primary_crisis": primary,

        "detected_needs": needs,

        "required_support": required_support,


        # Common fields
        "severity": severity,

        "match_strength": match_strength,

        "explanation": explanation
    }


    return result

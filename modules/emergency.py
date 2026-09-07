from transformers import pipeline


# =========================================================
# AI MODEL
# =========================================================

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    device=-1
)


# =========================================================
# CATEGORIES
# =========================================================

CATEGORIES = [
    "Flood",
    "Fire",
    "Earthquake",
    "Accident",
    "Medical Emergency",
    "Blood Assistance",
    "Medicine Assistance",
    "Food Assistance",
    "Water Assistance",
    "Shelter Needed",
    "Rescue Needed",
    "Volunteer Assistance",
    "Missing Person",
    "General Emergency"
]


# =========================================================
# KEYWORDS
# Useful especially for Bangla/Banglish input
# =========================================================

KEYWORDS = {

    "Food Assistance": [
        "food",
        "foods",
        "hungry",
        "hunger",
        "meal",
        "meals",
        "rice",
        "খাবার",
        "খেতে",
        "ক্ষুধা"
    ],

    "Water Assistance": [
        "water",
        "drinking water",
        "clean water",
        "পানি",
        "জল",
        "খাবার পানি",
        "বিশুদ্ধ পানি"
    ],

    "Blood Assistance": [
        "blood",
        "blood donor",
        "blood donation",
        "need blood",
        "blood needed",
        "রক্ত",
        "রক্ত লাগবে",
        "রক্ত দরকার",
        "রক্ত প্রয়োজন"
    ],

    "Medicine Assistance": [
        "medicine",
        "medicines",
        "medication",
        "medicine needed",
        "need medicine",
        "need medicines",
        "tablet",
        "tablets",
        "ওষুধ",
        "ওষুধ লাগবে",
        "ওষুধ দরকার"
    ],

    "Shelter Needed": [
        "shelter",
        "place to stay",
        "somewhere to stay",
        "safe place to stay",
        "homeless",
        "stay tonight",
        "থাকার জায়গা",
        "থাকার জায়গা দরকার",
        "আশ্রয়",
        "আশ্রয় দরকার"
    ],

    "Rescue Needed": [
        "rescue",
        "trapped",
        "stuck",
        "cannot get out",
        "can't get out",
        "unable to escape",
        "আটকে",
        "আটকা",
        "বের হতে পারছি না",
        "উদ্ধার"
    ],

    "Volunteer Assistance": [
        "volunteer",
        "volunteers",
        "need volunteers",
        "people to help",
        "people needed to help",
        "স্বেচ্ছাসেবক",
        "মানুষ দরকার",
        "সাহায্য করার মানুষ"
    ],

    "Medical Emergency": [
        "injured",
        "injury",
        "sick",
        "hospital",
        "doctor",
        "medical",
        "ambulance",
        "bleeding",
        "unconscious",
        "hurt",
        "patient",
        "অসুস্থ",
        "আহত",
        "ডাক্তার",
        "হাসপাতাল",
        "অ্যাম্বুলেন্স",
        "রক্তপাত",
        "রোগী"
    ],

    "Flood": [
        "flood",
        "flooded",
        "flooding",
        "water entered",
        "water level",
        "flood water",
        "বন্যা",
        "প্লাবিত",
        "পানি ঢুকেছে",
        "পানি বাড়ছে"
    ],

    "Fire": [
        "fire",
        "burning",
        "flames",
        "আগুন",
        "জ্বলছে",
        "পুড়ছে"
    ],

    "Earthquake": [
        "earthquake",
        "earthquake happened",
        "ভূমিকম্প"
    ],

    "Accident": [
        "accident",
        "crash",
        "collision",
        "road accident",
        "car accident",
        "দুর্ঘটনা",
        "এক্সিডেন্ট"
    ],

    "Missing Person": [
        "missing person",
        "missing",
        "lost person",
        "can't find",
        "cannot find",
        "নিখোঁজ",
        "হারিয়ে গেছে"
    ]
}


# =========================================================
# SUPPORT MAPPING
# =========================================================

SUPPORT = {

    "Flood": [
        "Rescue Team",
        "Food Supply",
        "Temporary Shelter",
        "Clean Water"
    ],

    "Fire": [
        "Fire Service",
        "Rescue Team",
        "Emergency Transport"
    ],

    "Earthquake": [
        "Rescue Team",
        "Temporary Shelter",
        "Medical Support",
        "Food Supply"
    ],

    "Accident": [
        "Emergency Transport",
        "Medical Support",
        "Blood Assistance"
    ],

    "Medical Emergency": [
        "Medical Support",
        "Ambulance",
        "Doctor Assistance"
    ],

    "Blood Assistance": [
        "Blood Donor",
        "Medical Support",
        "Hospital Assistance"
    ],

    "Medicine Assistance": [
        "Medicine Support",
        "Medical Support",
        "Pharmacy Assistance"
    ],

    "Food Assistance": [
        "Food Supply",
        "Food Distribution Team",
        "Volunteer Assistance"
    ],

    "Water Assistance": [
        "Clean Water",
        "Water Distribution Team",
        "Volunteer Assistance"
    ],

    "Shelter Needed": [
        "Temporary Shelter",
        "Food Supply",
        "Clean Water"
    ],

    "Rescue Needed": [
        "Rescue Team",
        "Emergency Transport",
        "Medical Support"
    ],

    "Volunteer Assistance": [
        "Volunteers",
        "Food Distribution Team",
        "Rescue Support"
    ],

    "Missing Person": [
        "Search & Rescue Team",
        "Police Assistance",
        "Volunteer Assistance"
    ],

    "General Emergency": [
        "Emergency Support",
        "Volunteer Assistance"
    ]
}


# =========================================================
# SEVERITY KEYWORDS
# =========================================================

CRITICAL_WORDS = [
    "dying",
    "critical",
    "unconscious",
    "severe bleeding",
    "heavy bleeding",
    "bleeding badly",
    "trapped",
    "can't breathe",
    "cannot breathe",
    "life threatening",
    "life-threatening",
    "urgent",
    "urgently",
    "child trapped",
    "baby trapped",
    "মারা যাচ্ছে",
    "মুমূর্ষু",
    "অজ্ঞান",
    "অনেক রক্ত",
    "রক্তপাত",
    "আটকে",
    "জরুরি"
]


HIGH_WORDS = [
    "injured",
    "injury",
    "sick",
    "flood",
    "flooded",
    "fire",
    "accident",
    "medicine",
    "blood",
    "homeless",
    "no food",
    "hungry",
    "no water",
    "আহত",
    "অসুস্থ",
    "বন্যা",
    "আগুন",
    "দুর্ঘটনা",
    "ওষুধ",
    "রক্ত",
    "ক্ষুধা"
]


# =========================================================
# KEYWORD CHECK
# =========================================================

def contains_keyword(text, keywords):

    text_lower = text.lower()

    for keyword in keywords:

        if keyword.lower() in text_lower:
            return True

    return False


# =========================================================
# DETECT NEEDS
# =========================================================

def detect_needs(text):

    detected = []

    # ---------------------------------------------
    # First: direct keyword detection
    # ---------------------------------------------

    for category, keywords in KEYWORDS.items():

        if contains_keyword(text, keywords):

            detected.append(category)


    # ---------------------------------------------
    # Special logic:
    # Blood should automatically imply medical need
    # ---------------------------------------------

    if "Blood Assistance" in detected:

        if "Medical Emergency" not in detected:
            detected.append("Medical Emergency")


    # ---------------------------------------------
    # Medicine should imply medical support
    # ---------------------------------------------

    if "Medicine Assistance" in detected:

        if "Medical Emergency" not in detected:
            detected.append("Medical Emergency")


    # ---------------------------------------------
    # AI detection
    # ---------------------------------------------

    try:

        ai_result = classifier(
            text,
            CATEGORIES,
            hypothesis_template="This person's situation is about {}."
        )

        top_label = ai_result["labels"][0]
        top_score = ai_result["scores"][0]


        # Only use AI prediction if it is reasonably meaningful
        if top_score >= 0.35:

            if top_label not in detected:

                detected.insert(0, top_label)

    except Exception:

        pass


    # ---------------------------------------------
    # Remove duplicates
    # ---------------------------------------------

    unique_needs = []

    for item in detected:

        if item not in unique_needs:

            unique_needs.append(item)


    # ---------------------------------------------
    # Fallback
    # ---------------------------------------------

    if not unique_needs:

        unique_needs = ["General Emergency"]


    return unique_needs


# =========================================================
# PRIMARY CRISIS
# =========================================================

def detect_primary_crisis(text, needs):

    crisis_categories = [
        "Flood",
        "Fire",
        "Earthquake",
        "Accident",
        "Missing Person"
    ]


    # If explicit crisis keyword exists,
    # prioritize it over generic AI prediction.

    for crisis in crisis_categories:

        if crisis in needs:

            return crisis


    # If no physical crisis exists,
    # choose the most important need.

    priority_order = [
        "Medical Emergency",
        "Blood Assistance",
        "Rescue Needed",
        "Medicine Assistance",
        "Food Assistance",
        "Water Assistance",
        "Shelter Needed",
        "Volunteer Assistance",
        "General Emergency"
    ]


    for item in priority_order:

        if item in needs:

            return item


    return "General Emergency"


# =========================================================
# SEVERITY
# =========================================================

def detect_severity(text, needs):

    text_lower = text.lower()


    # ---------------------------------------------
    # Critical
    # ---------------------------------------------

    for word in CRITICAL_WORDS:

        if word.lower() in text_lower:

            return "Critical"


    # ---------------------------------------------
    # High
    # ---------------------------------------------

    for word in HIGH_WORDS:

        if word.lower() in text_lower:

            return "High"


    # ---------------------------------------------
    # Multiple serious needs
    # ---------------------------------------------

    serious_needs = [
        "Medical Emergency",
        "Blood Assistance",
        "Rescue Needed",
        "Fire",
        "Accident"
    ]

    if any(item in needs for item in serious_needs):

        return "High"


    return "Medium"


# =========================================================
# REQUIRED SUPPORT
# =========================================================

def get_required_support(needs):

    support = []

    for need in needs:

        for item in SUPPORT.get(need, []):

            if item not in support:

                support.append(item)


    return support


# =========================================================
# EXPLANATION
# =========================================================

def generate_explanation(text, needs, severity):

    explanation_map = {

        "Flood":
            "a flood-related crisis",

        "Fire":
            "a fire-related emergency",

        "Earthquake":
            "an earthquake-related emergency",

        "Accident":
            "an accident",

        "Medical Emergency":
            "a medical situation",

        "Blood Assistance":
            "a blood requirement",

        "Medicine Assistance":
            "a medicine requirement",

        "Food Assistance":
            "a food requirement",

        "Water Assistance":
            "a clean water requirement",

        "Shelter Needed":
            "a need for temporary shelter",

        "Rescue Needed":
            "a rescue requirement",

        "Volunteer Assistance":
            "a need for volunteer support",

        "Missing Person":
            "a missing-person situation",

        "General Emergency":
            "an emergency situation"
    }


    descriptions = []

    for need in needs:

        if need in explanation_map:

            descriptions.append(
                explanation_map[need]
            )


    if len(descriptions) == 1:

        reason = descriptions[0]

    elif len(descriptions) == 2:

        reason = descriptions[0] + " and " + descriptions[1]

    else:

        reason = (
            ", ".join(descriptions[:-1])
            + ", and "
            + descriptions[-1]
        )


    return (
        "HopeLink detected "
        + reason
        + ". Based on the described situation, "
        + severity.lower()
        + " priority support was recommended."
    )


# =========================================================
# MAIN ANALYSIS FUNCTION
# =========================================================

def analyze_emergency(text):

    text = text.strip()


    if not text:

        return {
            "type": "General Emergency",
            "needs": ["General Emergency"],
            "confidence": 0,
            "match_strength": "Moderate",
            "severity": "Medium",
            "required_help": ["Emergency Support"],
            "explanation": "Please describe your emergency."
        }


    # Detect all needs
    needs = detect_needs(text)


    # Detect main crisis
    primary_crisis = detect_primary_crisis(
        text,
        needs
    )


    # Detect severity
    severity = detect_severity(
        text,
        needs
    )


    # Required support
    required_help = get_required_support(
        needs
    )


    # ---------------------------------------------
    # AI Match Strength
    # ---------------------------------------------

    try:

        ai_result = classifier(
            text,
            CATEGORIES,
            hypothesis_template="This person's situation is about {}."
        )

        score = ai_result["scores"][0]


        if score >= 0.60:

            match_strength = "Strong"

        elif score >= 0.35:

            match_strength = "Good"

        else:

            match_strength = "Moderate"

    except Exception:

        match_strength = "Good"


    # ---------------------------------------------
    # Explanation
    # ---------------------------------------------

    explanation = generate_explanation(
        text,
        needs,
        severity
    )


    return {

        "type": primary_crisis,

        "needs": needs,

        # Kept only for compatibility with old code
        "confidence": 0,

        "match_strength": match_strength,

        "severity": severity,

        "required_help": required_help,

        "explanation": explanation
    }

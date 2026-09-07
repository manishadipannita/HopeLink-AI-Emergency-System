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
        "need food",
        "i need food",
        "food needed",
        "no food",
        "খাবার",
        "খাবার লাগবে",
        "খাবার দরকার",
        "খাবার প্রয়োজন",
        "খেতে পারছি না",
        "ক্ষুধা",
        "চাল দরকার"
    ],

    "Water Assistance": [
        "water",
        "drinking water",
        "clean water",
        "safe water",
        "water needed",
        "need water",
        "no water",
        "পানি",
        "পানি লাগবে",
        "পানি দরকার",
        "পানি প্রয়োজন",
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
        "blood required",
        "need a blood donor",
        "looking for blood",
        "rokto",
        "roktto",
        "rokto lagbe",
        "rokto dorkar",
        "rokto proyojon",
        "rokto chai",
        "রক্ত",
        "রক্ত লাগবে",
        "রক্ত দরকার",
        "রক্ত প্রয়োজন",
        "রক্ত চাই",
        "রক্তদাতা",
        "রক্ত দাতা"
    ],

    "Medicine Assistance": [
        "medicine",
        "medicines",
        "medication",
        "medicine needed",
        "need medicine",
        "need medicines",
        "medicine required",
        "tablet",
        "tablets",
        "drug",
        "ওষুধ",
        "ওষুধ লাগবে",
        "ওষুধ দরকার",
        "ওষুধ প্রয়োজন",
        "ওষুধ চাই"
    ],

    "Shelter Needed": [
        "shelter",
        "place to stay",
        "somewhere to stay",
        "safe place to stay",
        "place for shelter",
        "homeless",
        "no place to stay",
        "stay tonight",
        "need shelter",
        "থাকার জায়গা",
        "থাকার জায়গা দরকার",
        "থাকার জায়গা লাগবে",
        "আশ্রয়",
        "আশ্রয় দরকার",
        "আশ্রয় লাগবে",
        "বাড়ি নেই"
    ],

    "Rescue Needed": [
        "rescue",
        "trapped",
        "stuck",
        "cannot get out",
        "can't get out",
        "unable to escape",
        "need rescue",
        "rescue needed",
        "আটকে",
        "আটকা",
        "আটকে আছি",
        "বের হতে পারছি না",
        "বের হতে পারতেছি না",
        "উদ্ধার",
        "উদ্ধার দরকার",
        "উদ্ধার লাগবে"
    ],

    "Volunteer Assistance": [
        "volunteer",
        "volunteers",
        "need volunteers",
        "people to help",
        "people needed to help",
        "need people",
        "helping people",
        "স্বেচ্ছাসেবক",
        "স্বেচ্ছাসেবক দরকার",
        "মানুষ দরকার",
        "সাহায্য করার মানুষ",
        "সাহায্যের মানুষ"
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
        "pain",
        "medical help",
        "medical assistance",
        "অসুস্থ",
        "অসুস্থ হয়েছে",
        "আহত",
        "আহত হয়েছে",
        "ডাক্তার",
        "হাসপাতাল",
        "অ্যাম্বুলেন্স",
        "রক্তপাত",
        "রোগী",
        "ব্যথা",
        "চিকিৎসা",
        "চিকিৎসা দরকার",
        "চিকিৎসা লাগবে"
    ],

    "Flood": [
        "flood",
        "flooded",
        "flooding",
        "water entered",
        "water entered the house",
        "water level",
        "flood water",
        "river overflow",
        "বন্যা",
        "বন্যা হয়েছে",
        "প্লাবিত",
        "পানি ঢুকেছে",
        "বাড়িতে পানি ঢুকেছে",
        "পানি বাড়ছে",
        "নদীর পানি বেড়েছে"
    ],

    "Fire": [
        "fire",
        "burning",
        "flames",
        "building on fire",
        "house on fire",
        "আগুন",
        "আগুন লেগেছে",
        "জ্বলছে",
        "পুড়ছে",
        "বাড়িতে আগুন"
    ],

    "Earthquake": [
        "earthquake",
        "earthquake happened",
        "earthquake occurred",
        "ভূমিকম্প",
        "ভূমিকম্প হয়েছে"
    ],

    "Accident": [
        "accident",
        "crash",
        "collision",
        "road accident",
        "car accident",
        "bike accident",
        "motorcycle accident",
        "দুর্ঘটনা",
        "এক্সিডেন্ট",
        "সড়ক দুর্ঘটনা"
    ],

    "Missing Person": [
        "missing person",
        "missing",
        "lost person",
        "can't find",
        "cannot find",
        "lost child",
        "missing child",
        "নিখোঁজ",
        "হারিয়ে গেছে",
        "খুঁজে পাচ্ছি না",
        "শিশু নিখোঁজ"
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
    "অনেক রক্তপাত",
    "প্রচুর রক্তপাত",
    "আটকে আছি",
    "আটকে আছে",
    "জরুরি",
    "জরুরি সাহায্য"
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
    "rescue",
    "trapped",

    "আহত",
    "অসুস্থ",
    "বন্যা",
    "আগুন",
    "দুর্ঘটনা",
    "ওষুধ",
    "রক্ত",
    "ক্ষুধা",
    "পানি নেই",
    "উদ্ধার",
    "আটকে"
]


# =========================================================
# KEYWORD CHECK
# =========================================================

def contains_keyword(text, keywords):

    text_lower = text.lower().strip()

    for keyword in keywords:

        if keyword.lower() in text_lower:
            return True

    return False


# =========================================================
# DIRECT KEYWORD DETECTION
# =========================================================

def detect_keyword_needs(text):

    detected = []

    for category, keywords in KEYWORDS.items():

        if contains_keyword(text, keywords):

            detected.append(category)

    return detected


# =========================================================
# AI DETECTION
# =========================================================

def detect_ai_need(text):

    try:

        ai_result = classifier(
            text,
            CATEGORIES,
            hypothesis_template="This person's situation is about {}."
        )

        top_label = ai_result["labels"][0]
        top_score = ai_result["scores"][0]

        if top_score >= 0.50:

            return top_label, top_score

    except Exception:

        pass

    return None, 0


# =========================================================
# DETECT ALL NEEDS
# =========================================================

def detect_needs(text):

    detected = []

    # -----------------------------------------------------
    # 1. Direct keyword detection
    # -----------------------------------------------------

    keyword_needs = detect_keyword_needs(text)

    for need in keyword_needs:

        if need not in detected:

            detected.append(need)


    # -----------------------------------------------------
    # 2. AI detection
    #
    # AI is used only when keyword detection does not
    # clearly identify the situation.
    # -----------------------------------------------------

    ai_label, ai_score = detect_ai_need(text)

    if ai_label:

        # Do not allow AI to replace clear keyword matches
        if not detected:

            detected.append(ai_label)


    # -----------------------------------------------------
    # 3. Blood automatically means medical support
    # -----------------------------------------------------

    if "Blood Assistance" in detected:

        if "Medical Emergency" not in detected:

            detected.append("Medical Emergency")


    # -----------------------------------------------------
    # 4. Medicine automatically means medical support
    # -----------------------------------------------------

    if "Medicine Assistance" in detected:

        if "Medical Emergency" not in detected:

            detected.append("Medical Emergency")


    # -----------------------------------------------------
    # 5. Flood + trapped means rescue
    # -----------------------------------------------------

    if "Flood" in detected:

        rescue_words = [
            "trapped",
            "stuck",
            "cannot get out",
            "can't get out",
            "unable to escape",
            "আটকে",
            "আটকা",
            "বের হতে পারছি না",
            "উদ্ধার"
        ]

        if contains_keyword(text, rescue_words):

            if "Rescue Needed" not in detected:

                detected.append("Rescue Needed")


    # -----------------------------------------------------
    # Remove duplicates
    # -----------------------------------------------------

    unique_needs = []

    for need in detected:

        if need not in unique_needs:

            unique_needs.append(need)


    # -----------------------------------------------------
    # Fallback
    # -----------------------------------------------------

    if not unique_needs:

        unique_needs = ["General Emergency"]


    return unique_needs


# =========================================================
# PRIMARY CRISIS
# =========================================================

def detect_primary_crisis(text, needs):

    # -----------------------------------------------------
    # Physical crisis gets highest priority
    # -----------------------------------------------------

    crisis_categories = [
        "Fire",
        "Earthquake",
        "Flood",
        "Accident",
        "Missing Person"
    ]

    for crisis in crisis_categories:

        if crisis in needs:

            return crisis


    # -----------------------------------------------------
    # Medical emergencies
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # Critical
    # -----------------------------------------------------

    for word in CRITICAL_WORDS:

        if word.lower() in text_lower:

            return "Critical"


    # -----------------------------------------------------
    # High
    # -----------------------------------------------------

    for word in HIGH_WORDS:

        if word.lower() in text_lower:

            return "High"


    # -----------------------------------------------------
    # Serious categories
    # -----------------------------------------------------

    serious_needs = [
        "Medical Emergency",
        "Blood Assistance",
        "Rescue Needed",
        "Fire",
        "Accident",
        "Earthquake"
    ]

    for need in serious_needs:

        if need in needs:

            return "High"


    # -----------------------------------------------------
    # Multiple needs
    # -----------------------------------------------------

    if len(needs) >= 3:

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


    if not descriptions:

        reason = "an emergency situation"

    elif len(descriptions) == 1:

        reason = descriptions[0]

    elif len(descriptions) == 2:

        reason = (
            descriptions[0]
            + " and "
            + descriptions[1]
        )

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


    # -----------------------------------------------------
    # Empty input
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # Detect needs
    # -----------------------------------------------------

    needs = detect_needs(text)


    # -----------------------------------------------------
    # Detect primary crisis
    # -----------------------------------------------------

    primary_crisis = detect_primary_crisis(
        text,
        needs
    )


    # -----------------------------------------------------
    # Detect severity
    # -----------------------------------------------------

    severity = detect_severity(
        text,
        needs
    )


    # -----------------------------------------------------
    # Required support
    # -----------------------------------------------------

    required_help = get_required_support(
        needs
    )


    # -----------------------------------------------------
    # AI match strength
    #
    # This is NOT shown as raw probability.
    # -----------------------------------------------------

    try:

        ai_result = classifier(
            text,
            CATEGORIES,
            hypothesis_template="This person's situation is about {}."
        )

        score = ai_result["scores"][0]


        if score >= 0.70:

            match_strength = "Strong"

        elif score >= 0.45:

            match_strength = "Good"

        else:

            match_strength = "Moderate"

    except Exception:

        match_strength = "Good"


    # -----------------------------------------------------
    # Explanation
    # -----------------------------------------------------

    explanation = generate_explanation(
        text,
        needs,
        severity
    )


    # -----------------------------------------------------
    # Final result
    # -----------------------------------------------------

    return {

        "type": primary_crisis,

        "needs": needs,

        # Kept for compatibility with old app.py
        "confidence": 0,

        "match_strength": match_strength,

        "severity": severity,

        "required_help": required_help,

        "explanation": explanation
    }

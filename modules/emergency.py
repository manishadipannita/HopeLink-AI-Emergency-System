from transformers import pipeline


# ==========================
# LOAD AI MODEL
# ==========================

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    device=-1
)


# ==========================
# ANALYZE EMERGENCY
# ==========================

def analyze_emergency(text):

    text = text.strip()

    if not text:
        return {
            "type": "Unknown",
            "confidence": 0,
            "severity": "Low",
            "required_help": [
                "Please describe your situation"
            ]
        }


    # ==========================
    # POSSIBLE EMERGENCY TYPES
    # ==========================

    categories = [
        "Food Assistance",
        "Water Assistance",
        "Blood Assistance",
        "Medical Emergency",
        "Medicine Assistance",
        "Shelter Needed",
        "Rescue Needed",
        "Volunteer Assistance",
        "Flood",
        "Fire",
        "Earthquake",
        "Accident",
        "Missing Person",
        "General Emergency"
    ]


    # ==========================
    # AI CLASSIFICATION
    # ==========================

    result = classifier(
        text,
        categories,
        hypothesis_template="This person's situation is about {}."
    )


    emergency_type = result["labels"][0]

    confidence = round(
        result["scores"][0] * 100,
        2
    )


    # ==========================
    # SEVERITY ANALYSIS
    # ==========================

    text_lower = text.lower()


    critical_words = [
        "trapped",
        "dying",
        "unconscious",
        "not breathing",
        "severe bleeding",
        "heavy bleeding",
        "critical",
        "life threatening",
        "life-threatening",
        "can't breathe",
        "cannot breathe",
        "fire",
        "stuck",
        "help me urgently"
    ]


    high_words = [
        "urgent",
        "urgently",
        "emergency",
        "injured",
        "seriously hurt",
        "danger",
        "dangerous",
        "no food",
        "no water",
        "homeless"
    ]


    if any(word in text_lower for word in critical_words):

        severity = "Critical"

    elif any(word in text_lower for word in high_words):

        severity = "High"

    else:

        severity = "Low"


    # ==========================
    # REQUIRED SUPPORT
    # ==========================

    support = {

        "Food Assistance": [
            "Food Supply",
            "Food Distribution",
            "Local Volunteers"
        ],

        "Water Assistance": [
            "Clean Drinking Water",
            "Water Distribution",
            "Local Volunteers"
        ],

        "Blood Assistance": [
            "Blood Donor",
            "Hospital Support",
            "Medical Assistance"
        ],

        "Medical Emergency": [
            "Medical Support",
            "Ambulance",
            "Doctor Assistance"
        ],

        "Medicine Assistance": [
            "Medicine Supply",
            "Pharmacy Support",
            "Medical Assistance"
        ],

        "Shelter Needed": [
            "Temporary Shelter",
            "Food Supply",
            "Basic Necessities"
        ],

        "Rescue Needed": [
            "Rescue Team",
            "Emergency Responders",
            "Emergency Transport"
        ],

        "Volunteer Assistance": [
            "Local Volunteers",
            "Humanitarian Organizations",
            "Emergency Support"
        ],

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
            "Ambulance"
        ],

        "Missing Person": [
            "Search and Rescue Team",
            "Local Volunteers",
            "Emergency Authorities"
        ],

        "General Emergency": [
            "Emergency Support",
            "Local Volunteers"
        ]
    }


    return {

        "type": emergency_type,

        "confidence": confidence,

        "severity": severity,

        "required_help": support.get(
            emergency_type,
            ["General Emergency Support"]
        )

    }

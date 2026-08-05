from transformers import pipeline


# Load AI model
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    device=-1
)



def analyze_emergency(text):

    categories = [
        "Flood",
        "Fire",
        "Medical Emergency",
        "Earthquake",
        "Accident",
        "Shelter Needed"
    ]


    result = classifier(
        text,
        categories
    )


    emergency_type = result["labels"][0]
    confidence = round(
        result["scores"][0] * 100,
        2
    )


    severity = "Low"


    if confidence > 70:
        severity = "High"

    if any(
        word in text.lower()
        for word in [
            "trapped",
            "dying",
            "critical",
            "urgent",
            "child",
            "fire"
        ]
    ):
        severity = "Critical"



    support = {

        "Flood": [
            "Food Supply",
            "Temporary Shelter",
            "Rescue Team"
        ],

        "Fire": [
            "Fire Service",
            "Rescue Team",
            "Emergency Transport"
        ],

        "Medical Emergency": [
            "Medical Support",
            "Ambulance",
            "Doctor Assistance"
        ],

        "Earthquake": [
            "Rescue Team",
            "Shelter",
            "Medical Support"
        ],

        "Accident": [
            "Emergency Transport",
            "Medical Support"
        ],

        "Shelter Needed": [
            "Temporary Shelter",
            "Food Supply"
        ]

    }


    return {

        "type": emergency_type,

        "confidence": confidence,

        "severity": severity,

        "required_help":
        support.get(
            emergency_type,
            [
                "General Emergency Support"
            ]
        )

    }
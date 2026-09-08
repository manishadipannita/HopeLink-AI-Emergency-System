def recommend_resources(emergency_type, severity="Medium"):

    resources = {

        "Flood": {
            "Emergency Centers": [
                "Temporary Shelter Center",
                "Disaster Management Support Center"
            ],
            "Available Help": [
                "Food Distribution Team",
                "Rescue Boat Team",
                "Medical Support Team"
            ]
        },

        "Fire": {
            "Emergency Centers": [
                "Fire Service Station",
                "Emergency Response Center"
            ],
            "Available Help": [
                "Fire Fighting Team",
                "Rescue Team",
                "Medical Support"
            ]
        },

        "Medical Emergency": {
            "Emergency Centers": [
                "Nearest Hospital",
                "Emergency Medical Center"
            ],
            "Available Help": [
                "Doctor",
                "Ambulance Service",
                "Medical Volunteer"
            ]
        },

        "Accident": {
            "Emergency Centers": [
                "Emergency Hospital",
                "Trauma Center"
            ],
            "Available Help": [
                "Ambulance",
                "First Aid Team",
                "Rescue Team"
            ]
        },

        "Food Shortage": {
            "Emergency Centers": [
                "Relief Distribution Center"
            ],
            "Available Help": [
                "Food Supply Team",
                "Humanitarian Volunteers"
            ]
        },

        "Shelter Needed": {
            "Emergency Centers": [
                "Temporary Shelter Center",
                "Relief Shelter"
            ],
            "Available Help": [
                "Shelter Volunteers",
                "Humanitarian Support Team"
            ]
        },

        "Volunteer Support": {
            "Emergency Centers": [
                "Local Volunteer Coordination Center"
            ],
            "Available Help": [
                "Community Volunteers",
                "Humanitarian Volunteers"
            ]
        },

        "General Emergency": {
            "Emergency Centers": [
                "Local Emergency Support Center"
            ],
            "Available Help": [
                "General Volunteers",
                "Emergency Response Team"
            ]
        }
    }

    result = resources.get(
        emergency_type,
        resources["General Emergency"]
    )

    return {
        "severity": severity,
        "centers": result["Emergency Centers"],
        "help": result["Available Help"]
    }

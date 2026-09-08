def get_emergency_tips(emergency_type):

    tips = {

        "Flood": [
            "🌊 Move to higher and safer ground",
            "💧 Avoid drinking or walking through contaminated flood water",
            "⚡ Turn off electricity if it is safe to do so",
            "🚨 Follow instructions from local rescue and emergency services"
        ],

        "Fire": [
            "🔥 Leave the building immediately",
            "🚪 Use emergency exits and never use elevators",
            "😷 Stay low to avoid smoke",
            "📞 Contact the local fire service and emergency responders"
        ],

        "Medical Emergency": [
            "🏥 Seek medical assistance immediately",
            "🩹 Provide first aid only if it is safe and you know how",
            "🧘 Keep the injured or sick person calm",
            "🚑 Contact emergency medical services if the situation is serious"
        ],

        "Accident": [
            "🚧 Move away from immediate danger if it is safe",
            "🩹 Avoid moving seriously injured people unless necessary for safety",
            "📞 Contact emergency medical and rescue services",
            "🚑 Request an ambulance if medical attention is needed"
        ],

        "Earthquake": [
            "🛡️ Drop, cover and hold on during shaking",
            "🏠 Move away from damaged buildings after the shaking stops",
            "📱 Keep communication devices available",
            "🚨 Follow instructions from emergency authorities"
        ],

        "Food Shortage": [
            "🍚 Contact a verified food relief or distribution center",
            "🤝 Reach out to trusted humanitarian organizations",
            "💧 Make sure children and vulnerable people have access to safe water",
            "📞 Contact local support services if food access is critical"
        ],

        "Shelter Needed": [
            "🏠 Move to a safe temporary shelter if your current location is unsafe",
            "🚨 Avoid damaged or dangerous buildings",
            "🤝 Contact verified humanitarian or shelter support organizations",
            "📱 Keep important communication devices and documents safe"
        ],

        "Volunteer Assistance": [
            "🤝 Contact trusted volunteer or humanitarian support groups",
            "📍 Clearly explain what type of help is needed",
            "📞 Contact emergency services first if there is immediate danger",
            "🛡️ Avoid entering dangerous areas without proper support"
        ],

        "Rescue Assistance": [
            "🚨 Contact local emergency or rescue services immediately",
            "🛡️ Move to the safest possible location",
            "📱 Keep your phone available for emergency communication",
            "⚠️ Do not enter dangerous areas without trained rescuers"
        ],

        "Blood Assistance": [
            "🩸 Contact the hospital or a verified blood donation network",
            "🏥 Follow the hospital's instructions regarding blood requirements",
            "📞 Ask trusted donors or verified organizations for assistance",
            "🚑 Seek immediate medical care if the patient is in critical condition"
        ],

        "General Emergency": [
            "⚠️ Stay calm and assess immediate danger",
            "📞 Contact local emergency services if the situation is urgent",
            "🛡️ Move to a safe location",
            "📱 Keep your phone available for emergency communication"
        ]
    }

    return tips.get(
        emergency_type,
        tips["General Emergency"]
    )

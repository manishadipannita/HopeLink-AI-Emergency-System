def get_emergency_tips(emergency_type):

    tips = {

        "Flood": [
            "🌊 Move to higher and safer ground",
            "💧 Keep clean drinking water",
            "⚡ Turn off electricity if water enters home",
            "📄 Keep important documents safe"
        ],


        "Fire": [
            "🔥 Leave the building immediately",
            "🚪 Use emergency exits",
            "😷 Stay low to avoid smoke",
            "📞 Contact fire service"
        ],


        "Medical": [
            "🏥 Call emergency medical support",
            "🩹 Provide first aid if possible",
            "🧘 Keep the patient calm",
            "🚑 Arrange emergency transport"
        ],


        "Earthquake": [
            "🏠 Move away from damaged buildings",
            "🛡️ Drop, cover and hold",
            "📱 Keep communication devices ready",
            "🚨 Follow safety instructions"
        ]

    }


    return tips.get(
        emergency_type,
        [
            "⚠️ Stay calm",
            "📞 Contact emergency services",
            "🛡️ Move to a safe location"
        ]
    )
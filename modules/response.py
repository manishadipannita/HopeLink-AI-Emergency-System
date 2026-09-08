def generate_response(emergency_type, severity):

    responses = {

        "Flood":
        "Please move to a safe and elevated location and avoid walking or driving through flood water. Rescue, shelter, food and medical support may be required.",

        "Fire":
        "Please leave the building immediately and move to a safe location. Avoid smoke and do not use elevators. Contact the fire service and emergency responders.",

        "Medical Emergency":
        "Please stay calm and seek medical assistance immediately. Contact local emergency medical services or go to the nearest hospital.",

        "Accident":
        "Please move to a safe location if possible and avoid further injury. Contact emergency medical services and request ambulance or rescue assistance.",

        "Food Shortage":
        "Food assistance may be required. Please contact a verified relief organization, food distribution center or humanitarian volunteer team.",

        "Shelter Needed":
        "Safe shelter may be required. Please contact a verified temporary shelter or humanitarian support organization and avoid unsafe buildings or areas.",

        "Volunteer Assistance":
        "HopeLink identified a need for general assistance. A volunteer or humanitarian support team may be able to help. If the situation is urgent or dangerous, contact local emergency services first.",

        "Rescue Assistance":
        "Rescue assistance may be required. Move to the safest possible location, avoid dangerous areas and contact local emergency or rescue services immediately.",

        "Blood Assistance":
        "Blood support may be required. Please contact the hospital or verified blood donation network and seek medical guidance immediately.",

        "General Emergency":
        "Please stay calm and move to a safe location. Contact local emergency services if the situation is urgent. HopeLink can help identify relevant support needs."
    }

    message = responses.get(
        emergency_type,
        responses["General Emergency"]
    )

    return {
        "message": message,
        "priority": severity
    }

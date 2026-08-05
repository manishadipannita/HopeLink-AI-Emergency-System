def generate_response(emergency_type, severity):


    responses = {


        "Flood":
        "We understand your situation. Please move to a safe place and avoid flood water. Emergency support for food, shelter and rescue has been identified.",


        "Fire":
        "Please leave the area immediately and move to a safe location. Contact fire service and emergency rescue support.",


        "Medical Emergency":
        "Please stay calm. Seek medical assistance immediately and contact emergency medical services.",


        "Accident":
        "Emergency assistance is required. Please ensure safety and contact medical support.",

    }


    message = responses.get(
        emergency_type,
        "Please stay safe. Emergency support resources are being identified."
    )


    return {

        "message": message,

        "priority": severity

    }
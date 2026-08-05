def match_volunteer(text):

    text_lower = text.lower()


    volunteer_type = "General Volunteer"

    skills = []


    # Food support
    if any(word in text_lower for word in [
        "food",
        "meal",
        "rice",
        "water",
        "cook"
    ]):
        volunteer_type = "Food Support Volunteer"
        skills.append("Food Distribution")


    # Medical support
    if any(word in text_lower for word in [
        "medicine",
        "doctor",
        "medical",
        "health",
        "nurse"
    ]):
        volunteer_type = "Medical Support Volunteer"
        skills.append("Medical Assistance")


    # Rescue support
    if any(word in text_lower for word in [
        "rescue",
        "transport",
        "boat",
        "vehicle"
    ]):
        volunteer_type = "Rescue Volunteer"
        skills.append("Emergency Rescue")


    # Shelter support
    if any(word in text_lower for word in [
        "shelter",
        "house",
        "place",
        "accommodation"
    ]):
        volunteer_type = "Shelter Support Volunteer"
        skills.append("Shelter Management")


    if not skills:
        skills.append("General Emergency Support")


    return {

        "volunteer_type": volunteer_type,

        "skills": skills,

        "matched_emergency": (
            "Disaster affected people "
            "requiring immediate support"
        )

    }
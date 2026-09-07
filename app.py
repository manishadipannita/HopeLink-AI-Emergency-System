import streamlit as st
from PIL import Image

from modules.emergency import analyze_emergency
from modules.volunteer import match_volunteer
from modules.report import generate_report, create_pdf
from modules.resources import recommend_resources
from modules.response import generate_response
from modules.emergency_tips import get_emergency_tips


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="HopeLink AI",
    page_icon="💙",
    layout="wide"
)


# =========================================================
# SIDEBAR LOGO
# =========================================================

try:

    logo = Image.open("HopeLink_logo.png")

    st.sidebar.image(
        logo,
        width=180
    )

except Exception:

    try:

        logo = Image.open("hopelink_logo.png")

        st.sidebar.image(
            logo,
            width=180
        )

    except Exception:

        st.sidebar.markdown(
            "## 💙 HopeLink AI"
        )


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("HopeLink AI")

st.sidebar.write(
    "AI-powered humanitarian support "
    "and emergency coordination."
)

st.sidebar.markdown("---")

st.sidebar.info(
    "HopeLink analyzes crisis descriptions "
    "and identifies relevant support needs."
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "⚠️ In a real emergency, contact local "
    "emergency services first."
)


# =========================================================
# MAIN HEADER
# =========================================================

st.title("💙 HopeLink AI")

st.subheader(
    "AI-powered crisis analysis and emergency support platform"
)

st.write(
    "HopeLink helps people describe their situation "
    "in their own words and identifies the types "
    "of support they may need."
)


# =========================================================
# ROLE SELECTION
# =========================================================

role = st.radio(
    "Choose your role:",
    [
        "🆘 I Need Help",
        "🤝 I Can Help"
    ],
    horizontal=True
)


# =========================================================
# I NEED HELP
# =========================================================

if role == "🆘 I Need Help":

    st.markdown("---")

    st.header("🚨 Describe Your Emergency")

    st.write(
        "Tell HopeLink what you need. "
        "You can describe your situation in your own words."
    )


    # =====================================================
    # EMERGENCY INPUT
    # =====================================================

    emergency_text = st.text_area(
        "Explain your situation:",
        placeholder=(
            "Example: My father is injured after the flood "
            "and we need medicine and a place to stay."
        ),
        height=150
    )


    # =====================================================
    # ANALYZE BUTTON
    # =====================================================

    if st.button(
        "🔍 Analyze My Situation",
        type="primary",
        use_container_width=True
    ):

        if not emergency_text.strip():

            st.warning(
                "Please describe your emergency first."
            )

        else:

            with st.spinner(
                "🧠 HopeLink AI is understanding your situation..."
            ):

                result = analyze_emergency(
                    emergency_text
                )

            st.session_state["result"] = result

            st.session_state[
                "emergency_text"
            ] = emergency_text


    # =====================================================
    # DISPLAY RESULT
    # =====================================================

    if "result" in st.session_state:

        result = st.session_state["result"]


        # =================================================
        # SUCCESS MESSAGE
        # =================================================

        st.success(
            "Emergency Analysis Completed"
        )


        # =================================================
        # AI UNDERSTANDING
        # =================================================

        st.markdown("---")

        st.header("🧠 AI Understanding")

        st.write(
            "HopeLink identified the following crisis "
            "and support needs:"
        )


        # =================================================
        # PRIMARY CRISIS
        # =================================================

        st.markdown(
            f"### 🚨 Primary Crisis: **{result.get('type', 'General Emergency')}**"
        )


        # =================================================
        # DETECTED NEEDS
        # =================================================

        st.markdown(
            "### 🤝 Detected Needs"
        )

        needs = result.get(
            "needs",
            [result.get("type", "General Emergency")]
        )


        for need in needs:

            st.markdown(
                f"- ✅ **{need}**"
            )


        # =================================================
        # AI ASSESSMENT
        # =================================================

        st.markdown("---")

        st.markdown(
            "### 🤖 AI Assessment"
        )


        match_strength = result.get(
            "match_strength",
            "Good"
        )


        if match_strength == "Strong":

            st.success(
                "🟢 Strong Match"
            )

        elif match_strength == "Good":

            st.info(
                "🔵 Good Match"
            )

        else:

            st.warning(
                "🟡 Moderate Match"
            )


        # =================================================
        # PRIORITY
        # =================================================

        st.markdown(
            "### ⚠️ Priority Level"
        )


        severity = result.get(
            "severity",
            "Medium"
        )


        if severity == "Critical":

            st.error(
                "🔴 CRITICAL"
            )

        elif severity == "High":

            st.warning(
                "🟠 HIGH"
            )

        elif severity == "Medium":

            st.info(
                "🟡 MEDIUM"
            )

        else:

            st.success(
                "🟢 LOW"
            )


        # =================================================
        # WHY HOPELINK RECOMMENDED THIS
        # =================================================

        st.markdown("---")

        st.header(
            "💡 Why HopeLink Recommended This"
        )


        st.info(
            result.get(
                "explanation",
                "HopeLink analyzed the situation "
                "and identified relevant support."
            )
        )


        # =================================================
        # REQUIRED SUPPORT
        # =================================================

        st.markdown("---")

        st.header(
            "🤝 Required Support"
        )


        required_help = result.get(
            "required_help",
            []
        )


        if required_help:

            for item in required_help:

                st.markdown(
                    f"✅ **{item}**"
                )

        else:

            st.write(
                "General emergency support"
            )


        # =================================================
        # RECOMMENDED RESOURCES
        # =================================================

        st.markdown("---")

        st.header(
            "📍 Recommended Resources"
        )


        try:

            resource = recommend_resources(
                result.get(
                    "type",
                    "General Emergency"
                )
            )


            # ---------------------------------------------
            # Handle dictionary response
            # ---------------------------------------------

            if isinstance(resource, dict):

                centers = resource.get(
                    "centers",
                    resource.get(
                        "emergency_centers",
                        []
                    )
                )

                help_list = resource.get(
                    "help",
                    resource.get(
                        "available_help",
                        []
                    )
                )

            else:

                centers = []

                help_list = []


            # ---------------------------------------------
            # Emergency Centers
            # ---------------------------------------------

            if centers:

                st.markdown(
                    "### 🏢 Emergency Centers"
                )


                for center in centers:

                    st.markdown(
                        f"🏠 **{center}**"
                    )


            # ---------------------------------------------
            # Available Help
            # ---------------------------------------------

            if help_list:

                st.markdown(
                    "### 🤝 Available Help"
                )


                for helper in help_list:

                    st.markdown(
                        f"🛟 **{helper}**"
                    )


            # ---------------------------------------------
            # No resources
            # ---------------------------------------------

            if not centers and not help_list:

                st.info(
                    "No specific resources are currently "
                    "available for this emergency type."
                )


        except Exception:

            st.info(
                "Resource recommendations are "
                "currently unavailable."
            )


        # =================================================
        # AI RESPONSE
        # =================================================

        st.markdown("---")

        st.header(
            "💙 HopeLink AI Response"
        )


        try:

            response = generate_response(
                result.get(
                    "type",
                    "General Emergency"
                ),
                result.get(
                    "severity",
                    "Medium"
                )
            )


            # ---------------------------------------------
            # If response is a dictionary
            # ---------------------------------------------

            if isinstance(response, dict):

                message = response.get(
                    "message",
                    "Please stay safe and seek "
                    "appropriate emergency support."
                )

                priority = response.get(
                    "priority",
                    result.get(
                        "severity",
                        "Medium"
                    )
                )


                st.success(
                    message
                )


                st.caption(
                    f"Priority Level: {priority}"
                )


            # ---------------------------------------------
            # If response is normal text
            # ---------------------------------------------

            else:

                st.success(
                    response
                )


                st.caption(
                    f"Priority Level: "
                    f"{result.get('severity', 'Medium')}"
                )


        except Exception:

            st.success(
                "We understand your situation. "
                "Please move to a safe place and "
                "seek appropriate emergency support."
            )


        # =================================================
        # SAFETY TIPS
        # =================================================

        st.markdown("---")

        st.header(
            "🛡️ Emergency Safety Tips"
        )


        try:

            tips = get_emergency_tips(
                result.get(
                    "type",
                    "General Emergency"
                )
            )


            if tips:

                for tip in tips:

                    st.markdown(
                        f"📌 {tip}"
                    )

            else:

                st.info(
                    "Please prioritize your safety "
                    "and contact local emergency services."
                )


        except Exception:

            st.info(
                "Please prioritize your safety "
                "and contact local emergency services."
            )


        # =================================================
        # REPORT GENERATOR
        # =================================================

        st.markdown("---")

        st.header(
            "📋 Emergency Report Generator"
        )


        st.write(
            "Generate a downloadable summary "
            "of the analyzed emergency."
        )


        if st.button(
            "📄 Generate Emergency Report",
            use_container_width=True
        ):

            try:

                report = generate_report(
                    st.session_state.get(
                        "emergency_text",
                        ""
                    ),
                    result
                )


                pdf_file = create_pdf(
                    report
                )


                st.download_button(
                    label="⬇️ Download Emergency Report",
                    data=pdf_file,
                    file_name="HopeLink_Emergency_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )


            except Exception as e:

                st.error(
                    f"Could not generate report: {e}"
                )


# =========================================================
# I CAN HELP
# =========================================================

else:

    st.markdown("---")

    st.header(
        "🤝 I Can Help"
    )

    st.write(
        "Tell HopeLink how you can help people "
        "during an emergency."
    )


    # =====================================================
    # VOLUNTEER NAME
    # =====================================================

    volunteer_name = st.text_input(
        "Your Name"
    )


    # =====================================================
    # LOCATION
    # =====================================================

    volunteer_location = st.text_input(
        "Your Location"
    )


    # =====================================================
    # HELP OPTIONS
    # =====================================================

    st.markdown(
        "### What kind of help can you provide?"
    )


    help_options = st.multiselect(
        "Select your available support:",
        [
            "🍚 Food Support",
            "💧 Water Support",
            "🩸 Blood Donation",
            "💊 Medicine Support",
            "🏠 Shelter Support",
            "🛟 Rescue Support",
            "🚗 Transportation",
            "👥 Volunteer / Physical Help",
            "🏥 Medical Support"
        ]
    )


    # =====================================================
    # AVAILABILITY
    # =====================================================

    availability = st.selectbox(
        "Availability:",
        [
            "Available Now",
            "Available Today",
            "Available Later"
        ]
    )


    # =====================================================
    # REGISTER
    # =====================================================

    if st.button(
        "🤝 Register as a Helper",
        type="primary",
        use_container_width=True
    ):

        if not volunteer_name.strip():

            st.warning(
                "Please enter your name."
            )

        elif not help_options:

            st.warning(
                "Please select at least one type of help."
            )

        else:

            st.success(
                f"Thank you, {volunteer_name}! "
                "Your willingness to help has been recorded."
            )


            st.markdown(
                "### 💙 Your Support"
            )


            st.write(
                f"📍 Location: "
                f"{volunteer_location or 'Not provided'}"
            )


            st.write(
                f"⏱️ Availability: {availability}"
            )


            for item in help_options:

                st.write(
                    f"✅ {item}"
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "💙 HopeLink AI — Turning crisis information "
    "into meaningful support."
)

st.caption(
    "Prototype for humanitarian and social-impact applications."
)

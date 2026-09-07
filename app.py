import streamlit as st
from PIL import Image

from modules.emergency import analyze_emergency
from modules.volunteer import match_volunteer
from modules.report import generate_report, create_pdf
from modules.resources import recommend_resources
from modules.response import generate_response
from modules.emergency_tips import get_emergency_tips


# ==========================
# PAGE CONFIGURATION
# ==========================

st.set_page_config(
    page_title="HopeLink AI",
    page_icon="🌍",
    layout="wide"
)


# ==========================
# CSS STYLE
# ==========================

st.markdown(
    """
    <style>

    .title {
        text-align: center;
        font-size: 38px;
        font-weight: 700;
        color: #1f4e79;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #666;
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    try:

        logo = Image.open("hopelink_logo.png")

        st.image(
            logo,
            width=150
        )

    except Exception:

        st.write("🌍")


    st.title("HopeLink AI")


    st.write(
        """
        🌍 **AI Emergency Network**

        **Features:**

        ✅ Crisis Detection  
        ✅ Severity Analysis  
        ✅ Resource Matching  
        ✅ Volunteer Connection  
        ✅ Emergency Safety Tips  
        ✅ Emergency Report
        """
    )


    st.info(
        "AI-powered support during emergencies."
    )


# ==========================
# MAIN HEADER
# ==========================

st.markdown(
    """
    <div class="title">
        HopeLink AI Emergency Response System
    </div>

    <div class="subtitle">
        AI-powered crisis analysis and emergency support platform
    </div>
    """,
    unsafe_allow_html=True
)


st.write("")


# ==========================
# ROLE SELECTION
# ==========================

mode = st.selectbox(
    "Choose your role:",
    [
        "🆘 I Need Help",
        "🤝 I Can Help"
    ]
)


# ==========================================================
# NEED HELP MODE
# ==========================================================

if mode == "🆘 I Need Help":

    st.header(
        "🚨 Describe Your Emergency"
    )


    st.write(
        "Tell HopeLink what you need. You can describe your situation "
        "in your own words."
    )


    emergency_text = st.text_area(
        "Explain your situation:",
        placeholder=(
            "Example: My village is flooded and families need "
            "food and shelter."
        ),
        height=150
    )


    # ==========================
    # ANALYZE EMERGENCY
    # ==========================

    if st.button(
        "🔍 Analyze Emergency",
        use_container_width=True
    ):

        if emergency_text.strip():

            with st.spinner(
                "AI is analyzing the crisis..."
            ):

                result = analyze_emergency(
                    emergency_text
                )


            # Save result
            st.session_state["result"] = result


            st.success(
                "Emergency Analysis Completed"
            )


            # ==========================
            # EMERGENCY TYPE + CONFIDENCE
            # ==========================

            col1, col2 = st.columns(2)


            with col1:

                st.subheader(
                    "🚨 Emergency / Support Type"
                )

                st.info(
                    result["type"]
                )


            with col2:

                st.subheader(
                    "🤖 AI Classification Confidence"
                )

                st.info(
                    f'{result["confidence"]}%'
                )


            # ==========================
            # SEVERITY
            # ==========================

            st.subheader(
                "⚠️ Severity Level"
            )


            if result["severity"] == "Critical":

                st.error(
                    "🔴 " + result["severity"]
                )


            elif result["severity"] == "High":

                st.warning(
                    "🟠 " + result["severity"]
                )


            else:

                st.success(
                    "🟢 " + result["severity"]
                )


            # ==========================
            # REQUIRED SUPPORT
            # ==========================

            st.subheader(
                "🤝 Required Support"
            )


            for item in result["required_help"]:

                st.write(
                    "✅",
                    item
                )


            # ==========================
            # RECOMMENDED RESOURCES
            # ==========================

            st.divider()


            st.header(
                "📍 Recommended Resources"
            )


            resource = recommend_resources(
                result["type"],
                result["severity"]
            )


            col1, col2 = st.columns(2)


            with col1:

                st.write(
                    "**🏢 Emergency Centers**"
                )


                for center in resource.get(
                    "centers",
                    []
                ):

                    st.write(
                        "🏠",
                        center
                    )


            with col2:

                st.write(
                    "**🤝 Available Help**"
                )


                for help_item in resource.get(
                    "help",
                    []
                ):

                    st.write(
                        "🛟",
                        help_item
                    )


            # ==========================
            # AI RESPONSE
            # ==========================

            st.divider()


            st.header(
                "💙 HopeLink AI Response"
            )


            response = generate_response(
                result["type"],
                result["severity"]
            )


            st.success(
                response["message"]
            )


            st.write(
                "**Priority Level:**",
                response["priority"]
            )


            # ==========================
            # SAFETY TIPS
            # ==========================

            st.divider()


            st.header(
                "🛡️ Emergency Safety Tips"
            )


            tips = get_emergency_tips(
                result["type"]
            )


            for tip in tips:

                st.write(
                    tip
                )


        else:

            st.warning(
                "Please describe your emergency."
            )


    # ======================================================
    # EMERGENCY REPORT GENERATOR
    # ======================================================

    if "result" in st.session_state:

        st.divider()


        st.header(
            "📋 Emergency Report Generator"
        )


        st.write(
            "Generate a downloadable summary of the analyzed emergency."
        )


        if st.button(
            "📄 Generate PDF Report"
        ):

            try:

                report = generate_report(
                    st.session_state["result"]
                )


                pdf_file = create_pdf(
                    report
                )


                st.success(
                    "Report Generated Successfully"
                )


                with open(
                    pdf_file,
                    "rb"
                ) as file:

                    st.download_button(
                        label="📥 Download Emergency Report",
                        data=file,
                        file_name="HopeLink_Emergency_Report.pdf",
                        mime="application/pdf"
                    )


            except Exception as e:

                st.error(
                    f"Could not generate the report: {e}"
                )


# ==========================================================
# VOLUNTEER MODE
# ==========================================================

if mode == "🤝 I Can Help":

    st.header(
        "🤝 Volunteer Registration"
    )


    st.write(
        "Tell HopeLink how you can support people during emergencies."
    )


    volunteer_text = st.text_area(
        "How can you help?",
        placeholder=(
            "Example: I can provide food, medicine and transportation."
        ),
        height=150
    )


    if st.button(
        "🔎 Find Volunteer Match",
        use_container_width=True
    ):

        if volunteer_text.strip():

            with st.spinner(
                "Finding the best volunteer match..."
            ):

                result = match_volunteer(
                    volunteer_text
                )


            st.success(
                "Volunteer Match Found"
            )


            # ==========================
            # VOLUNTEER CATEGORY
            # ==========================

            st.subheader(
                "🤝 Volunteer Category"
            )


            st.info(
                result["volunteer_type"]
            )


            # ==========================
            # SKILLS
            # ==========================

            st.subheader(
                "🛠️ Skills"
            )


            for skill in result["skills"]:

                st.write(
                    "✅",
                    skill
                )


            # ==========================
            # MATCHED EMERGENCY
            # ==========================

            st.subheader(
                "🚨 Recommended For"
            )


            st.write(
                result["matched_emergency"]
            )


        else:

            st.warning(
                "Please enter your support details."
            )


# ==========================
# FOOTER
# ==========================

st.markdown(
    """
    <div class="footer">
        © 2026 HopeLink AI | AI-Powered Emergency Response Network
    </div>
    """,
    unsafe_allow_html=True
)

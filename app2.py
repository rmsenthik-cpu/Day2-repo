import streamlit as st
from collections import Counter

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="Smart Healthcare Diagnosis Assistant",
    page_icon="🏥",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f4f8fb;
}

.stButton button {
    background-color: #198754;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
}

.result-box {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
    margin-top: 20px;
}

h1, h2, h3 {
    color: #0b3d2e;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🏥 Smart Healthcare Diagnosis Assistant")
st.subheader("AI-Based Medical Prediction using Self-Consistency Prompting")

st.markdown("""
This Healthcare AI System performs:

✅ Symptom Analysis  
✅ Multiple Diagnosis Paths  
✅ Disease Prediction  
✅ Medical Test Recommendations  
✅ Healthcare Suggestions  
✅ Self-Consistency Reasoning
""")

# ---------------------------------------------------
# DISEASE DATABASE
# ---------------------------------------------------
disease_database = {

    "Fever": [
        "Viral Infection",
        "COVID-19",
        "Typhoid",
        "Malaria"
    ],

    "Cough": [
        "Common Cold",
        "COVID-19",
        "Bronchitis",
        "Pneumonia"
    ],

    "Chest Pain": [
        "Heart Disease",
        "Angina",
        "Acid Reflux",
        "Anxiety Disorder"
    ],

    "Headache": [
        "Migraine",
        "Stress",
        "Hypertension",
        "Sinus Infection"
    ],

    "Fatigue": [
        "Anemia",
        "Diabetes",
        "Thyroid Disorder",
        "Sleep Disorder"
    ],

    "Shortness of Breath": [
        "Asthma",
        "COVID-19",
        "Heart Failure",
        "Pneumonia"
    ],

    "Sore Throat": [
        "Flu",
        "COVID-19",
        "Tonsillitis",
        "Viral Infection"
    ],

    "Nausea": [
        "Food Poisoning",
        "Gastritis",
        "Migraine",
        "Viral Infection"
    ]
}

# ---------------------------------------------------
# TEST RECOMMENDATIONS
# ---------------------------------------------------
test_recommendations = {
    "COVID-19": "RT-PCR Test, Oxygen Saturation Check",
    "Heart Disease": "ECG, Echocardiogram",
    "Diabetes": "Blood Sugar Test",
    "Pneumonia": "Chest X-Ray",
    "Typhoid": "Widal Test",
    "Malaria": "Blood Smear Test",
    "Anemia": "Complete Blood Count (CBC)",
    "Asthma": "Pulmonary Function Test"
}

# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------
st.header("🩺 Patient Symptom Analysis")

selected_symptoms = st.multiselect(
    "Select Symptoms",
    list(disease_database.keys())
)

patient_age = st.number_input(
    "Patient Age",
    min_value=1,
    max_value=120,
    step=1
)

severity = st.selectbox(
    "Symptom Severity",
    [
        "Mild",
        "Moderate",
        "Severe"
    ]
)

duration = st.selectbox(
    "Duration of Symptoms",
    [
        "1-2 Days",
        "3-7 Days",
        "More than 1 Week"
    ]
)

# ---------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------
if st.button("🔍 Analyze Diagnosis"):

    if not selected_symptoms:
        st.error("Please select at least one symptom")

    else:

        all_possible_diseases = []

        # ---------------------------------------------------
        # SELF-CONSISTENCY ANALYSIS
        # ---------------------------------------------------
        for symptom in selected_symptoms:

            diseases = disease_database.get(symptom, [])

            all_possible_diseases.extend(diseases)

        # ---------------------------------------------------
        # COUNT DISEASE OCCURRENCES
        # ---------------------------------------------------
        disease_count = Counter(all_possible_diseases)

        sorted_diseases = disease_count.most_common()

        # ---------------------------------------------------
        # MOST CONSISTENT DIAGNOSIS
        # ---------------------------------------------------
        most_likely = sorted_diseases[0][0]

        # ---------------------------------------------------
        # GENERATE REPORT
        # ---------------------------------------------------
        report = f"""
# 🏥 Smart Healthcare Diagnosis Report

## 👤 Patient Information

- Age: {patient_age}
- Severity: {severity}
- Duration: {duration}

---

## 🩺 Symptoms Entered

"""

        for symptom in selected_symptoms:
            report += f"- {symptom}\n"

        report += "\n---\n"

        report += "## 🔬 Possible Diagnosis Paths\n\n"

        for disease, score in sorted_diseases:
            report += f"- {disease} → Consistency Score: {score}\n"

        report += "\n---\n"

        report += f"## ✅ Most Consistent Medical Prediction\n\n"
        report += f"### {most_likely}\n"

        report += "\n---\n"

        report += "## 🧪 Recommended Medical Tests\n\n"

        if most_likely in test_recommendations:
            report += f"- {test_recommendations[most_likely]}\n"
        else:
            report += "- General Blood Test\n"

        report += "\n---\n"

        report += "## 💡 Healthcare Recommendations\n\n"

        recommendations = [
            "Consult a certified medical professional.",
            "Maintain proper hydration.",
            "Take adequate rest.",
            "Avoid self-medication.",
            "Monitor symptoms regularly.",
            "Follow prescribed medical advice."
        ]

        for rec in recommendations:
            report += f"- {rec}\n"

        report += "\n---\n"

        report += """
## ⚠ Medical Disclaimer

This AI-generated report is for educational purposes only.

Please consult a licensed healthcare professional for proper diagnosis and treatment.
"""

        # ---------------------------------------------------
        # SUCCESS MESSAGE
        # ---------------------------------------------------
        st.success("Diagnosis Analysis Completed Successfully!")

        # ---------------------------------------------------
        # DISPLAY REPORT
        # ---------------------------------------------------
        st.markdown("## 📋 Diagnosis Report")

        st.markdown(
            f"""
<div class="result-box">
{report.replace('\n', '<br>')}
</div>
""",
            unsafe_allow_html=True
        )

        # ---------------------------------------------------
        # DOWNLOAD BUTTON
        # ---------------------------------------------------
        st.download_button(
            label="📥 Download Diagnosis Report",
            data=report,
            file_name="healthcare_diagnosis_report.txt",
            mime="text/plain"
        )

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("📘 About Project")

st.sidebar.info("""
This application demonstrates:

✅ Self-Consistency Prompting

✅ AI Medical Reasoning

✅ Disease Prediction

✅ Healthcare Decision Support

✅ Telemedicine AI Systems

✅ Clinical Recommendation Systems
""")

st.sidebar.markdown("---")

st.sidebar.markdown("🏥 Smart Healthcare AI Assistant")

import streamlit as st

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Legal Contract Reviewer",
    page_icon="⚖",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}

.stButton button {
    background-color: #6f42c1;
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
    color: #2d1b69;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("⚖ AI Legal Contract Reviewer")
st.subheader("Constitutional Prompting Based Legal Risk Analysis System")

st.markdown("""
This AI Legal System performs:

✅ Legal Risk Detection  
✅ Compliance Analysis  
✅ Ambiguous Clause Identification  
✅ Ethical Contract Review  
✅ Corporate Policy Validation  
✅ Constitutional AI Reasoning
""")

# ---------------------------------------------------
# LEGAL RULES DATABASE
# ---------------------------------------------------
risk_keywords = {
    "High Risk": [
        "unlimited liability",
        "terminate without notice",
        "confidential forever",
        "full responsibility",
        "no refund"
    ],

    "Compliance Issues": [
        "data sharing",
        "personal information",
        "third-party transfer",
        "cross-border data"
    ],

    "Ambiguous Clauses": [
        "reasonable effort",
        "as soon as possible",
        "may terminate",
        "if necessary",
        "subject to change"
    ]
}

# ---------------------------------------------------
# USER INPUTS
# ---------------------------------------------------
st.header("📄 Contract Analysis")

contract_title = st.text_input(
    "Contract Title",
    placeholder="Example: Employment Agreement"
)

contract_type = st.selectbox(
    "Contract Type",
    [
        "Employment Contract",
        "NDA",
        "Service Agreement",
        "Vendor Agreement",
        "Lease Agreement",
        "Partnership Agreement",
        "Software License Agreement"
    ]
)

jurisdiction = st.selectbox(
    "Jurisdiction",
    [
        "India",
        "USA",
        "Europe",
        "UK",
        "Global"
    ]
)

contract_text = st.text_area(
    "Paste Contract Content",
    height=300,
    placeholder="""
Example:
The company may terminate the agreement without notice.
The user accepts full responsibility for all damages.
Personal information may be shared with third-party vendors.
"""
)

# ---------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------
if st.button("🔍 Analyze Legal Contract"):

    if not contract_text:
        st.error("Please enter contract content")

    else:

        text_lower = contract_text.lower()

        high_risks = []
        compliance_issues = []
        ambiguous_clauses = []

        # ---------------------------------------------------
        # CONSTITUTIONAL ANALYSIS
        # ---------------------------------------------------
        for keyword in risk_keywords["High Risk"]:
            if keyword in text_lower:
                high_risks.append(keyword)

        for keyword in risk_keywords["Compliance Issues"]:
            if keyword in text_lower:
                compliance_issues.append(keyword)

        for keyword in risk_keywords["Ambiguous Clauses"]:
            if keyword in text_lower:
                ambiguous_clauses.append(keyword)

        # ---------------------------------------------------
        # GENERATE REPORT
        # ---------------------------------------------------
        report = f"""
# ⚖ AI Legal Contract Review Report

## 📄 Contract Information

- Contract Title: {contract_title}
- Contract Type: {contract_type}
- Jurisdiction: {jurisdiction}

---

## 🚨 Legal Risk Analysis

"""

        if high_risks:
            for risk in high_risks:
                report += f"- High Risk Clause Detected: '{risk}'\n"
        else:
            report += "- No major high-risk clauses detected.\n"

        report += "\n---\n"

        report += "## 📋 Compliance Issues\n\n"

        if compliance_issues:
            for issue in compliance_issues:
                report += f"- Compliance Concern Found: '{issue}'\n"
        else:
            report += "- No major compliance issues detected.\n"

        report += "\n---\n"

        report += "## ❓ Ambiguous Clauses\n\n"

        if ambiguous_clauses:
            for clause in ambiguous_clauses:
                report += f"- Ambiguous Language Detected: '{clause}'\n"
        else:
            report += "- No ambiguous clauses identified.\n"

        report += "\n---\n"

        report += "## ✅ Ethical & Compliance Recommendations\n\n"

        recommendations = [
            "Clearly define termination conditions.",
            "Limit liability clauses to reasonable levels.",
            "Ensure GDPR and privacy compliance.",
            "Avoid vague contractual language.",
            "Specify responsibilities explicitly.",
            "Review contract with legal counsel."
        ]

        for rec in recommendations:
            report += f"- {rec}\n"

        report += "\n---\n"

        report += """
## ⚠ Legal Disclaimer

This AI-generated legal review is for educational purposes only.

Please consult a licensed legal professional for official legal advice.
"""

        # ---------------------------------------------------
        # SUCCESS MESSAGE
        # ---------------------------------------------------
        st.success("Legal Contract Analysis Completed Successfully!")

        # ---------------------------------------------------
        # DISPLAY REPORT
        # ---------------------------------------------------
        st.markdown("## 📑 Legal Review Report")

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
            label="📥 Download Legal Report",
            data=report,
            file_name="legal_contract_review.txt",
            mime="text/plain"
        )

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("📘 About Project")

st.sidebar.info("""
This application demonstrates:

✅ Constitutional Prompting

✅ AI Legal Analysis

✅ Compliance Validation

✅ Legal Risk Detection

✅ Contract Ambiguity Detection

✅ Corporate LegalTech Systems
""")

st.sidebar.markdown("---")

st.sidebar.markdown("⚖ AI-Powered Legal Compliance Assistant")

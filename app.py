import streamlit as st
from openai import OpenAI

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------
st.set_page_config(
    page_title="Cybersecurity Incident Analyzer",
    page_icon="🛡",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("🛡 GenAI Cybersecurity Incident Analyzer")
st.subheader("AI-Powered Threat Detection & Security Reasoning")

# -----------------------------------
# API KEY
# -----------------------------------
api_key = st.text_input(
    "Enter OpenAI API Key",
    type="password"
)

# -----------------------------------
# INCIDENT INPUTS
# -----------------------------------
st.header("🚨 Incident Details")

incident_type = st.selectbox(
    "Select Incident Type",
    [
        "Phishing Attack",
        "Ransomware",
        "DDoS Attack",
        "SQL Injection",
        "Malware Infection",
        "Privilege Escalation",
        "Insider Threat",
        "Data Breach",
        "Zero-Day Exploit",
        "Credential Theft"
    ]
)

severity = st.selectbox(
    "Initial Severity Level",
    [
        "Low",
        "Medium",
        "High",
        "Critical"
    ]
)

affected_system = st.text_input(
    "Affected Systems",
    placeholder="Example: Web Server, Database, Employee Endpoints"
)

incident_description = st.text_area(
    "Describe the Cybersecurity Incident",
    height=200,
    placeholder="""
Example:
Multiple employees received phishing emails containing malicious links.
Several systems showed unauthorized login attempts and unusual outbound traffic.
"""
)

# -----------------------------------
# GENERATE BUTTON
# -----------------------------------
if st.button("🔍 Analyze Incident"):

    if not api_key:
        st.error("Please enter OpenAI API Key")

    elif not incident_description:
        st.error("Please enter incident description")

    else:

        client = OpenAI(api_key=api_key)

        # -----------------------------------
        # CHAIN-OF-THOUGHT PROMPT
        # -----------------------------------
        prompt = f"""
You are an Enterprise AI Cybersecurity Analyst.

Analyze the cybersecurity incident step-by-step using Chain-of-Thought reasoning.

Incident Information:
Incident Type: {incident_type}
Severity: {severity}
Affected Systems: {affected_system}

Incident Description:
{incident_description}

Perform the following tasks:

1. Identify the likely attack type.
2. Analyze attacker behavior patterns.
3. Determine attack severity and business impact.
4. Identify potentially compromised systems.
5. Explain indicators of compromise (IoCs).
6. Recommend immediate containment actions.
7. Suggest recovery procedures.
8. Recommend long-term prevention strategies.
9. Generate SOC Incident Summary Report.

Instructions:
- Use professional cybersecurity terminology.
- Provide logical reasoning step-by-step.
- Use enterprise SOC analysis standards.
- Keep recommendations practical and actionable.
"""

        # -----------------------------------
        # API CALL
        # -----------------------------------
        with st.spinner("Analyzing Cybersecurity Threat..."):

            try:

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.3
                )

                result = response.choices[0].message.content

                # -----------------------------------
                # OUTPUT
                # -----------------------------------
                st.success("Incident Analysis Completed")

                st.markdown("## 📊 Threat Intelligence Report")

                st.write(result)

                # -----------------------------------
                # DOWNLOAD REPORT
                # -----------------------------------
                st.download_button(
                    label="📥 Download Incident Report",
                    data=result,
                    file_name="cybersecurity_incident_report.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {e}")

# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.title("📘 About")

st.sidebar.info("""
This application demonstrates:

✅ Chain-of-Thought Prompting

✅ AI Cybersecurity Reasoning

✅ Threat Analysis

✅ SOC Incident Reporting

✅ Enterprise Security Automation

✅ Incident Mitigation Recommendations
""")

st.sidebar.markdown("---")

st.sidebar.markdown("🛡 AI-Powered Enterprise Security System")

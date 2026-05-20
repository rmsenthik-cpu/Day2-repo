import streamlit as st
from openai import OpenAI

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Financial Risk Advisor",
    page_icon="💰",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f4f7fc;
}

.stButton button {
    background-color: #0d6efd;
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
    color: #0b1f3a;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("💰 AI Financial Risk Advisor")
st.subheader("Tree-of-Thought AI Investment Analysis System")

st.markdown("""
This AI application performs:

✅ Investment Strategy Comparison  
✅ ROI Analysis  
✅ Risk Assessment  
✅ Portfolio Diversification  
✅ Financial Advisory Recommendations  
✅ Tree-of-Thought Reasoning
""")

# ---------------------------------------------------
# API KEY
# ---------------------------------------------------
api_key = st.text_input(
    "Enter OpenAI API Key",
    type="password"
)

# ---------------------------------------------------
# AVAILABLE INVESTMENT OPTIONS
# ---------------------------------------------------
investment_options = [
    "Stocks",
    "Mutual Funds",
    "Cryptocurrency",
    "Real Estate",
    "Gold",
    "Fixed Deposits",
    "Government Bonds",
    "Index Funds",
    "Retirement Plans",
    "Startup Investments"
]

# ---------------------------------------------------
# USER INPUTS
# ---------------------------------------------------
st.header("📊 Investment Details")

selected_investments = st.multiselect(
    "Select Preferred Investment Options",
    investment_options
)

investment_amount = st.number_input(
    "Investment Amount",
    min_value=1000,
    step=1000
)

risk_tolerance = st.selectbox(
    "Risk Tolerance",
    [
        "Low",
        "Medium",
        "High"
    ]
)

investment_duration = st.selectbox(
    "Investment Duration",
    [
        "Short-Term",
        "Medium-Term",
        "Long-Term"
    ]
)

financial_goal = st.text_input(
    "Financial Goal",
    placeholder="Example: Wealth Creation, Retirement Planning"
)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=0,
    step=1000
)

existing_savings = st.number_input(
    "Existing Savings",
    min_value=0,
    step=1000
)

market_condition = st.selectbox(
    "Current Market Condition",
    [
        "Bull Market",
        "Bear Market",
        "Stable Market",
        "Volatile Market"
    ]
)

# ---------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------
if st.button("🚀 Generate Financial Advisory Report"):

    if not api_key:
        st.error("Please enter OpenAI API Key")

    elif not selected_investments:
        st.error("Please select at least one investment option")

    else:

        client = OpenAI(api_key=api_key)

        # ---------------------------------------------------
        # TREE-OF-THOUGHT PROMPT
        # ---------------------------------------------------
        prompt = f"""
You are an AI Financial Risk Advisor.

Use Tree-of-Thought reasoning to evaluate multiple investment strategies.

Investor Information
------------------------------------------------
Preferred Investments: {selected_investments}

Investment Amount: ₹{investment_amount}

Risk Tolerance: {risk_tolerance}

Investment Duration: {investment_duration}

Financial Goal: {financial_goal}

Monthly Income: ₹{monthly_income}

Existing Savings: ₹{existing_savings}

Market Condition: {market_condition}
------------------------------------------------

Perform the following tasks:

1. Analyze multiple investment paths.
2. Compare conservative, balanced, and aggressive strategies.
3. Evaluate ROI potential for each strategy.
4. Analyze financial risks and uncertainties.
5. Compare short-term and long-term outcomes.
6. Recommend the most optimal investment strategy.
7. Suggest portfolio diversification methods.
8. Generate professional financial advisory report.

Instructions:
- Use Tree-of-Thought reasoning.
- Explore multiple investment possibilities.
- Compare different reasoning paths before final recommendations.
- Use professional financial terminology.
- Clearly structure the report with headings.
- Keep recommendations practical and realistic.
"""

        # ---------------------------------------------------
        # OPENAI API CALL
        # ---------------------------------------------------
        with st.spinner("Analyzing Investment Strategies..."):

            try:

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.4
                )

                result = response.choices[0].message.content

                # ---------------------------------------------------
                # SUCCESS MESSAGE
                # ---------------------------------------------------
                st.success("Financial Advisory Report Generated Successfully!")

                # ---------------------------------------------------
                # DISPLAY OUTPUT
                # ---------------------------------------------------
                st.markdown("## 📈 Financial Analysis Report")

                st.markdown(
                    f"""
<div class="result-box">
{result.replace('\n', '<br>')}
</div>
""",
                    unsafe_allow_html=True
                )

                # ---------------------------------------------------
                # DOWNLOAD BUTTON
                # ---------------------------------------------------
                st.download_button(
                    label="📥 Download Financial Report",
                    data=result,
                    file_name="financial_advisory_report.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {e}")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("📘 About Project")

st.sidebar.info("""
This application demonstrates:

✅ Tree-of-Thought Prompting

✅ AI Financial Advisory

✅ Investment Risk Analysis

✅ ROI Comparison

✅ Portfolio Optimization

✅ FinTech AI Systems

✅ Streamlit Deployment
""")

st.sidebar.markdown("---")

st.sidebar.markdown("💰 AI-Powered Financial Advisory System")

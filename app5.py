import streamlit as st
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_groq import ChatGroq

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="Titanic Dataset AI Analyzer",
    page_icon="🚢",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🚢 Titanic Dataset AI Analyzer")
st.subheader("AI-Powered Data Analysis using LangChain + Groq")

st.markdown("""
This application allows users to:

✅ Upload Titanic Dataset CSV  
✅ Ask Natural Language Questions  
✅ Perform AI-Based Data Analysis  
✅ Generate Dataset Insights  
✅ Use LLM + Pandas Agent
""")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("⚙ Configuration")

groq_api_key = st.sidebar.text_input(
    "Enter Groq API Key",
    type="password"
)

st.sidebar.markdown("""
Get FREE API Key from:

https://console.groq.com/keys
""")

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload Titanic CSV File",
    type=["csv"]
)

# ---------------------------------------------------
# MAIN APPLICATION
# ---------------------------------------------------
if uploaded_file is not None:

    # LOAD DATASET
    df = pd.read_csv(uploaded_file)

    # DISPLAY DATASET
    st.markdown("## 📊 Dataset Preview")
    st.dataframe(df.head())

    st.markdown("## 📈 Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    # ---------------------------------------------------
    # USER QUESTION
    # ---------------------------------------------------
    st.markdown("## 🤖 Ask Questions About Dataset")

    user_query = st.text_input(
        "Enter Your Question",
        placeholder="Example: Who survived in Titanic dataset?"
    )

    # ---------------------------------------------------
    # ANALYZE BUTTON
    # ---------------------------------------------------
    if st.button("🚀 Analyze Dataset"):

        if not groq_api_key:
            st.error("Please enter Groq API Key")

        elif not user_query:
            st.error("Please enter your question")

        else:

            try:

                # ---------------------------------------------------
                # LOAD LLM
                # ---------------------------------------------------
                llm = ChatGroq(
                    model_name="llama-3.1-8b-instant",
                    api_key=groq_api_key
                )

                # ---------------------------------------------------
                # CREATE AGENT
                # ---------------------------------------------------
                agent = create_pandas_dataframe_agent(
                    llm,
                    df,
                    verbose=True,
                    allow_dangerous_code=True
                )

                # ---------------------------------------------------
                # RUN QUERY
                # ---------------------------------------------------
                with st.spinner("Analyzing Dataset..."):

                    response = agent.run(user_query)

                # ---------------------------------------------------
                # DISPLAY OUTPUT
                # ---------------------------------------------------
                st.success("Analysis Completed Successfully!")

                st.markdown("## 🧠 AI Analysis Result")

                st.markdown(f"""
<div style="
background-color:white;
padding:20px;
border-radius:10px;
box-shadow:0px 0px 10px rgba(0,0,0,0.1);
">
{response}
</div>
""", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {e}")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

st.markdown("""
### 📘 Technologies Used

- Python
- Streamlit
- LangChain
- Groq LLM
- Pandas AI Agent
""")

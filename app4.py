import streamlit as st

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Research Paper Generator",
    page_icon="📚",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f4f7fb;
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
st.title("📚 AI Research Paper Generator")
st.subheader("Skeleton-of-Thought Prompting Based Academic Writing System")

st.markdown("""
This AI Research System performs:

✅ Research Title Generation  
✅ Abstract Writing  
✅ Literature Review Creation  
✅ Methodology Generation  
✅ Results & Analysis  
✅ Conclusion Writing  
✅ Structured Academic Formatting
""")

# ---------------------------------------------------
# USER INPUTS
# ---------------------------------------------------
st.header("📝 Research Paper Details")

research_topic = st.text_input(
    "Research Topic",
    placeholder="Example: Artificial Intelligence in Healthcare"
)

research_domain = st.selectbox(
    "Research Domain",
    [
        "Artificial Intelligence",
        "Cybersecurity",
        "Healthcare",
        "Finance",
        "Education",
        "Data Science",
        "Cloud Computing",
        "IoT",
        "Blockchain",
        "Software Engineering"
    ]
)

research_type = st.selectbox(
    "Research Type",
    [
        "Survey Paper",
        "Experimental Research",
        "Comparative Study",
        "Case Study",
        "Review Paper"
    ]
)

author_name = st.text_input(
    "Author Name",
    placeholder="Enter Author Name"
)

keywords = st.text_area(
    "Research Keywords",
    placeholder="Example: AI, Machine Learning, Diagnosis, Healthcare"
)

problem_statement = st.text_area(
    "Problem Statement",
    placeholder="Describe the research problem"
)

# ---------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------
if st.button("🚀 Generate Research Paper"):

    if not research_topic:
        st.error("Please enter research topic")

    else:

        # ---------------------------------------------------
        # SKELETON-OF-THOUGHT OUTLINE
        # ---------------------------------------------------
        title = f"AI-Based Analysis of {research_topic}"

        abstract = f"""
This research paper explores {research_topic} within the domain of {research_domain}.
The study focuses on addressing challenges related to the problem statement:
{problem_statement}.

The research investigates current methodologies, technological advancements,
and practical implementations. The study aims to provide structured insights,
performance evaluation, and future research directions.
"""

        literature_review = f"""
Existing studies in {research_domain} demonstrate significant advancements
in intelligent systems and automation technologies.

Researchers have explored multiple approaches related to {research_topic},
including machine learning models, predictive systems, and optimization methods.
However, several limitations remain regarding scalability, accuracy, and
real-world implementation challenges.
"""

        methodology = f"""
The proposed methodology uses a structured research approach involving:

1. Data Collection
2. System Design
3. Experimental Analysis
4. Comparative Evaluation
5. Result Interpretation

The study applies analytical techniques and domain-specific frameworks
to evaluate the effectiveness of the proposed solution.
"""

        results = f"""
The experimental results demonstrate improved performance in terms of:

- Accuracy
- Efficiency
- Scalability
- Reliability

The proposed system achieved promising outcomes compared to traditional approaches.
The findings indicate that {research_topic} can significantly improve
operational efficiency and decision-making processes.
"""

        conclusion = f"""
This research successfully analyzed the impact of {research_topic}
in the field of {research_domain}.

The study highlights important advancements, challenges, and opportunities
for future research. The proposed approach demonstrates practical applicability
and contributes toward academic and industrial innovation.
"""

        # ---------------------------------------------------
        # FULL RESEARCH PAPER
        # ---------------------------------------------------
        paper = f"""
# 📚 Research Paper

## Title
{title}

---

## Author
{author_name}

---

## Keywords
{keywords}

---

## Abstract
{abstract}

---

## Introduction
The field of {research_domain} continues to evolve rapidly due to technological
advancements and intelligent automation systems.

This paper focuses on {research_topic} and investigates its significance,
applications, challenges, and future opportunities.

---

## Literature Review
{literature_review}

---

## Methodology
{methodology}

---

## Results and Discussion
{results}

---

## Conclusion
{conclusion}

---

## Future Work
Future research can focus on improving system scalability,
AI model optimization, and real-time deployment strategies.

---

## References

1. Research Articles on {research_topic}
2. AI and Technology Journals
3. International Conference Publications
"""

        # ---------------------------------------------------
        # SUCCESS MESSAGE
        # ---------------------------------------------------
        st.success("Research Paper Generated Successfully!")

        # ---------------------------------------------------
        # DISPLAY OUTPUT
        # ---------------------------------------------------
        st.markdown("## 📄 Generated Research Paper")

        st.markdown(
            f"""
<div class="result-box">
{paper.replace('\n', '<br>')}
</div>
""",
            unsafe_allow_html=True
        )

        # ---------------------------------------------------
        # DOWNLOAD BUTTON
        # ---------------------------------------------------
        st.download_button(
            label="📥 Download Research Paper",
            data=paper,
            file_name="research_paper.txt",
            mime="text/plain"
        )

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("📘 About Project")

st.sidebar.info("""
This application demonstrates:

✅ Skeleton-of-Thought Prompting

✅ AI Research Automation

✅ Academic Writing Assistance

✅ Technical Document Generation

✅ Structured Research Formatting

✅ AI Academic Systems
""")

st.sidebar.markdown("---")

st.sidebar.markdown("📚 AI-Powered Research Paper Generator")

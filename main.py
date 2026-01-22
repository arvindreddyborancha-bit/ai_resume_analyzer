import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer & Skill Gap Recommendation System")

st.write(
    "This application analyzes a student's resume and identifies missing skills "
    "based on the selected job role."
)

resume_text = st.text_area(
    "Paste Resume Text Here",
    height=200
)

role = st.selectbox(
    "Select Target Job Role",
    ["Java Developer", "Data Analyst", "Web Developer"]
)

if st.button("Analyze Resume"):
    if resume_text.strip() == "":
        st.warning("Please paste resume text")
    else:
        st.subheader("Generated AI Analysis Prompt")

        prompt = f"""
You are an AI Resume Analyzer.

Resume Text:
{resume_text}

Target Role:
{role}

Tasks:
1. Extract technical skills from the resume
2. List required skills for the target role
3. Identify missing skills (skill gap)
4. Recommend skills to learn

Provide output in bullet points.
"""
        st.code(prompt)


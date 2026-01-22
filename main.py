import streamlit as st

if st.button("Analyze Resume"):
    if resume_text.strip() == "":
        st.warning("Please paste resume text")
    else:
        # 1. Generate AI prompt (optional, for showing AI workflow)
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

        # 2. --- Skill Gap Calculation ---
        # Predefined required skills for each role
        role_skills = {
            "Java Developer": ["Java", "OOP", "Spring", "SQL", "Git"],
            "Data Analyst": ["Python", "SQL", "Excel", "Power BI", "Statistics"],
            "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Git"]
        }

        # Convert resume text to lowercase for matching
        resume_lower = resume_text.lower()

        # Find skills present in resume
        found_skills = []
        for skill in role_skills[role]:
            if skill.lower() in resume_lower:
                found_skills.append(skill)

        # Find missing skills
        missing_skills = [skill for skill in role_skills[role] if skill not in found_skills]

        # Display results
        st.subheader("Skill Gap Analysis")
        st.write("Skills Found:", found_skills if found_skills else "None")
        st.write("Missing Skills:", missing_skills if missing_skills else "None")

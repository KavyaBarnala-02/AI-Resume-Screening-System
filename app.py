import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import extract_text_from_pdf, extract_skills

# Page Configuration
st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.title("📄 AI Resume Screening System")
st.markdown("---")

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Step 1: Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])
    
with col2:
    st.subheader("Step 2: Job Description")
    job_description = st.text_area("Paste Job Description (JD) here...", height=200)

if st.button("Analyze Resume") and uploaded_file and job_description:
    with st.spinner("Analyzing..."):
        # 1. Extract Text
        resume_text = extract_text_from_pdf(uploaded_file)
        
        # 2. Extract Skills
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)
        
        # 3. Compare Using TF-IDF & Cosine Similarity
        documents = [resume_text, job_description]
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(documents)
        similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        match_percentage = round(similarity_score * 100, 2)
        
        # 4. Identify Matched and Missing Skills
        matched_skills = [skill for skill in jd_skills if skill in resume_skills]
        missing_skills = [skill for skill in jd_skills if skill not in resume_skills]

        # --- Display Results ---
        st.markdown("---")
        st.header(f"Results: {match_percentage}% Match")
        
        # Visualization: Gauge Chart
        fig = px.pie(
            values=[match_percentage, 100 - match_percentage], 
            names=["Match", "Gap"],
            hole=0.7,
            color_discrete_sequence=["#2ecc71", "#e74c3c"],
            title="Resume Compatibility Score"
        )
        st.plotly_chart(fig, use_container_width=True)

        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.success("✅ Matched Skills")
            if matched_skills:
                for skill in matched_skills:
                    st.write(f"- {skill}")
            else:
                st.write("No matching skills found.")
                
        with res_col2:
            st.error("❌ Missing Skills")
            if missing_skills:
                for skill in missing_skills:
                    st.write(f"- {skill}")
            else:
                st.write("Great! No major skills missing.")

        # Text Summary
        with st.expander("View Extracted Resume Text"):
            st.write(resume_text)

elif not uploaded_file or not job_description:
    st.info("Please upload a resume and paste a job description to start the analysis.")
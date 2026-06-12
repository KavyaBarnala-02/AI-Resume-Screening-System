import PyPDF2
import spacy
from spacy.matcher import PhraseMatcher

# Load NLP model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Comprehensive Skill List for extraction
TECHNICAL_SKILLS = [
    "Python", "Java", "C++", "JavaScript", "SQL", "NoSQL", "React", "Angular", 
    "Node.js", "Docker", "Kubernetes", "AWS", "Azure", "GCP", "Machine Learning", 
    "Data Science", "Deep Learning", "NLP", "Tableau", "Power BI", "Excel", 
    "Pandas", "NumPy", "Scikit-Learn", "TensorFlow", "PyTorch", "Flask", "Django",
    "Streamlit", "HTML", "CSS", "Git", "Jenkins", "Linux", "R", "Spark", "Hadoop"
]

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_skills(text):
    doc = nlp(text.lower())
    matched_skills = []
    
    # Simple phrase matching for skills
    for skill in TECHNICAL_SKILLS:
        if skill.lower() in text.lower():
            matched_skills.append(skill)
            
    return list(set(matched_skills))
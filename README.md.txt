# 🤖 AI Resume Screening System

An AI-powered Resume Screening System that automates the resume evaluation process by comparing candidate resumes with job descriptions using **Machine Learning** and **Natural Language Processing (NLP)**.

This project helps recruiters quickly identify suitable candidates by calculating a resume-job compatibility score, extracting technical skills, identifying skill gaps, and maintaining candidate records.

---

## 📌 Project Overview

Recruiters often spend significant time manually reviewing resumes. This project simplifies that process by using AI techniques to analyze resumes and compare them with job descriptions.

The system extracts text from PDF resumes, identifies technical skills, calculates a matching percentage using TF-IDF and Cosine Similarity, and provides insights into matched and missing skills.

---

## ✨ Features

- 📄 Upload Resume (PDF)
- 📝 Enter Job Description
- 🔍 Automatic Resume Text Extraction
- 🧠 Skill Extraction using NLP
- 📊 Resume Match Percentage
- ✅ Matched Skills Detection
- ❌ Missing Skills Identification
- 🏆 Candidate Leaderboard
- 📁 Candidate History
- 📤 Export Results to CSV
- 📑 PDF Report Generation
- 💡 Resume Improvement Suggestions
- 📈 Interactive Data Visualization

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries & Frameworks
- Streamlit
- Scikit-Learn
- spaCy
- Pandas
- Plotly
- PyPDF2

### Machine Learning Concepts
- TF-IDF (Term Frequency–Inverse Document Frequency)
- Cosine Similarity

### NLP
- Skill Extraction using spaCy

### Data Storage
- CSV File

---

## ⚙️ How It Works

1. Upload a resume in PDF format.
2. Enter the job description.
3. Extract text from the uploaded resume.
4. Identify technical skills from both the resume and the job description.
5. Convert text into numerical vectors using TF-IDF.
6. Compare both vectors using Cosine Similarity.
7. Calculate the resume compatibility score.
8. Display:
   - Match Percentage
   - Matched Skills
   - Missing Skills
9. Save candidate information.
10. Generate reports and export results.

---

## 📂 Project Structure

```
AI Resume Screening System/
│
├── app.py
├── utils.py
├── requirements.txt
├── candidates.csv
├── Project_Report.pdf
├── Project_Presentation.pptx
└── Screenshots/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Screening-System.git
```

Move into the project directory

```bash
cd AI-Resume-Screening-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📊 Sample Output

The application provides:

- Resume Match Percentage
- Matched Skills
- Missing Skills
- Candidate Ranking
- Candidate History
- CSV Export
- PDF Report

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Python Programming
- Machine Learning
- Natural Language Processing (NLP)
- Streamlit Web Application Development
- Data Analysis
- Resume Parsing
- TF-IDF Vectorization
- Cosine Similarity
- Project Documentation
- GitHub Version Control

---

## 🔮 Future Improvements

- Integration with online job portals
- Batch resume screening
- Cloud database integration
- AI-powered interview recommendations
- Advanced NLP for contextual skill extraction
- Admin dashboard with analytics

---

## 👩‍💻 Author

**Barnala Venkata Satya Kavya Sree**

BCA (Data Science)

Centurion University of Technology and Management

---

## 📜 License

This project is developed for educational and academic purposes.
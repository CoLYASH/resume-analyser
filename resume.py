import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    import pdfplumber
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    from docx import Document
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def clean_text(text):
    return re.sub(r'\s+', ' ', text)

def extract_skills(text):
    skills_list = ["Python", "Java", "SQL", "Machine Learning", "Deep Learning", "Streamlit", "NLP", "Data Analysis"]
    text = text.lower()
    found = [skill for skill in skills_list if skill.lower() in text]
    return list(set(found))

def extract_education(text):
    education_keywords = ["Bachelor", "Master", "B.Tech", "M.Tech", "BSc", "MSc", "PhD"]
    lines = text.split('\n')
    edu_lines = [line for line in lines if any(keyword in line for keyword in education_keywords)]
    return edu_lines

def extract_experience(text):
    exp_keywords = ["Intern", "Experience", "Worked", "Project", "Developed"]
    lines = text.split('\n')
    exp_lines = [line for line in lines if any(keyword in line for keyword in exp_keywords)]
    return exp_lines

import streamlit as st
from resume import *

st.title("📄 Resume Analyser with NLP")
st.markdown("Upload your resume and get a smart analysis!")

uploaded_file = st.file_uploader("Choose a Resume File", type=['pdf', 'docx'])

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1]

    if file_type == 'pdf':
        text = extract_text_from_pdf(uploaded_file)
    elif file_type == 'docx':
        text = extract_text_from_docx(uploaded_file)
    else:
        st.error("Unsupported file type")
        st.stop()

    text = clean_text(text)
    doc = nlp(text)

    st.subheader("🔍 Extracted Information:")

    st.markdown("**Skills:**")
    st.write(", ".join(extract_skills(text)))

    st.markdown("**Education:**")
    for edu in extract_education(text):
        st.write(f"- {edu}")

    st.markdown("**Experience / Projects:**")
    for exp in extract_experience(text):
        st.write(f"- {exp}")

    st.success("Resume analysis complete!")

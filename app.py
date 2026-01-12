import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Configure AI
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except:
    st.warning("API Key not found. Please set GOOGLE_API_KEY.")

def extract_text_from_pdf(file):
    try:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def extract_text_from_docx(file):
    try:
        doc = Document(file)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception as e:
        return f"Error reading DOCX: {e}"

def get_gemini_response(content_parts):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([SYSTEM_PROMPT] + content_parts)
    return response.text

# --- UI Layout ---
st.set_page_config(page_title="Prompt Refiner", layout="wide")

st.title("Multi-Modal Prompt Refinement System")
st.markdown("Upload sketches, docs, or text to generate a structured prompt.")

# Input Section
col1, col2 = st.columns(2)

with col1:
    st.subheader("Inputs")
    input_text = st.text_area("Enter textual description:", height=150)
    
    uploaded_files = st.file_uploader("Upload Documents (PDF, DOCX) or Images (PNG, JPG)", 
                                      type=['pdf', 'docx', 'png', 'jpg', 'jpeg'], 
                                      accept_multiple_files=True)

    process_btn = st.button("Refine Prompt")

# Processing Section
if process_btn:
    content_parts = []
    
    # 1. Add Text Input
    if input_text:
        content_parts.append(f"User Text Input: {input_text}")
    
    # 2. Process Files
    if uploaded_files:
        for file in uploaded_files:
            file_type = file.type
            
            if "pdf" in file_type:
                text = extract_text_from_pdf(file)
                content_parts.append(f"Content from {file.name}: {text}")
            
            elif "word" in file_type or "document" in file_type:
                text = extract_text_from_docx(file)
                content_parts.append(f"Content from {file.name}: {text}")
                
            elif "image" in file_type:
                # Gemini can process images directly
                img = Image.open(file)
                content_parts.append(img)
                content_parts.append(f"Image context: {file.name}")

    if not content_parts:
        st.error("Please provide at least one input.")
    else:
        with col2:
            st.subheader("Refined Output")
            with st.spinner("Analyzing and Refining..."):
                try:
                    response = get_gemini_response(content_parts)
                    st.markdown(response)
                    st.success("Refinement Complete")
                except Exception as e:
                    st.error(f"Error processing request: {str(e)}")

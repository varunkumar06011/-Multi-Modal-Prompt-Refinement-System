# Multi-Modal Prompt Refinement System

### 📌 Project Overview
This tool solves the "Garbage In, Garbage Out" problem in AI. It allows users to upload rough inputs (sketches, PDF specs, emails) and uses Google Gemini 1.5 Flash to convert them into professional, structured technical prompts.

### 🚀 Features
* **Multi-Modal Input:** Accepts Images (wireframes), PDFs (specs), and Text simultaneously.
* **Instant Refinement:** Generates a "5-Point Structured Prompt" for developers.
* **Streamlit Dashboard:** Simple, clean UI for non-technical users.

### 🛠️ Tech Stack
* **Python 3.11+**
* **Streamlit** (Frontend)
* **Google Gemini 1.5 Flash** (LLM Engine)

### 📦 Installation
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your API key to `.env`
4. Run: `streamlit run app.py`

### 📄 Documentation
For a full deep-dive into the design choices, please see the [Design Rationale](design_rationale.md) file.

# Design Rationale & Thought Process

## 1. Problem Approach
The objective was to create a system capable of standardizing vague user inputs into structured technical prompts. The core challenge identified was **ambiguity reduction**—users often provide incomplete specifications.

## 2. Architectural Choices
* **Frontend:** Streamlit was chosen for its native support of multi-modal widgets (file uploaders for both images and documents side-by-side), allowing for rapid prototyping as required by the deadline.
* **Processing:** * *Text Extraction:* PyPDF2 and python-docx are used for raw text extraction to ensure the LLM receives the full context of specification documents.
    * *Vision:* The system utilizes an LLM with native vision capabilities (Gemini 1.5 Flash) to interpret "product sketches" and "reference designs" directly. This avoids the fragility of traditional OCR on hand-drawn diagrams.

## 3. Template Design Rationale
The "Refined Prompt" template focuses on 5 key areas:
1.  **Core Intent:** Filters out noise to find the primary goal.
2.  **Functional Requirements:** Separates actionable features from general descriptions.
3.  **Technical Constraints:** Isolates critical limitations (platforms, tools) that change the implementation.
4.  **Deliverables:** Clarifies the "Definition of Done."
5.  **Open Questions:** This is the most critical section for "Refinement." It shifts the burden of ambiguity back to the user by explicitly asking for missing details, rather than the AI guessing incorrectly.

## 4. AI vs. Deterministic Logic
* *AI Role:* Semantic understanding, pattern recognition in images, and summarizing diverse inputs.
* *System Role:* Enforcing the output structure (via System Prompting) and handling file I/O safety.

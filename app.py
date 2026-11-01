import streamlit as st
import google.generativeai as genai

# For your free desktop demo phase, paste your free key between the quotes below
genai.configure(api_key="PASTE_YOUR_FREE_API_KEY_HERE")

st.set_page_config(page_title="Appraisal System", page_icon="📋")
st.title("📋 Corporate Performance Appraisal Portal")

# Dropdowns for your 135 employees and 7 appraisers
employee_list = [f"Employee {i}" for i in range(1, 136)]
selected_employee = st.selectbox("Select Employee to Appraise:", options=employee_list)

appraiser_list = [f"Appraiser {i}" for i in range(1, 8)]
selected_appraiser = st.selectbox("Your Identity (Appraiser Panel):", options=appraiser_list)

# Structured evaluation feedback text box
evaluation_text = st.text_area("Provide Detailed Performance Feedback:", height=150)

if st.button("🚀 Process & Submit Appraisal", use_container_width=True):
    if evaluation_text:
        with st.spinner("AI Engine running analytics... Please wait..."):
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # The exact instructions for the AI
            structured_prompt = f"""
            System Instruction: You are an expert HR analyst. Review the provided peer feedback and generate an objective performance summary report.
            
            Target Employee: {selected_employee}
            Reviewer: {selected_appraiser}
            Feedback: {evaluation_text}
            """
            
            response = model.generate_content(structured_prompt)
            st.success(f"Appraisal successfully logged!")
            st.markdown("### 📊 Generated Summary")
            st.write(response.text)
    else:
        st.warning("Please type in some feedback before submitting.")

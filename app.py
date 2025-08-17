import streamlit as st
import pandas as pd
from src.preprocessing.file_ingest import extract_text_from_pdf, extract_text_from_docx, load_csv, load_excel
from src.genai.genai_module import generate_summary
from src.dashboard.dashboard import render_data_dashboard  # Import your dashboard module
from src.feedback.qa import answer_user_question  # Import your QA module


def prepare_limited_data(df, max_chars=20000, max_columns=5, max_rows=100):
    """
    Limit dataset size for LLM input by:
    - Selecting top columns (up to max_columns)
    - Selecting top rows (up to max_rows)
    - Ensuring converted CSV string does not exceed max_chars
    
    Returns CSV string suitable for LLM input.
    """
    limited_df = df.iloc[:, :max_columns]
    limited_df = limited_df.head(max_rows)
    csv_text = limited_df.to_csv(index=False)

    while len(csv_text) > max_chars and max_rows > 10:
        max_rows = max_rows // 2
        limited_df = limited_df.head(max_rows)
        csv_text = limited_df.to_csv(index=False)

    if len(csv_text) > max_chars:
        csv_text = csv_text[:max_chars]

    return csv_text


def qa_section(context_text):
    st.subheader("Ask Questions About Your Dataset")
    user_question = st.text_input("Type your question:")
    if user_question:
        with st.spinner("Analyzing question..."):
            answer = answer_user_question(context_text, user_question)
        st.markdown(f"**Answer:** {answer}")


def main():
    st.title("Gen AI Data Analyst Assistant")
    
    uploaded_file = st.file_uploader("Upload a financial report or data file", type=["pdf", "docx", "csv", "xlsx"])
    
    if uploaded_file:
        file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
        st.write(file_details)
        
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
            st.subheader("Extracted Text:")
            st.write(text[:1000] + "...")  # Show snippet
            
            summary = generate_summary(text)
            st.subheader("AI-Generated Summary:")
            st.write(summary)
            
            # QA Section with context as limited extracted text
            qa_section(text[:2000])

        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_docx(uploaded_file)
            st.subheader("Extracted Text:")
            st.write(text[:1000] + "...")
            
            summary = generate_summary(text)
            st.subheader("AI-Generated Summary:")
            st.write(summary)

            # QA Section with context as limited extracted text
            qa_section(text[:2000])

        elif uploaded_file.type == "text/csv":
            df = load_csv(uploaded_file)
            st.subheader("CSV Data Preview:")
            st.dataframe(df.head())
            
            limited_csv = prepare_limited_data(df)
            stats_text = df.describe().to_string()
            prompt_text = f"Here is a sample of the data:\n{limited_csv}\n\nSummary statistics:\n{stats_text}\n\nProvide a concise summary of this data."
            
            summary = generate_summary(prompt_text)
            st.subheader("AI-Generated Summary of CSV:")
            st.write(summary)
            
            render_data_dashboard(df)

            # QA Section with context as limited_csv + stats_text
            context_text = f"{limited_csv}\n\n{stats_text}"
            qa_section(context_text)
            
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = load_excel(uploaded_file)
            st.subheader("Excel Data Preview:")
            st.dataframe(df.head())
            
            limited_csv = prepare_limited_data(df)
            stats_text = df.describe().to_string()
            prompt_text = f"Here is a sample of the data:\n{limited_csv}\n\nSummary statistics:\n{stats_text}\n\nProvide a concise summary of this data."
            
            summary = generate_summary(prompt_text)
            st.subheader("AI-Generated Summary of Excel:")
            st.write(summary)
            
            render_data_dashboard(df)

            # QA Section with context as limited_csv + stats_text
            context_text = f"{limited_csv}\n\n{stats_text}"
            qa_section(context_text)

        else:
            st.error("Unsupported file type!")


if __name__ == "__main__":
    main()

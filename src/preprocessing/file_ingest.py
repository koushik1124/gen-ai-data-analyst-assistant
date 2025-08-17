import pdfplumber
import pandas as pd
from docx import Document

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

def load_csv(csv_path):
    return pd.read_csv(csv_path)

def load_excel(excel_path):
    return pd.read_excel(excel_path)

# Example usage:
# text = extract_text_from_pdf('data/sample_report.pdf')
# df = load_csv('data/sales_data.csv')
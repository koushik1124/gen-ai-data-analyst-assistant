Gen AI Data Analyst Assistant
Overview
An interactive web app that empowers users to upload, summarize, visualize, and ask questions about their datasets—leveraging advanced LLMs and automated dashboards.
Perfect for financial reports, CSV/Excel data, and business analytics.

Features
Upload files: Supports CSV, Excel, PDF, and DOCX formats.

AI-powered summary: Generates concise, business-ready summaries using GenAI via OpenRouter.

Automated dashboard: Visualizes descriptive statistics, top categories, and trends for rapid data exploration.

Interactive Q&A: Users can ask questions and clarify insights about their uploaded data—responses powered by LLMs.

Modular design: Clean separation of ingestion, analytics, dashboard, and QA for extensibility.

How to Use
Clone this repo:

bash
git clone https://github.com/yourusername/gen-ai-data-analyst-assistant.git
cd gen-ai-data-analyst-assistant
Install dependencies:

bash
pip install -r requirements.txt
Copy .env.example to .env and add your OpenRouter API key:

text
OPENAI_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxx
Run the app:

bash
streamlit run app.py
Upload a data file and explore summaries, dashboards, and Q&A!

Tech Stack
Python, Pandas

Streamlit

OpenAI/OpenRouter API

Modular: src/preprocessing, src/genai, src/dashboard, src/feedback


import os
from dotenv import load_dotenv
from openai import OpenAI

# --- Load .env ---
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("❌ OPENAI_API_KEY not found in .env file")

# --- Initialize OpenRouter client (not api.openai.com) ---
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def generate_summary(text: str) -> str:
    """
    Generate a concise business summary of a financial report
    using OpenRouter (GPT-4o).
    """
    completion = client.chat.completions.create(
        model="openai/gpt-4o",  # You can also try other models via OpenRouter
        messages=[
            {"role": "system", "content": "You are an expert business analyst who writes clear summaries."},
            {"role": "user", "content": f"Summarize this financial report in clear, concise business language:\n\n{text}"}
        ],
        max_tokens=300,
        temperature=0.5,
    )

    return completion.choices[0].message.content.strip()

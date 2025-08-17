import os
from openai import OpenAI

# Initialize OpenAI client for OpenRouter
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"  # Ensure correct OpenRouter endpoint
)

def answer_user_question(context_text: str, question: str) -> str:
    """Generate an answer for user question based on provided context."""
    prompt = (
        f"You are a data analyst assistant. Based on the following context, answer the question clearly:\n\n"
        f"{context_text}\n\n"
        f"Question: {question}\nAnswer:"
    )
    completion = client.chat.completions.create(
        model="openai/gpt-4o",  # Use an OpenRouter-supported model name
        messages=[
            {"role": "system", "content": "You answer as a clear, data-driven analyst."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.5,
    )
    return completion.choices[0].message.content.strip()

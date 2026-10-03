import json
import os
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No API key found. Please check your .env file.")
client = OpenAI(api_key=api_key)

PERSONAS_FILE = Path(__file__).parent / "adopting_personas.jsonl"


def load_conversations(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def ask_chatgpt(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content


for messages in load_conversations(PERSONAS_FILE):
    persona = messages[0]["content"]
    question = messages[-1]["content"]
    print(f"Persona: {persona}")
    print(f"Question: {question}")
    print(f"Answer: {ask_chatgpt(messages)}")
    print("-" * 80)

import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv()

if not api_key:
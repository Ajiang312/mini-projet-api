import vertexai
from vertexai.preview.generative_models import GenerativeModel
import os
from dotenv import load_dotenv

load_dotenv()

def get_ai_joke():
    vertexai.init(
        project=os.getenv("GCP_PROJECT"),  # ou "PROJECT_ID" selon ton .env
        location=os.getenv("GCP_REGION")
    )

    model = GenerativeModel(model_name="gemini-1.5-flash")
    chat = model.start_chat()
    response = chat.send_message("Raconte-moi une blague drôle en français.")
    return response.text

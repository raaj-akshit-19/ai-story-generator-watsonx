# story_generator.py (Secure version)
import os
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

# 🔐 Load credentials from environment variables
api_key = os.environ.get("WATSONX_API_KEY")
project_id = os.environ.get("WATSONX_PROJECT_ID")

if not api_key or not project_id:
    raise ValueError("❌ Missing environment variables: WATSONX_API_KEY and/or WATSONX_PROJECT_ID")

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": api_key
}

# 🧠 Choose the model
model_id = "meta-llama/llama-3-3-70b-instruct"

# ⚙️ Generation parameters
parameters = {
    GenParams.DECODING_METHOD: "sample",
    GenParams.MIN_NEW_TOKENS: 500,
    GenParams.MAX_NEW_TOKENS: 800,
    GenParams.TEMPERATURE: 0.85,
    GenParams.TOP_P: 0.9,
    GenParams.REPETITION_PENALTY: 1.1
}

# 🔄 Load model
model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id
)

# 🚀 Generate story
def generate_story(user_prompt):
    full_prompt = f"""
    Write a complete, original, and engaging short story based on the prompt below.
    Avoid romance. Focus on suspense, mystery, science fiction, or adventure.

    Prompt: {user_prompt}
    """
    response = model.generate_text(prompt=full_prompt)
    return response.get("generated_text", str(response))

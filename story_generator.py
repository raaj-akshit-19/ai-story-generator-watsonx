from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "se1cIzHrq3IRTo5G98rl8d-biJxg6WwgZ6fh_HbM4jda"
}
project_id = "39f9e1ef-1cc7-4c01-be80-c694258c61cd"
model_id = "meta-llama/llama-3-3-70b-instruct"
parameters = {
    GenParams.DECODING_METHOD: "sample",
    GenParams.MIN_NEW_TOKENS: 500,
    GenParams.MAX_NEW_TOKENS: 800,
    GenParams.TEMPERATURE: 0.85,
    GenParams.TOP_P: 0.9,
    GenParams.REPETITION_PENALTY: 1.1
}
model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id
)
def generate_story(user_prompt):
    full_prompt = f"""
    Write a complete, original, and engaging short story based on the prompt below.
    Avoid romance. Focus on suspense, mystery, science fiction, or adventure.

    Prompt: {user_prompt}
    """
    response = model.generate_text(prompt=full_prompt)
    return response.get('generated_text', str(response))

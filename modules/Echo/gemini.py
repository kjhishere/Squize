import os
import google.generativeai as genai


class Gemini:
    def __init__(
        self,
        MODEL: str = "gemini-1.5-flash",
        APIKEY: str = os.environ["GOOGLE_API_KEY"],
    ) -> None:
        genai.configure(api_key=APIKEY)
        self.model = genai.GenerativeModel(model_name=MODEL)

    def __call__(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text

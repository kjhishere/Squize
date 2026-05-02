import os
import dotenv

from google import genai


class Gemini:

    def __init__(
        self,
        model: str = "gemini-3.1-flash-lite-preview",
        api_key: str = dotenv.get_key(".env", "GOOGLE_API_KEY") or os.environ["GOOGLE_API_KEY"],
    ) -> None:
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def __call__(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        return response.text

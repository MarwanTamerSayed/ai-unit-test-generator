import os
from dotenv import load_dotenv
from openai import OpenAI


class LLMClient:
    def __init__(self):
        load_dotenv()

        api_key = os.getenv("OPENROUTER_API_KEY")
        base_url = os.getenv("OPENROUTER_BASE_URL")
        model = os.getenv("OPENROUTER_MODEL")

        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in .env")

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        self.model = model


    def generate(self, prompt: str):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a strict CLI developer tool.\n"
                        "Your only job is to generate Python unit tests for the provided function.\n"
                        "Do NOT redefine the function under any circumstances.\n"
                        "Output ONLY executable Python test code.\n"
                        "Do NOT include explanations.\n"
                        "Do NOT include markdown.\n"
                        "Do NOT include comments outside the code.\n"
                        "Do NOT include backticks.\n"
                        "Return ONLY pure Python code.\n"
                        "DO NOT include main blocks.\n"
                        "Return ONLY test code."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.0,
            max_tokens=800,
        )

        raw_output = response.choices[0].message.content.strip()
        cleaned = self._clean_output(raw_output)
        self._validate_output(cleaned)
        return cleaned
    
    
    def _clean_output(self, text: str) -> str:
       
        if "```" in text:
            parts = text.split("```")
            if len(parts) >= 2:
                text = parts[1]

        text = text.strip()

        return text
    

    def _validate_output(self, text: str):
        forbidden_phrases = [
            "Here are",
            "Explanation",
            "Test cases:",
            "These tests"
        ]

        for phrase in forbidden_phrases:
            if phrase in text:
                raise ValueError("Model output contains forbidden explanatory text")
            if "__main__" in text:
                raise ValueError("Main execution block not allowed")


    


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
        fallback_models = [
            "mistralai/mistral-7b-instruct:free",
            "meta-llama/llama-3.3-70b-instruct:free",
            "arcee-ai/trinity-large-preview:free",
            "meta-llama/llama-3.2-3b-instruct:free",
            "qwen/qwen3-next-80b-a3b-instruct:free",
            "qwen/qwen3-vl-30b-a3b-thinking",
            "google/gemma-3-27b-it:free",

            self.model,
        ]

        last_exception = None

        for model in fallback_models:
            try:
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a strict CLI developer tool.\n"
                            "Your only job is to generate comprehensive Python unit tests for the provided function.\n"
                            "\n"
                            "Requirements:\n"
                            "- Do NOT redefine the function under any circumstances.\n"
                            "- Generate thorough and well-structured test cases.\n"
                            "- Cover normal cases.\n"
                            "- Cover edge cases.\n"
                            "- Cover boundary conditions.\n"
                            "- Include invalid or unexpected inputs if applicable.\n"
                            "- Test different input variations and data types when relevant.\n"
                            "- Include multiple assertions when appropriate.\n"
                            "- Assume the function is already imported.\n"
                            "- Strive for high test coverage.\n"
                            "\n"
                            "Output Rules:\n"
                            "- Output ONLY executable Python test code.\n"
                            "- Do NOT include explanations.\n"
                            "- Do NOT include markdown.\n"
                            "- Do NOT include backticks.\n"
                            "- Do NOT include text outside the code.\n"
                            "- Do NOT include main blocks (if __name__ == '__main__').\n"
                            "- Return ONLY pure Python test code.\n"
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

                try:
                    self._validate_output(cleaned)
                    return cleaned
                except Exception:
                    print(
                        "[WARN] The generated unit tests may be incomplete or not fully correct "
                        "because this is a free model."
                    )
                    return cleaned

            except Exception as api_error:
                print(f"[WARN] Model '{model}' API call failed. Trying next model...")
                last_exception = api_error
                continue

        raise RuntimeError(f"All models failed. Last error: {last_exception}")
    
    
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


    


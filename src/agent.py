import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class DeepResearchAgent:
    def __init__(self, model_name="gemini-2.0-flash-exp"):
        self.model = genai.GenerativeModel(model_name)

    def plan_research(self, topic):
        prompt = f"Break down the following research topic into 3-5 specific search queries: {topic}"
        response = self.model.generate_content(prompt)
        return response.text

    def synthesize_report(self, findings):
        prompt = f"Based on these findings, write a comprehensive report with citations: {findings}"
        response = self.model.generate_content(prompt)
        return response.text

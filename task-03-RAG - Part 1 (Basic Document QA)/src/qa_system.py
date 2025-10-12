from langchain.chains import RetrievalQA
from langchain.llms.base import LLM
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import os
from typing import Optional, List

class GeminiLLM(LLM):
    """LangChain-compatible wrapper for Google Gemini models."""

    model_name: str
    api_key: str

    @property
    def _llm_type(self) -> str:
        return "gemini-pro"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """Generate text using Gemini."""
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(self.model_name)
        response = model.generate_content(prompt)

        # Return plain text
        return getattr(response, "text", "")

def build_qa_chain(retriever, model_name="gemini-1.5-flash"):
    """Build RetrievalQA chain with Gemini model."""
    load_dotenv(find_dotenv())
    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        raise ValueError("GENAI_API_KEY not found in environment variables!")

    llm = GeminiLLM(model_name=model_name, api_key=api_key)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

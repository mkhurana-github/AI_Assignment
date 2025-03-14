from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import ChatPromptTemplate
import google.generativeai as genai
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

# Authenticate with Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load content directly from URL
url = input("Enter the URL: ")
query = input("Enter your search query: ")

loader = WebBaseLoader(url)
docs = loader.load()

# Extract text from the webpage
content = ' '.join(doc.page_content for doc in docs)

# Ask Gemini to find the answer from the page
prompt = ChatPromptTemplate.from_template(
    """
    You are an AI agent. Given the following webpage content:

    {content}

    Answer this question: {query}
    """
)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt.format(content=content, query=query))

print("\nAnswer:")
print(response.text)

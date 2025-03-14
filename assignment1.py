import google.generativeai as genai
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

print("Script is running...")

# Load environment variables
load_dotenv()

# Google Gemini API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Model configuration
model_name = "gemini-1.5-flash"
temperature = 0.1
model = genai.GenerativeModel(model_name)

# Load the text file
file_path = "legalAgreement.txt"  # Path to your text file
with open(file_path, "r") as file:
    text_content = file.read()

# Create a LangChain prompt for extracting JSON data
prompt_template = ChatPromptTemplate.from_template(
    """
    Given the following legal agreement text:
    {text}

    Extract the following details in JSON format:
    1. Name of the parties
    2. Payment amount
    3. Payment method
    4. Payment date
    5. Two-line description of what the agreement is about.
    """
)
formatted_prompt = prompt_template.format(text=text_content)

# Send to Gemini and get the response
response = model.generate_content(formatted_prompt, generation_config={"temperature": temperature})

# Output the response
print("Gemini Response:")
print(response.text)

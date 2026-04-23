from dotenv import load_dotenv  # .env file se environment variables load karne ke liye
from langchain_groq import ChatGroq  # Groq LLM use karne ke liye
import os  # system environment variables access karne ke liye


load_dotenv()  # .env file ko load kar rahe h

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

if __name__ == "__main__":
    response = llm.invoke("Who is 2nd PM of India?")
    print(response.content)
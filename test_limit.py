import os
from langchain_groq import ChatGroq

try:
    print("Initializing 70B...")
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.0, max_retries=0)
    
    # Create ~15,000 char payload
    text = "This is a test of the context limit. " * 500
    print(f"Payload length: {len(text)}")
    
    response = llm.invoke(f"Extract info from this: {text}")
    print("SUCCESS!")
except Exception as e:
    print(f"ERROR: {type(e).__name__} - {str(e)}")

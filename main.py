from langchain_ollama import OllamaLLM
import openai
import sys
import os
from langchain_core.prompts import ChatPromptTemplate

os.environ["OPENAI_API_KEY"]="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"
template="""
Answer the qustion below.

Here is the conversation history :{context}

Qustion: {qustion}
Answer :
"""

model= OllamaLLM(model="llama3")
prompt =ChatPromptTemplate.from_template(template)
chain=prompt | model

def handel_conversation():
    context=""
    print("Welcome to the AI chatbot! Type 'exit' to quit." )
    while True:
        user_input=input("You :")
        if user_input.lower() =="exit":
            break

        r=chain.invoke({"context": context,"qustion": user_input})
        print("SKS Bot :", r)
        context += f"\nUser: {user_input}\nAI: {r}"

if __name__=="__main__":
    handel_conversation()
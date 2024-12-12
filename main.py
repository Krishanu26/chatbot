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
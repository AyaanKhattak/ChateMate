from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Template for the chatbot conversation
template = """
Answer the question below.

Here is the conversation history:
{context}

Question:
{question}

Answer:
"""

# Initialize the language model
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Function to handle the conversation
def handle_conversation():
    context = ""
    print("Welcome to ChatMate! Type 'exit' anytime to quit the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("ChatMate: Goodbye! Have a great day!")
            break
        
        # Generate the response from the AI model
        result = chain.invoke({"context": context, "question": user_input})
        print("ChatMate: ", result)
        
        # Update the context with the new conversation
        context += f"\nUser: {user_input}\nChatMate: {result}"

# Main function to run the chatbot
if __name__ == "__main__":
    handle_conversation()

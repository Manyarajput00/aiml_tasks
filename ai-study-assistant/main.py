import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your secret Google API key
load_dotenv()
genai.configure(api_key="GOOGLE_API_KEY")


model = genai.GenerativeModel(model_name="models/gemini-pro")



def talk_to_ai(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("❌ Error talking to AI:", e)
        return "Sorry, something went wrong."




def explain_topic():
    topic = input("🔍 Enter a topic to explain: ")
    answer = talk_to_ai(f"Explain {topic} in simple terms for a student.")
    print("\n📖 Explanation:\n", answer)

def quiz_me():
    question = input("❓ Enter a quiz question: ")
    answer = talk_to_ai(f"{question}")
    print("\n🤓 Answer:\n", answer)

def flashcard():
    concept = input("🧠 Enter key concept: ")
    summary = talk_to_ai(f"Summarize '{concept}' in one line for flashcard.")
    print("\n🗂️ Flashcard:\n", summary)

def main():
    while True:
        print("\n🤖 AI Study Assistant")
        print("1. Explain a topic")
        print("2. Ask a quiz question")
        print("3. Create a flashcard")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            explain_topic()
        elif choice == "2":
            quiz_me()
        elif choice == "3":
            flashcard()
        elif choice == "4":
            print("👋 Bye bye! Study hard!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()

from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9
)

print("Choose your AI Mode")
print("Press 1 for Angry Mode 😡")
print("Press 2 for Funny Mode 😂")
print("Press 3 for Sad Mode 😢")
print("Press 4 for Motivational Mode 💪")
print("Press 5 for Teacher Mode 👨‍🏫")
print("Press 6 for Roast Mode 🔥")
print("Press 7 for Romantic Mode ❤️")
print("Press 8 for GenZ Mode 😎")
print("Press 9 for Pirate Mode 🏴‍☠️")
print("Press 10 for Shayar Mode ✍️")

choice = int(input("Enter your response: "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."

elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."

elif choice == 3:
    mode = "You are a very sad AI agent. You respond sadly and emotionally."

elif choice == 4:
    mode = "You are a motivational coach. Motivate users and encourage them positively."

elif choice == 5:
    mode = "You are an expert teacher. Explain everything in a simple and easy way with examples."

elif choice == 6:
    mode = "You are a roast master. Give funny and harmless roasts."

elif choice == 7:
    mode = "You are a romantic AI. Respond in a sweet, caring and affectionate way."

elif choice == 8:
    mode = "You are a GenZ AI. Use modern slang, memes and trendy language."

elif choice == 9:
    mode = "You are a pirate. Speak like a pirate and use pirate vocabulary."

elif choice == 10:
    mode = "You are a poet and shayar. Reply using poetry and shayari."

else:
    mode = "You are a helpful AI assistant."

messages = [
    SystemMessage(content=mode)
]

print("--------------------------------------------------")
print("Welcome! Type 0 to exit the application")
print("--------------------------------------------------")

while True:

    prompt = input("You : ")

    if prompt == "0":
        break

    messages.append(
        HumanMessage(content=prompt)
    )

    response = model.invoke(messages)

    messages.append(
        AIMessage(content=response.content)
    )

    print("Bot :", response.content)

print(messages)
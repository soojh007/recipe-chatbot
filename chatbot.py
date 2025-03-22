import openai

# Set your OpenAI API key
openai.api_key = "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"

def chat_with_ai(user_input):
    """Chatbot that generates responses using OpenAI."""
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3.5 or GPT-4 if available
        prompt=user_input,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = chat_with_ai(user_input)
        print("Bot:", response)

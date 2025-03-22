import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Use OpenAI API Key from environment variables
openai.api_key = os.getenv("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")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

import openai
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins

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

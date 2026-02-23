from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": data["messages"],
            "temperature": 0.7,
            "max_tokens": 400
        }
    )

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
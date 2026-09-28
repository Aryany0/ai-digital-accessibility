from dotenv import load_dotenv
import os
import ollama

load_dotenv()
print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "AI Digital Accessibility Backend is running!"


@app.route("/simplify", methods=["POST"])
def simplify_text():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": (
                    "Rewrite the following text in simple, clear English. "
                    "Keep the original meaning. Do not add unnecessary information.\n\n"
                    + text
                )
            }
        ]
    )

    simplified_text = response["message"]["content"]

    return jsonify({
        "original": text,
        "simplified": simplified_text
    })

if __name__ == "__main__":
    app.run(debug=True)
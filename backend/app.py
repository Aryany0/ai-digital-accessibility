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
        return jsonify({
            "error": "No text provided"
        }), 400

    
    simplified_text = (
        "This is a temporary simplified version of: " + text
    )

    return jsonify({
        "original": text,
        "simplified": simplified_text
    })


if __name__ == "__main__":
    app.run(debug=True)
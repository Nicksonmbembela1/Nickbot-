import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("message")
    response = model.generate_content(prompt)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

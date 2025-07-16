from flask import Flask, render_template, request, jsonify, session, send_file
from datetime import datetime
import os, io
import together
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "secret")  # for session

client = together.Together(api_key=os.getenv("TOGETHER_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatpage")
def chat_page():
    session["chat_history"] = []
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    today = datetime.now().strftime("%A, %d %B %Y")
    current_time = datetime.now().strftime("%I:%M %p")

    system_prompt = f"""
You are a helpful AI assistant with a panda mascot named Kramig 🐼.
Be clear, structured, friendly, and use emojis when relevant.
📅 Date: {today}
🕒 Time: {current_time}
"""

    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        max_tokens=300,
        temperature=0.7,
    )

    reply = response.choices[0].message.content.strip()
    session["chat_history"].append(f"You: {user_input}\nAI: {reply}\n")
    return jsonify({"reply": reply})

@app.route("/download", methods=["GET"])
def download_chat():
    history = "\n".join(session.get("chat_history", []))
    return send_file(
        io.BytesIO(history.encode("utf-8")),
        mimetype="text/plain",
        as_attachment=True,
        download_name="chat_history.txt"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)), debug=True)
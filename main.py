from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import fitz  # PyMuPDF
import together
from dotenv import load_dotenv

load_dotenv()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

client = together.Together(api_key=os.getenv("TOGETHER_API_KEY"))
file_text_content = ""  # Global variable to store uploaded file content

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatpage")
def chat_page():
    return render_template("chat.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    global file_text_content
    uploaded_file = request.files["file"]
    if uploaded_file.filename.endswith(".pdf"):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
        uploaded_file.save(file_path)
        doc = fitz.open(file_path)
        file_text_content = "\n".join([page.get_text() for page in doc])
        return jsonify({"success": True, "preview": file_text_content[:1000] + "..."})
    return jsonify({"success": False, "error": "Only PDF files are supported."})

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    system_prompt = f"""
You are a friendly and helpful assistant for students. 
Use emojis, answer in structured points, and make the response very clear.

If file content is available, use it to answer questions.

--- File Content (if uploaded) ---
{file_text_content[:3000]}
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
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
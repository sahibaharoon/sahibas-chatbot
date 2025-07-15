# 🤖 Sahiba's AI Chatbot

> A friendly and smart chatbot built with Flask, Together AI, and PDF upload support — made with ♥️ by Sahiba Haroon.


---

## 🚀 Features

- 🌈 Beautiful UI with a friendly vibe
- 🧠 AI-powered chat using [Together API](https://www.together.ai/)
- 📄 Upload PDFs and chat based on their content
- 💬 Structured, emoji-rich responses
- 🖱️ Smooth typing animation and file preview
- 📱 Fully responsive front-end

---

## 📂 Project Structure
<pre>
<code>
📁 chatbot-project/
├── main.py                 # Flask backend (entry point)
├── templates/
│   ├── index.html          # Welcome / landing page
│   └── chat.html           # Chat interface
├── static/
│   ├── style.css           # Custom styling
│   ├── script.js           # Typing animation & chat logic
│   
├── uploads/                # Uploaded PDF files (temporary)
├── .env                    # Your Together API key (not pushed)
└── requirements.txt        # Python dependencies
</code>
</pre>

---

## 🛠️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/sahibaharoon/sahibas-chatbot.git
   cd chatbot-project
2. **Create virtual environment**

3. **Install dependencies**
     - pip install -r requirements.txt
4. **Add env file**
   - Make a together api key and add it
   - TOGETHER_API_KEY=yourkey
6. **Run app**
   - python3 main.py


   

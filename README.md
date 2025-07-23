# 🤖 FAQ Chatbot using Flask

A simple and customizable FAQ chatbot built using **Python** and **Flask**. It reads frequently asked questions from a JSON file and returns accurate answers to user queries. This project is ideal for businesses, customer support portals, and educational platforms.

---

## 📂 Project Structure

faq_chatbot_project/
│
├── app.py # Main Flask application script
│
├── chatbot/ # Core chatbot logic
│ ├── init.py
│ ├── chatbot.py # Logic to generate response
│ ├── data_loader.py # Loads the JSON-based FAQ data
│ └── preprocess.py # Preprocesses user input
│
├── data/
│ └── faqs.json # Question-Answer pairs in JSON format
│
├── static/
│ └── style.css # CSS for the frontend chat interface
│
├── templates/
│ └── index.html # HTML UI for chatbot
│
├── venv/ # Virtual environment (excluded via .gitignore)
│
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules (ignores venv, pycache, etc.)
└── README.md # This file

yaml
Copy code

---

## 🚀 Features

- 💬 Chat interface for asking questions
- 📄 FAQ data loaded from JSON
- 🧠 Input cleaning/preprocessing
- 🎨 Simple and customizable frontend
- 🧩 Modular Python code
- ⚡ Fast and lightweight with Flask

---

## 📦 Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
▶️ How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/rk-srinath/FAQ_chatbot_project.git
cd FAQ_chatbot_project
(Optional) Create & activate virtual environment:

bash
Copy code
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Install required packages:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
Open browser and go to:

cpp
Copy code
http://127.0.0.1:5000
💡 How It Works
User types a question into the chat interface

The question is preprocessed (e.g., converted to lowercase)

The chatbot compares it with stored questions in faqs.json

The closest match's answer is returned and displayed

✍️ Customize FAQs
To change the chatbot’s knowledge, edit data/faqs.json:

json
Copy code
[
  {
    "question": "How do I reset my password?",
    "answer": "Click on 'Forgot password' and follow the instructions."
  },
  {
    "question": "What is your refund policy?",
    "answer": "We offer a 30-day refund guarantee."
  }
]
🌐 Deployment Options
You can deploy this project on:

🚀 Render

🛤️ Railway

🌍 PythonAnywhere

🌀 Replit

☁️ Heroku (if no DB)

# 🤖 AI-Chatbot

A lightweight Python terminal chatbot powered by the OpenAI Responses API.

> A clean starter project for learning how to build an AI assistant with Python.

## ✨ Features

- 💬 Interactive terminal chat
- 🧠 OpenAI Responses API integration
- 🔐 API key kept outside source code
- 🛡️ Safe `.gitignore` setup for local secrets
- 🧩 Simple structure that is easy to extend

## 🛠️ Tech Stack

- Python 3
- OpenAI Python SDK
- OpenAI Responses API

## 📁 Project Structure

```text
AI-Chatbot/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/harsh618-netizen/AI-Chatbot.git
cd AI-Chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Set `OPENAI_API_KEY` in your local environment. Do **not** put a real key in GitHub or commit it to the repository.

Linux/macOS:

```bash
export OPENAI_API_KEY="your_api_key"
```

Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key"
```

### 4. Run the chatbot

```bash
python main.py
```

Type `exit` or `quit` to stop the chat.

## 🔒 Security

Never commit a real OpenAI API key to this public repository. Keep credentials in environment variables or another local secret store that is excluded from Git.

## 🔮 Future Ideas

- Conversation history
- Voice input/output
- GUI interface
- Tool calling and agent capabilities
- Persistent chat sessions

## 📌 Project Status

**Active starter project** — built to be expanded into a more capable Python AI agent.

## 📄 License

This project is available for learning and personal development.

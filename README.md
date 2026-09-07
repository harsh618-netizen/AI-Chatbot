# AI-Chatbot

A simple Python AI chatbot powered by the OpenAI API.

## Features

- Terminal-based chat interface
- OpenAI Responses API
- Environment-variable based API key handling
- Clean starter structure for future agent features

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your API key as an environment variable.

Linux/macOS:

```bash
export OPENAI_API_KEY="your_api_key"
```

Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key"
```

4. Run:

```bash
python main.py
```

Type `exit` or `quit` to stop.

## Security

Never commit a real API key to this public repository. Keep secrets in environment variables or a local `.env` file that is ignored by Git.

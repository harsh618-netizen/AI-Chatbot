# Contributing to AI-Chatbot

Thanks for your interest in improving AI-Chatbot! 🚀

## How to contribute

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and keep the code clean and focused.
4. Test the project locally.
5. Commit your changes with a clear message:
   ```bash
   git commit -m "feat: describe your change"
   ```
6. Push your branch and open a pull request.

## Development setup

```bash
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

Set `OPENAI_API_KEY` in your local environment before running the application.

## Pull request guidelines

- Explain what changed and why.
- Keep pull requests focused on one main improvement.
- Do not commit API keys, passwords, tokens, or other secrets.
- Update documentation when behavior or setup changes.
- Add or update tests when appropriate.

## Code style

Prefer clear, readable Python and small, maintainable changes. Avoid unrelated formatting changes in feature pull requests.

## Security

Never include a real OpenAI API key in source code, commits, issues, or pull requests. Use environment variables or a secure secret manager.

Thank you for contributing! ❤️

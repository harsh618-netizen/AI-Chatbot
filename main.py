import os
from openai import OpenAI

SYSTEM_PROMPT = """You are AI-Chatbot, a helpful and friendly Python AI agent.
Answer clearly and concisely. If you are unsure, say so instead of inventing facts.
"""


def main() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Set it as an environment variable before running."
        )

    client = OpenAI()

    print("AI-Chatbot is ready! Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        try:
            response = client.responses.create(
                model="gpt-5.5",
                instructions=SYSTEM_PROMPT,
                input=user_input,
            )
            print(f"AI: {response.output_text}\n")
        except Exception as exc:
            print(f"AI: Sorry, something went wrong: {exc}\n")


if __name__ == "__main__":
    main()

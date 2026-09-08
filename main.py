import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI


def main():
    print("Hello from ai-agent!")

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("API key no loaded")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true",
                        help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "user", "content": args.user_prompt},
    ]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    generate_content(client, messages, args.verbose)


def generate_content(
        client: OpenAI,
        messages: list[dict],
        verbose: bool = False
        ) -> None:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )
    if not response.usage:
        raise RuntimeError("Failed API request")
    if verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"Response: {response.choices[0].message.content}")


if __name__ == "__main__":
    main()

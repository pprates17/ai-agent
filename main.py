import os
import sys
import argparse
import json

from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERS


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
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

    for _ in range(MAX_ITERS):
        try:
            final_response = generate_content(client, messages, args.verbose)
            if final_response:
                print(f"Response: {final_response}")
                return
        except Exception as e:
            print(f"Error generating content {e}")

    print(f"Maximum number of iterations({MAX_ITERS}) reached...")
    sys.exit(1)


def generate_content(
        client: OpenAI,
        messages: list[dict],
        verbose: bool = False
        ) -> str | None:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions
    )
    if not response.usage:
        raise RuntimeError("Failed API request")
    if verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    response = response.choices[0].message
    messages.append(response)

    if not response.tool_calls:
        return response.content

    for tool_call in response.tool_calls:
        function_args = json.loads(tool_call.function.arguments or "{}")
        print(f"Calling function: {tool_call.function.name}({function_args})")
        result_message = call_function(tool_call)
        print(f"Result message: {result_message}")

        if result_message['content'] == "":
            raise Exception("Error: Empty result")

        messages.append(result_message)

        if verbose:
            print(f"-> {result_message['content']}")
    return None


if __name__ == "__main__":
    main()

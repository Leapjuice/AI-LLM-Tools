import asyncio
from openai import AsyncOpenAI

# WARNING: Hardcoding API keys is not secure.
# It is recommended to use environment variables or a secret management system.
# For personal, local scripts, this can be acceptable, but never share code
# with a hardcoded key.

# THIS SCRIPT USES GROK 4 (grok-4-0709) LANGUAGE MODEL BY DEFAULT

API_KEY = "<--- INSERT X.AI API KEY HERE --->"

async def main():
    """
    Main function to run the interactive chat session with the Grok-4 model
    using the OpenAI SDK, with conversation memory.
    """
    if not API_KEY:
        print("Error: API_KEY is not set. Please set it directly in the script.")
        return

    print("Initializing Grok-4 chat...")
    print("Type '/new' to start a new conversation.")
    print("Type '/exitnow' to end the session.")
    print("---------------------------------")

    try:
        # Initialize the asynchronous OpenAI client, pointing it to the xAI API endpoint.
        client = AsyncOpenAI(
            api_key=API_KEY,
            base_url="https://api.x.ai/v1"
        )
        model_name = "grok-4-0709"
        print(f"Successfully configured client for xAI API. Using model: {model_name}")

    except Exception as e:
        print(f"Error: Could not initialize the OpenAI client.")
        print(f"Details: {e}")
        return

    # List to store the history of the current conversation
    conversation_history = []

    # Start the main conversation loop
    while True:
        try:
            # Determine the appropriate prompt based on conversation history
            if not conversation_history:
                prompt_text = "\nWhat would you like to ask Grok 4?: "
            else:
                prompt_text = "\nWhat else?: "
            
            user_prompt = input(prompt_text)

            # If the user just presses enter, prompt again
            if not user_prompt.strip():
                continue
            
            # Command to exit the program
            if user_prompt.strip().lower() == '/exitnow':
                print("\nAlright, stopping now. Goodbye!")
                break
            
            # Command to start a new chat session
            if user_prompt.strip().lower() == '/new':
                conversation_history = []
                print("\n--- New chat session started. ---")
                continue

            # Add the user's message to the history
            conversation_history.append({"role": "user", "content": user_prompt})

            print("\nGrok says: ", end="", flush=True)

            # Variable to accumulate the full response from the model
            full_response = ""

            # Create the chat completion request with the entire conversation history
            response_stream = await client.chat.completions.create(
                model=model_name,
                messages=conversation_history, # Send the whole history
                stream=True
            )

            # Asynchronously iterate through the stream, print the content, and build the full response
            async for chunk in response_stream:
                content = chunk.choices[0].delta.content
                if content:
                    print(content, end="", flush=True)
                    full_response += content
            
            # Add the assistant's complete response to the history for context in the next turn
            if full_response:
                conversation_history.append({"role": "assistant", "content": full_response})

            print() # Print a newline after the full response is streamed

        except Exception as e:
            print(f"\nAn error occurred during the API call: {e}")
            print("Please check your API key and network connection, then try your request again.")
            # Remove the last user message from history if the API call failed
            if conversation_history and conversation_history[-1]["role"] == "user":
                conversation_history.pop()
            # Continue the loop to allow the user to try again

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting program.")

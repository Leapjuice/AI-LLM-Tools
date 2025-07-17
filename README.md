Grok-4 Command-Line Chat Client
This is a simple yet powerful Python script that allows you to chat with the Grok-4 model directly from your terminal. It uses the OpenAI SDK to connect to the xAI API, providing a seamless and continuous conversation experience.

The client maintains a session history, enabling you to ask follow-up questions and have context-aware conversations.

Features
Interactive Chat: Engage in a continuous conversation with the Grok-4 model.

Conversation Memory: The script remembers the entire chat history for the current session, allowing for contextual follow-ups and revisions.

Streaming Responses: Watch the model's response get printed to the console in real-time.

Simple Commands: Use /new to clear the history and start a new conversation, and /exitnow to gracefully end the session.

Resilient Connection: Basic error handling is included to manage API connection issues.

How to Use
1. Prerequisites
Python 3.7+

An API key from xAI

2. Setup
It is highly recommended to run this script in a virtual environment to avoid conflicts with other Python projects.

# 1. Navigate to the project directory
cd /path/to/your/project

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate

3. Installation
With your virtual environment active, install the necessary library:

pip install openai

4. Configuration
Open the grok-chat.py script and replace the placeholder API key with your own xAI key:

# Replace this with your actual key
API_KEY = "YOUR_XAI_API_KEY_HERE"

5. Run the Script
You're all set! Start the chat client by running:

python grok-chat.py

Disclaimer
This script is intended for personal use. Hardcoding API keys directly into the script is not a secure practice for production or shared environments. For more secure applications, consider using environment variables or a secret management tool.

# Steps to Set Up the Flask App:
1. Install Flask and Requests: Run the following command to install the required dependencies:
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install flask requests
```
2. Set Environment Variables: Set the required environment variables:
```bash
export WEBHOOK_VERIFY_TOKEN="your_verify_token"
export GRAPH_API_TOKEN="your_graph_api_token"
export PORT=5000
```
3. Run the Flask App: Start the Flask app:
```bash
python webhook.py
```
4. Expose the App to the Internet: Use a tool like ngrok to expose the app to the internet for webhook testing:
```bash
ngrok http 5000
```
5. Set Up the Webhook: Use the public URL from ngrok to set up the webhook in the Facebook Developer Console.

This Flask app mirrors the functionality of the original Node.js app, including logging incoming messages, verifying the webhook, and sending replies via the WhatsApp Cloud API.
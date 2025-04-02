import os
import json
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_VERIFY_TOKEN = os.getenv("WEBHOOK_VERIFY_TOKEN")
GRAPH_API_TOKEN = os.getenv("GRAPH_API_TOKEN")
PORT = int(os.getenv("PORT", 5000))


@app.route("/webhook", methods=["POST"])
def webhook():
    # Log incoming messages
    print("Incoming webhook message:", json.dumps(request.json, indent=2))

    # Check if the webhook request contains a message
    message = (
        request.json.get("entry", [{}])[0]
        .get("changes", [{}])[0]
        .get("value", {})
        .get("messages", [{}])[0]
    )

    # Check if the incoming message contains text
    if message and message.get("type") == "text":
        # Extract the business number to send the reply from it
        business_phone_number_id = (
            request.json.get("entry", [{}])[0]
            .get("changes", [{}])[0]
            .get("value", {})
            .get("metadata", {})
            .get("phone_number_id")
        )

        # Send a reply message
        reply_url = f"https://graph.facebook.com/v18.0/{business_phone_number_id}/messages"
        headers = {"Authorization": f"Bearer {GRAPH_API_TOKEN}"}

        # Reply to the message
        reply_data = {
            "messaging_product": "whatsapp",
            "to": message["from"],
            "text": {"body": "Echo: " + message["text"]["body"]},
            "context": {"message_id": message["id"]},
        }
        requests.post(reply_url, headers=headers, json=reply_data)

        # Mark the incoming message as read
        read_data = {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": message["id"],
        }
        requests.post(reply_url, headers=headers, json=read_data)

    return "", 200


@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    # Check the mode and token sent are correct
    if mode == "subscribe" and token == WEBHOOK_VERIFY_TOKEN:
        print("Webhook verified successfully!")
        return challenge, 200
    else:
        return "Forbidden", 403


@app.route("/")
def home():
    return "<pre>Nothing to see here.\nCheckout README.md to start.</pre>"


if __name__ == "__main__":
    print(f"Server is listening on port: {PORT}")
    app.run(host="0.0.0.0", port=PORT)
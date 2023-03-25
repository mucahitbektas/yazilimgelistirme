import json
import websocket

# Define the URL of the WebSocket server
ws_url = "wss://example.com"

# Define the message to be sent
response = {
    "action": "CONFIRM",
    "name": "Mücahit BEKTAŞ",
    "email": "mucahitbektas@gmail.com",
    "phone": "5454644546",
    "confirmation_code": "4tq14t88tq52h447t0e66436t4eehk851e683te2bb0846teh047f5t763822af9"
}

# Encode the message as a JSON object
message = json.dumps(response)

# Define the function to be called when the WebSocket connection is opened
def on_open(ws):
    # Send the message to the server
    ws.send(message)

# Define the function to be called when a message is received from the server
def on_message(ws, message):
    # Print the received message to the console
    print(f"Received message from server: {message}")

# Create a WebSocket connection to the server and attach the event handlers
ws = websocket.create_connection(ws_url)
ws.send('Hello, server!')
ws.send('Thanks for the message!')
ws.close()

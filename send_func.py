import asyncio 
import json
import websockets

def message_reader(filename='message.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        db = json.load(f)
    message_dict = db['message']
    return message_dict

async def send_json_message(message):
    async with websockets.connect("wss://cekirdektenyetisenler.kartaca.com/ws") as websocket:
        json_message = json.dumps(message)
        await websocket.send(json_message)

if "__main__" == __name__:
    message = message_reader("message.json")
    asyncio.run(send_json_message(message))
    

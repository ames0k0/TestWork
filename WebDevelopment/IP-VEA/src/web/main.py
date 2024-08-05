import os
import json

import motor.motor_asyncio
from fastapi import FastAPI


tags_metadata = [
    {
        "name": "messages",
        "description": "Operations with messaages.",
    },
    {
        "name": "dev",
        "description": "Dev functions to manage messages.",
    },
]

app = FastAPI(
    title='Messaging application',
    summary='Writing (anonym) messages. FastAPI + MongoDB + aiogram3',
    openapi_tags=tags_metadata,
)
client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://root:toor@localhost:27017/"
)

db = client.app_messages
messages_collection = db.get_collection("messages")


@app.post('/api/v1/message/', tags=['messages'])
async def create_message(message: str) -> str:
    """ Creates a message, and Returns "OK"
    """
    await messages_collection.insert_one({"message": message})
    return "OK"


@app.get('/api/v1/messages/', tags=['messages'])
async def get_messages(n_messages: int | None = None) -> list[str]:
    """ Returns list of messages (`n_messages=20`)
    """
    if (not n_messages) or n_messages < 1:
        n_messages = 20
    messages = []
    for message in await messages_collection.find().to_list(n_messages):
        messages.append(message["message"])
    return messages


@app.delete('/api/v1/messages/', tags=["dev"])
async def delete_messages() -> str:
    """ Deletes all messages
    """
    await messages_collection.drop()
    return "OK"

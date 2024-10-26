#          █  █ █▄ █ █▄ █ █▀▀ ▀▄▀ █▀█ █▄ █
#          ▀▄▄▀ █ ▀█ █ ▀█ ██▄  █  █▄█ █ ▀█ ▄
#                © Copyright 2024
#            ✈ https://t.me/unneyon
#           📩 https://vk.com/unneyon

# 🔒 Licensed under CC-BY-NC-ND 4.0 unless otherwise specified.
# 🌐 https://creativecommons.org/licenses/by-nc-nd/4.0
# + attribution
# + non-commercial
# + no-derivatives

# You CANNOT edit this file without direct permission from the author.
# You can redistribute this file without any changes.

import aiohttp

from fastapi import Request
from fastapi.responses import JSONResponse

import utils


async def delete(request: Request, body: dict):
    obj = body['object']
    ans: dict = await utils.vk.request(
        "messages.delete",
        data={
            "delete_for_all": 1,
            "conversation_message_ids": obj['conversation_message_ids'],
            "peer_id": obj['chat_local_id'] + 2e9,
            "v": "5.186"
        }
    )
    cmids = [i['conversation_message_id'] for i in ans['response'] if i.get('response', 0) == 1]

    if ans.get("response"):
        cmids = [i['conversation_message_id'] for i in ans['response'] if i.get('response', 0) == 1]
        if len(cmids) > 0:
            return JSONResponse(
                content={
                    "ok": True,
                    "conversation_message_ids": [i['conversation_message_id'] for i in ans['response'] if i.get('response', 0) == 1]
                },
                status_code=200
            )
    else:
        return JSONResponse(
            content={
                "ok": False,
                "error": {
                    "type": "INTERNAL_SERVER_ERROR",
                    "message": "Бот не смог удалить сообщения."
                }
            },
            status_code=500
        )
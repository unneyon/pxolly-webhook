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


async def reset_theme(request: Request, body: dict):
    obj = body['object']
    await utils.vk.request(
        "messages.resetConversationStyle",
        data={
            "peer_id": obj['chat_local_id'] + 2e9,
            "v": "5.186"
        }
    )
    
    return JSONResponse(
        content={
            "ok": True
        }
    )


async def set_theme(request: Request, body: dict):
    obj = body['object']
    await utils.vk.request(
        "messages.setConversationStyle",
        data={
            "peer_id": obj['chat_local_id'] + 2e9,
            "style": obj['style'],
            "v": "5.186"
        }
    )

    return JSONResponse(
        content={
            "ok": True
        }
    )
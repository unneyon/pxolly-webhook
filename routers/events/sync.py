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

code = """
var e = 2000000000;
var h = API.messages.search({{
    q: '{text}',
    count: 5,
}}).items;

var i = 0;
while (i < h.length) {{
    if (
        h[i].peer_id > e &&
        '{text}' == h[i].text &&
        {from_id} == h[i].from_id &&
        {date} == h[i].date &&
        {cmid} == h[i].conversation_message_id
    ) {{
        return h[i].peer_id - e;
    }}
    i = i + 1;
}}
return false;
"""

async def sync_chat(request: Request, body: dict):
    msg = body['object']['message']
    ans = await utils.vk.execute(
        code = code.format(
            text=msg['text'],
            from_id=msg['from_id'],
            date=msg['date'],
            cmid=msg['conversation_message_id']
        )
    )

    if ans.get('response'):
        return JSONResponse(
            content={
                "ok": True,
                "local_id": ans.get('response', 0)
            },
            status_code=200
        )
    else:
        return JSONResponse(
            content={
                "ok": False,
                "error": {
                    "type": "INTERNAL_SERVER_ERROR",
                    "message": "Вебхук не смог найти чат, в котором происходит синхронизация. Попробуйте ещё раз или обратитесь к администратору вебхука."
                }
            },
            status_code=500
        )
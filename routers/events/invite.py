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
import vkbottle

from fastapi import Request
from fastapi.responses import JSONResponse

import utils


async def invite_user(request: Request, body: dict):
    obj = body['object']
    try:
        ans = await utils.vk.messages.add_chat_user(
            chat_id=obj['chat_local_id'],
            user_id=obj['user_id']
        )
        return JSONResponse(
            content={"ok": True},
            status_code=200
        )
    except vkbottle.VKAPIError[925] as e:
        return JSONResponse(
            content={
                "ok": False,
                "error": {
                    "type": "BOT_ACCESS_DENIED",
                    "message": f"VK API says: [{e.code}] {e.error_msg}"
                }
            }
        )
    except vkbottle.VKAPIError[981] as e:
        return JSONResponse(
            content={
                "ok": False,
                "error": {
                    "type": "INVALID_PRIVACY_SETTINGS_FOR_INVITE",
                    "message": f"VK API says: [{e.code}] {e.error_msg}"
                }
            }
        )
    except vkbottle.VKAPIError as e:
        return JSONResponse(
            content={
                "ok": False,
                "error": {
                    "type": "VK_API_ERROR",
                    "message": f"VK API says: [{e.code}] {e.error_msg}"
                }
            }
        )
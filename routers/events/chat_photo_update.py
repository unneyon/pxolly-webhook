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

import io
import requests
import vkbottle
from vkbottle import PhotoChatFaviconUploader

from fastapi import Request
from fastapi.responses import JSONResponse

import utils


async def update_photo(request: Request, body: dict):
    obj = body['object']
    try:
        if obj['is_remove'] == 0:
            file = io.BytesIO(requests.get(obj['photo_url']).content)
            file.name = "photo.png"
            uploader = PhotoChatFaviconUploader(utils.vk)
            photo = await uploader.raw_upload(
                obj['chat_local_id'],
                file_source=file
            )
        else:
            await utils.vk.messages.delete_chat_photo(chat_id=obj['chat_local_id'])
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
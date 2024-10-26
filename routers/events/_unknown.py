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

import json
import logging

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

import utils

logger = logging.getLogger(__name__)


async def unknown_event(request: Request, body: json):
    logger.debug(body)
    return JSONResponse(
        content={
            "ok": False,
            "error": {
                "type": "UNKNOWN_EVENT",
                "message": "Бот отправил неизвестный вебхуку тип события. Обратитесь к администратору вебхука."
            }
        },
        status_code=418
    )
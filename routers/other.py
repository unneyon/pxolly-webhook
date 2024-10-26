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

import datetime
import pytz
import time

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

import utils
from .events import handlers, unknown_event


other = APIRouter()

templates = Jinja2Templates(directory="templates")


@other.get("/")
async def start(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": utils.config['web-check']['title'],
            "text": utils.config['web-check']['text'],
            "little_text": utils.config['web-check']['little_text'],
            "uptime": str(datetime.timedelta(seconds=round(time.perf_counter() - utils.init_ts))),
            "time": datetime.datetime.now(tz=pytz.timezone("Europe/Moscow")).strftime("%d.%m.%Y %H:%M")
        },
        status_code=200
    )


@other.post("/")
async def start(request: Request):
    body = await request.json()
    func = handlers.get(body['type'], unknown_event)
    return await func(request, body)
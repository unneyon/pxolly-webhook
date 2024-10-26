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
import asyncio
import functools
import json
import os
import time
import vkbottle


if os.path.isfile("config.json"):
    config = json.loads(open("config.json", "r", encoding="utf-8").read())
else:
    dcfg = json.loads(open("config.example.json", "r", encoding="utf-8").read())
    json.dumps(dcfg, open("config.json", "w+", encoding="utf-8"), ensure_ascii=False, indent=4)
init_ts = time.perf_counter()

if config['credential']['vk_token']:
    vk = vkbottle.API(config['credential']['vk_token'])
else:
    print("\033[31mВы не заполнили поле `vk_token` в `config.json`!\033[0m")
    exit()


def print_copyrights():
    print(f"\033[36m          █  █ █▄ █ █▄ █ █▀▀ ▀▄▀ █▀█ █▄ █\033[0m")
    print(f"\033[36m          ▀▄▄▀ █ ▀█ █ ▀█ ██▄  █  █▄█ █ ▀█ ▄\033[0m")
    print(f"\033[36m                © Copyright 2024\033[0m")
    print(f"\033[36m            ✈ https://t.me/unneyon\033[0m")
    print(f"\033[36m           📩 https://vk.com/unneyon\033[0m", end="\n\n")
    print(f"\033[36m 🔒 Licensed under the GNU GPLv3\033[0m")
    print(f"\033[36m 🌐 https://www.gnu.org/licenses/gpl-3.0.html\033[0m", end="\n\n")


async def get_confirm_code():
    if not config['credential']['pxolly_token']:
        print("\033[31mВы не заполнили поле `pxolly_token` в `config.json`!\033[0m")
        exit()
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url="https://api.pxolly.ru/m/callback.getConfirmationCode",
            params={"access_token": config['credential']['pxolly_token']}
        ) as request:
            result = await request.json()
    return result.get("response", {}).get("code", None)


def run_sync(func, *args, **kwargs):
    return asyncio.get_event_loop().run_in_executor(
        None,
        functools.partial(func, *args, **kwargs),
    )
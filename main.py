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

import uvicorn
from loguru import logger

import utils
from routers import app

utils.print_copyrights()
logger.remove()

if utils.config['port'] < 1024:
    print("\033[31mУкажите порт в `config.json` больше, чем 1024\033[0m")
    exit()


if __name__ == "__main__":
    print(f"\033[36mПриложение [pxolly. webhook] успешно запущено!\033[0m")
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=utils.config['port']
    )
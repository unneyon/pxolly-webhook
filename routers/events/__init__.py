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

from ._unknown import unknown_event
from .confirmation import confirm
from .sync import sync_chat
from .delete_for_all import delete
from .invite import invite_user
from .chat_photo_update import update_photo
from .themes import set_theme, reset_theme

handlers = {
    "confirmation": confirm,
    "sync": sync_chat,
    "delete_for_all": delete,
    "invite_user": invite_user,
    "chat_photo_update": update_photo,
    "set_theme": set_theme,
    "reset_theme": reset_theme,
    "bot_command": unknown_event
}
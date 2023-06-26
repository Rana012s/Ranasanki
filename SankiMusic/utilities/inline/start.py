from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from SankiMusic.utilities.config import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="≽ 𝐂ᴏᴍᴍᴀɴᴅs ≼",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="✮ 𝐒ᴇᴛᴛɪɴɢs ✮", callback_data="settings_helper"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❀⋟ 𝐇ᴇʟᴘ ⋞❀", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ 𝐔ᴘᴅᴀᴛᴇs ✭", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="✭ 𝐒ᴜᴘᴘᴏʀᴛ ✭", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="✮ 𝐒ᴏᴜʀᴄᴇ ✮", url="https://te.legra.ph/file/5fa7b4d86dcd5720ef30c.mp4"
            )
        ]
     ]
    return buttons

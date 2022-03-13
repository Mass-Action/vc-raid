#@TheVenomXD

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from .. import vcbot, SUDO_USERS, HNDLR, hl, START_VID

# @vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["start"], prefixes=HNDLR))
# async def start(_, e: Message):
   # video=START_VID,
  # await vcbot.send_video(e.chat.id, video, f"Vc Raid Bot Is Working Fine. \nSend `{hl}help` To Know Your Commands. \n\n< Powered By @ArrayCore >")

START_MSG = "**Hello [{}](tg://user?id={}) !** \n\n __ • I'm ArrayCore An Advance And Simple Group Voice Call Bot__ \n\n **Click Below Buttons for More Info**",         

@vcbot.on_message(filters.user(SUDO_USERS) & ~filters.private & filters.command(["end"], prefixes=HNDLR))
async def _start(_, ok: Message):
        await vcbot.send_message(Message.chat.id,
        text=START_MSG.format(Message.from_user.first_name, Message.from_user.id),
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Channel •", url="https://t.me/ArrayCore"),
                    InlineKeyboardButton(
                        "• Support •", url="https://t.me/DNHxHELL")
                ], [
                    InlineKeyboardButton(
                        "• Repo •", url="https://github.com/desinobita/ArrayCore-")
                ]]
            ))

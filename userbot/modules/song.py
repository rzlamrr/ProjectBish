# Originally from Bothub
# Port to UserBot by @heyworld

from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
#from userbot.utils import admin_cmd
from userbot.events import register
from userbot import bot, CMD_HELP
import glob
import os
try:
 import instantmusic , subprocess
except:
 os.system("pip install instantmusic")



os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s "+name)


@register(outgoing=True, pattern="^.song(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.edit("🚛Loading...")
    bruh(str(cmd))
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("`sending song...`")
    await bot.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)

# Copyright (C) 2020 azrim.
# All rights reserved.
"""
   Spotify Music Downloader for your userbot
"""
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.smd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("🚛Loading...")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("Downloading **music** taking some **times**,  `Stay Tuned...`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              await bot.send_message(chat, link)
              respond = await response
          except YouBlockedUserError:
              await event.reply("```U gay bro! unblock @SpotifyMusicDownloaderBot and try again...```")
              return
          await event.delete()
          await bot.forward_messages(event.chat_id, respond.message)

CMD_HELP.update({
        "song":
        ">`.song` <songname>"
        "\nUsage: For searching songs.\n"
        ">`.smd` <song tittle>"
        "\nUsage: Download music from Spotify\n"
    })

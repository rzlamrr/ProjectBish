# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
#
import os
import lyricsgenius
import random

from userbot.events import register
from userbot import (CMD_HELP, LOGS, GENIUS, lastfm, LASTFM_USERNAME)
from pylast import User

GApi = GENIUS
genius = lyricsgenius.Genius(GApi)


@register(outgoing=True, pattern="^.lyrics(?: |$)(.*)")
async def lyrics(lyric):
    if r"-" in lyric.text:
        pass
    else:
        await lyric.edit("`⚠️ please use '-' as divider for <artist> and <song>`\n"
                         "eg: `Feby Putri - Halu`")
        return
    if GApi is None:
        await lyric.edit(
            "`Provide genius access token to Heroku ConfigVars...`")
    else:
        try:
            args = lyric.text.split('.lyrics')[1].split('-')
            artist = args[0].strip(' ')
            song = args[1].strip(' ')
        except Exception:
            await lyric.edit("`OOF! Please provide artist and song names`")
            return

    if len(args) < 1:
        await lyric.edit("`😐 Please provide artist and song names`")
        return

    await lyric.edit(f"🚛Loading...")

    try:
        songs = genius.search_song(song, artist)
    except TypeError:
        songs = None

    if songs is None:
        await lyric.edit(f"Song **{artist} - {song}** not found!")
        return
    if len(songs.lyrics) > 4096:
        await lyric.edit("`Lyrics is too big, view the file to see it.`")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Lyrics Search Results for {artist} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
    else:
        await lyric.edit(f"**Lyrics Search Results for** `{artist} - {song}`\n\n{songs.lyrics}")
    return


@register(outgoing=True, pattern="^.current_lyrics(?: |$)(.*)")
async def current_lyrics(lyric):
    genius = lyricsgenius.Genius(GENIUS)

    playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
    song = playing.get_title()
    artist = playing.get_artist()
    try:
        songs = genius.search_song(song, artist)
    except TypeError:
        songs = None
    if songs is None:
        await lyric.edit(f"Song **{artist} - {song}** not found!")
        return
    if len(songs.lyrics) > 4096:
        await lyric.edit("`Lyrics is too big, view the file to see it.`")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Lyrics Search Results for {artist} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
    else:
        await lyric.edit(f"**Lyrics Search Results for** `{artist} - {song}`\n\n{songs.lyrics}")


CMD_HELP.update({
    "lyrics":
    ">`.lyrics` **<artist name> - <song name>**"
    "\nUsage: Get lyrics matched artist and song."
    "\n\n>`.current_lyrics`"
    "\nUsage: Get lyrics artist and song from current lastfm scrobbling."
})

# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        query = CMD_HELP.get(args)
        if query:
            string = (
                "**Query**:\n\n"
                f"    `{args}`\n\n"
                f"**Command**:\n\n"
            )
            for cmd, usage in query.items():
                string += f">`.{cmd}`\n"
                string += f"{usage}"
        else:
            cmd, usage = None, None
            for module in CMD_HELP:
                for key, value in CMD_HELP.get(module).items():
                    if args == key:
                        usage = value
                        break
                else:
                    await event.edit(
                        "`There is no command or module`: **{args}**.")
                    return False
                if cmd is not None and usage is not None:
                    string = (
                        "**Query**:\n\n"
                        f"    >`{args}`\n\n"
                        f"**Usage**:\n\n"
                        f"{usage}"
                    )
        await event.edit(string)
    else:
        string = (
            "**Usage**:\n\n"
            "    >`.help` [module]\n\n"
            f"**Loaded Modules [{len(CMD_HELP)}]**:\n\n"
        )
        for key in CMD_HELP:
            string += (f"`{key}`    ")
        await event.edit(string)

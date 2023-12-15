#!/usr/bin/env python3
from pyrogram.handlers import MessageHandler, EditedMessageHandler
from pyrogram.filters import command
from io import BytesIO

from bot import bot, LOGGER 
from bot.helper.telegram_helper.message_utils import sendMessage, sendFile
from bot.helper.ext_utils.bot_utils import cmd_exec, new_task
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands


@new_task
async def shell(_, message):
    cmd = message.text.split(maxsplit=1)
    if len(cmd) == 1:
        await sendMessage(message, '<b>Tidak ada perintah untuk dieksekusi!</b>')
        return
    cmd = cmd[1]
    stdout, stderr, _ = await cmd_exec(cmd, shell=True)
    reply = ''
    if len(stdout) != 0:
        reply += f"<b>Stdout</b>\n<pre language='bash'>{stdout}</pre>\n"
        LOGGER.info(f"Shell - {cmd} - {stdout}")
    if len(stderr) != 0:
        reply += f"<b>Stderr</b>\n<pre language='bash'>{stderr}</pre>"
        LOGGER.error(f"Shell - {cmd} - {stderr}")
    if len(reply) > 3000:
        with BytesIO(str.encode(reply)) as out_file:
            out_file.name = "shell_output.txt"
            await sendFile(message, out_file)
    elif len(reply) != 0:
        await sendMessage(message, reply)
    else:
        await sendMessage(message, '<b>Tidak ada balasan!</b>')



bot.add_handler(
    MessageHandler(
        shell, 
        filters=command(
            BotCommands.ShellCommand
        ) & CustomFilters.owner
    )
)
bot.add_handler(
    EditedMessageHandler(
        shell, 
        filters=command(
            BotCommands.ShellCommand
        ) & CustomFilters.owner
    )
)
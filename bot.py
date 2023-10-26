from pyrogram import Client
from pyrogram import types
from pyrogram.raw import functions
from config import *
import os

class Bot(Client):
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    def __init__(self):
        super().__init__(
            "simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"{me.first_name} | @{me.username} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")

    async def stop(self, *args):
        await super().stop()
        print("Bot Restarting........")

    async def on_upload_progress(self, current, total):
        # Handle progress updates for large file uploads here
        # For example, you can log the progress or send updates to the user.

    async def upload_large_file(self, chat_id, file_path, file_name):
        try:
            result = await self.send(
                functions.messages.UploadMedia(
                    peer=await self.resolve_peer(chat_id),
                    media=types.InputMediaUploadedDocument(
                        file=await self.upload_file(file_path),
                        force_document=True,
                        attributes=[types.DocumentAttributeFilename(file_name)],
                    ),
                ),
                file_name=file_name,
            )
            return result
        except Exception as e:
            print(f"Error uploading the file: {e}")

bot = Bot()
bot.run()

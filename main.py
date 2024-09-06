from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession, CreateNewSession
import asyncio

async def main():
    client = TelegramClient("telethon.session")
asyncio.run(main())

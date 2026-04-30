# src/bridge.py
import os
import asyncio
import threading
import pyautogui
from telegram.ext import Application, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

class TelegramBridge:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.app = Application.builder().token(self.token).build()

    async def _handle_message(self, update, context):
        text = update.message.text.lower()
        
        # Simple Logic: "Open [website]"
        if "open" in text:
            url = text.replace("open", "").strip()
            import webbrowser
            webbrowser.open(f"https://{url}.com" if "." not in url else url)
            await update.message.reply_text(f"Opening {url} on your desktop, Sir.")
            
        # Add more remote commands here (Volume, Lock PC, etc.)
        elif "lock" in text:
            os.system("rundll32.exe user32.dll,LockWorkStation")
            await update.message.reply_text("Workstation secured.")

    def _start_polling(self):
        # Create a new event loop for this background thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message))
        print("[System] Mobile Gateway Active...")
        self.app.run_polling(close_loop=False)

    def launch(self):
        """Starts the Telegram bot in a separate background thread."""
        thread = threading.Thread(target=self._start_polling, daemon=True)
        thread.start()

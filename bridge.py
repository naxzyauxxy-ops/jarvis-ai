from telegram.ext import Application, MessageHandler, filters
import pyautogui

class TelegramBridge:
    def __init__(self, token):
        self.app = Application.builder().token(token).build()
    
    async def handle_message(self, update, context):
        command = update.message.text.lower()
        if "open browser" in command:
            pyautogui.press('win')
            pyautogui.write('chrome')
            pyautogui.press('enter')
            await update.message.reply_text("Browser opened on your desktop, Sir.")

    def run(self):
        self.app.add_handler(MessageHandler(filters.TEXT, self.handle_message))
        self.app.run_polling()

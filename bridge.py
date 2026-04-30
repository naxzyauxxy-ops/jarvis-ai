import telebot
import os
import webbrowser
from threading import Thread

class MobileGateway(Thread):
    def __init__(self, token):
        super().__init__(daemon=True)
        self.bot = telebot.TeleBot(token)

    def run(self):
        @self.bot.message_handler(func=lambda m: True)
        def handle_commands(message):
            cmd = message.text.lower()
            if "open browser" in cmd:
                webbrowser.open("https://google.com")
                self.bot.reply_to(message, "Desktop browser opened, Sir.")
            elif "screenshot" in cmd:
                # Logic to trigger vision.py and return analysis
                self.bot.reply_to(message, "Analyzing desktop view...")
        
        self.bot.polling()

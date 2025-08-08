import requests
import asyncio
import time
from telegram import Bot

# Telegram bot token and chat ID
BOT_TOKEN = "8008174287:AAEHjiuDmfIpCrb78idrOrIgeLDwkMI6vZI"
CHAT_ID = "903712215"

# List of URLs to check
URLS = [
    "https://www.karurcinemas.com/",
    "https://www.karurcinemas.com/movies/"
]

# Keyword to search for
KEYWORD = "Coolie"

bot = Bot(token=BOT_TOKEN)

async def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if KEYWORD.lower() in response.text.lower():
            await bot.send_message(chat_id=CHAT_ID, text=f"🎬 '{KEYWORD}' is now available!\n{url}")
            print(f"Found keyword on {url}, notification sent.")
            return True
        else:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Keyword not found on {url}.")
            return False
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False

async def main():
    while True:
        for url in URLS:
            found = await check_website(url)
            if found:
                return  # Stop if found
        await asyncio.sleep(300)  # Wait 5 minutes before checking again

if __name__ == "__main__":
    asyncio.run(main())


import os
import importlib
import logging
import signal
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.command import (
    start_command,
    help_command,
    ban_command,
    unban_command,
    info_command,
    sangmata_command
)
from config import api_id, api_hash, bot_token, owner_id

# Inisialisasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Mendapatkan path absolut dari direktori "plugins"
plugins_dir = os.path.abspath("plugins")

# Melakukan iterasi pada setiap file di direktori "plugins"
for filename in os.listdir(plugins_dir):
    # Mengecek apakah file tersebut adalah file Python (.py)
    if filename.endswith(".py"):
        # Menghilangkan ekstensi file Python (.py) untuk mendapatkan nama modul
        module_name = filename[:-3]

        # Membentuk nama package dengan menggabungkan "plugins" dan nama modul
        package_name = f"plugins.{module_name}"

        # Menambahkan pesan logging sebelum loading modul
        logging.info(f"Loading modul {module_name}")

        # Mengimpor modul dengan menggunakan importlib
        module = importlib.import_module(package_name)

        # Menambahkan modul yang diimpor ke dalam globals() agar dapat diakses di file ini
        globals()[module_name] = module

# Inisialisasi klien bot Telegram
bot = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Tambahkan handler untuk command-command
bot.add_handler(start_command)
bot.add_handler(help_command)
bot.add_handler(ban_command)
bot.add_handler(unban_command)
bot.add_handler(info_command)
bot.add_handler(sangmata_command)

# Menambahkan fungsi penanganan sinyal SIGINT (CTRL+C)
def handle_sigint(signal, frame):
    logging.info("Bot dimatikan dengan CTRL+C")
    bot.stop()

# Menangkap sinyal SIGINT (CTRL+C)
signal.signal(signal.SIGINT, handle_sigint)

# Menjalankan bot
bot.start()
logging.info("Bot telah berhasil diaktifkan.")

try:
    bot.run()
except KeyboardInterrupt:
    logging.info("Bot dimatikan dengan CTRL+C")
    bot.stop()

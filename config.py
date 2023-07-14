import os
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Konfigurasi API ID, API Hash, dan Token Bot
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

# Konfigurasi ID Pemilik Bot
owner_id = int(os.environ.get("OWNER_ID"))

# Konfigurasi ID Grup Log
log_group_id = int(os.environ.get("LOG_GROUP_ID"))

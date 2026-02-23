import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "32546882"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "81254ed5acbeb5839a3493a995994864")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8507577912:AAE8HDhJSlaumOr4ftPF6oWuaEV7D2q-OHI")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Semextract_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "1806771298"))
# ------------------X------------------------------
CREATOR_ID = int(os.environ.get("CREATOR_ID", "1806771298"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1003700223671"))


SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1806771298").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003700223671"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003700223671"))

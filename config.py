import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "222868689"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "0c9262bdjhfdshdvdshvschb7b447ffd8e38f1e4d")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Rajasthani_king_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7995790656"))
# ------------------X------------------------------
CREATOR_ID = int(os.environ.get("CREATOR_ID", "7995790656"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1003687978698"))


SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7438818824").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003687978698"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003687978698"))

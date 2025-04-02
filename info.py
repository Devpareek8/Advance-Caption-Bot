from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6914788581"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://vault.pictures/p/a8c03ae4dbac4f6f9c81cbf8a2507781")
API_ID = int(getenv("API_ID", "24942826"))
API_HASH = str(getenv("API_HASH", "e3e2f3b65ef58634139ccd27d6b7d8cb"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
FORCE_SUB = os.environ.get("FORCE_SUB", "") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://Demo23:Demo23@cluster0.fjar36c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}\nDev</b>",
    )
)

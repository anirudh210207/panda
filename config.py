import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", '27316382'))
API_HASH = getenv("API_HASH", 'a267e971b12a958177464646a7829f15')

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", '7202606996:AAFVrm8pn5vK0IDngos-etIo38hmhDnMPVw')

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Branded:Brandedking82@branded.kauagbt.mongodb.net/?retryWrites=true&w=majority")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝗦ʜᴀᴅᴏᴡ  Mɪᴋᴏ")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "8116165837"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002485728952"))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7006715434"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/LEGENDMICKEY/Pandamusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/we_the_shadows")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+NP_dopYLKWo0YTJl")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION",  None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/634e3ba7e32808c97ac88.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/634e3ba7e32808c97ac88.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

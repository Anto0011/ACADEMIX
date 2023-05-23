import pathlib
import logging
import os
from logging.config import dictConfig
from dotenv import load_dotenv
import discord

#Load variables from .env file
load_dotenv()

#Load the keys from .env file
DISCORD_API_KEY = str(os.getenv("DISCORD_API_KEY"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GUILDS_ID = discord.Object(id= int(os.getenv("GUILD")))#type: ignore

#Load database credentials
ht = str(os.getenv("ht"))
user = str(os.getenv("user"))
pwd = str(os.getenv("pwd"))
db = str(os.getenv("db"))

#Create the base directory
BASE_DIR = pathlib.Path(__file__).parent

#Import path of discord commands
CMDS_DIR = BASE_DIR / "cmds"
COGS_DIR = BASE_DIR / "cogs"
SLASHCMDS_DIR = BASE_DIR / "slashcmds"

#Logging settings
LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s - %(message)s"
        },
        "standard": {
            "format": "%(levelname)-10s - %(name)-15s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/infos.log",
            "mode": "w",
            "formatter": "verbose"
        }
    },
    "loggers": {
        "bot": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False
        }
    }
}

#Initialize logging
dictConfig(LOGGING_CONFIG)

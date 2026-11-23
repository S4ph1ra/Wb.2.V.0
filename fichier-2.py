import sys
import threading
import argparse
from websocket_client import WcsBot
from config import CONFIG
from bot_logic import FarmingStrategy

def main():
    parser = argparse.ArgumentParser(description="Wildcraft Bot - Mode Offline/Online")
    parser.add_argument("--session", type=str, help="Session Key WCSO", default=CONFIG["session_key"])
    parser.add_argument("--mode", type=str, choices=["online", "offline"], default="offline")
    args = parser.parse_args()

    bot = WcsBot(args.session, args.mode)
    bot.start()

if __name__ == "__main__":
    main()
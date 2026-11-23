from config import CONFIG
import time

class FarmingStrategy:
    @staticmethod
    def level_up():
        while True:
            if CONFIG["strategy"] == "level_up":
                print("🔥 Mode 'level_up' activé. Optimisation XP...")
                time.sleep(CONFIG["interval"])

    @staticmethod
    def resource_optimize():
        while True:
            if CONFIG["strategy"] == "resource_optimize":
                print("💰 Mode 'resource_optimize' activé. Optimisation ressources...")
                time.sleep(CONFIG["interval"])
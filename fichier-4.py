import websocket
import json
import time
from threading import Thread

class WcsBot:
    def __init__(self, session_key, mode):
        self.session_key = session_key
        self.mode = mode
        self.websocket = None
        self.running = False

    def connect(self):
        if self.mode == "online":
            self.websocket = websocket.WebSocket()
            self.websocket.connect(f"wss://wcs-server.com/ws?session={self.session_key}")
            Thread(target=self.listen, daemon=True).start()

    def listen(self):
        while self.running:
            try:
                data = self.websocket.recv()
                if "level_up" in data:
                    self._handle_level_up(json.loads(data))
                elif "resource_gained" in data:
                    self._handle_resource(json.loads(data))
            except Exception as e:
                print(f"⚠️ Erreur WebSocket: {e}")

    def _handle_level_up(self, data):
        level = data["level"]
        print(f"🎉 Niveau {level} atteint ! XP: {data['xp']}")

    def _handle_resource(self, data):
        resource = data["resource"]
        amount = data["amount"]
        print(f"🌿 {resource} (+{amount})")

    def start(self):
        self.running = True
        self.connect()
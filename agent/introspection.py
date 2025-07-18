# File: agent/introspection.py

import datetime
from .emotion_engine import EmotionEngine

class Introspection:
    def __init__(self, engine: EmotionEngine):
        self.engine = engine

    def log_rationale(self, trigger: str) -> dict:
        """Generate a human-readable rationale for the last state change."""
        prev = self.engine.history[-2] if len(self.engine.history) > 1 else None
        curr = self.engine.history[-1]
        return {
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "trigger": trigger,
            "from_state": prev.name if prev else None,
            "to_state": curr.name,
            "reasoning": f"Transitioned due to input '{trigger}'."
        }

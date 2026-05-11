from typing import List, Dict
from datetime import datetime


class ResearchMemory:
    def __init__(self):
        self.past_research : List[Dict] = []

    def add_research(self, topic: str, report: str, timestamp: datetime):

        self.past_research.append({
            "topic": topic,
            "report": report,
            "timestamp": timestamp
        })

    
    def get_relvant_context(self, current_topic: str) -> str:
        relevant = [r for r in self.past_research
            if self._is_relevant(r['topic'], current_topic)]

        return "\n".join([r['report'] for r in relevant])
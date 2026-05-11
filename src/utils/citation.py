from typing import List, Dict
import re


class CitationManager:
    def __init__(self):
        self.citations: List[Dict] = []

    def add_citation(self, text: str, source: Dict):
        citation_id = len(self.citations) + 1
        self.citations.append({
            "id": citation_id,
            "title": source.get("title"),
            "url": source.get("url"),
            "date": source.get("published_date"),
            "snippet": text
        })
        return f"{text} [{citation_id}]"

    def format_bibliography(self) -> str:
        bibliography = "\n## منابع\n\n"
        for cite in self.citations:
            bibliography += f"[{cite['id']}] {cite['title']}\n"
            bibliography += f"      {cite['url']}\n"
            bibliography += f"      تاریخ دسترسی: {cite['date']}\n\n"
        return bibliography
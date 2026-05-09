from tavily import TavilyClient
from typing import List, Dict
import os


class SearchAgent:

    def __init__(self):
        self.client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def search(self, query: str, max_results: int = 5) -> List[Dict]:
        try:
            response = self.client.search(
                query=query,
                max_results=max_results,
                search_depth="advanced"
            )

            results = []
            for result in response.get('results', []):
                results.append({
                    'title': result.get('title', ''),
                    'url': result.get('url', ''),
                    'content': result.get('content', ''),
                    'score': result.get('score', '')
                })

            return results
        except Exception as e:
            print(f"search error: {e}")
            return []

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from typing import List, Dict


class SummarizerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0.3)

    def summarize(self, query: str, search_results: List[Dict]) -> str:
        context = "\n\n".join([
            f"""
            Title: {r['title']}
            Content: {r['content']}
            Source: {r['url']}
            """

            for r in search_results
        ])

        messages = [
            SystemMessage(
                content="""
You are a research summarizer.
Create a concise but informative summary from the search results.
Include key findings, trends, and important insights.
"""
            ),
            HumanMessage(
                content=f"""
Research Query:
{query}

Search Results:
{context}

Generate a summary:
"""
            )
        ]

        response = self.llm.invoke(messages)
        return response.content

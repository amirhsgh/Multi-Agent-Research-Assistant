from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


class CriticAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)

    def critique(self, report: str) -> str:
        messages = [
            SystemMessage(
                content="""
You are a research critic.

Evaluate the report for:
- completeness
- clarity
- factual consistency
- missing important points

Provide concise feedback and improvements.
"""
            ),
            HumanMessage(content=report)
        ]

        response = self.llm.invoke(messages)
        return response.content

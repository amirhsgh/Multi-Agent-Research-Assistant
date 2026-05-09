from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from typing import List


class PlannerAgent:
    def __init__(self, model_name: str = "gpt-4.1-nano"):
        self.llm = ChatOpenAI(model=model_name, temperature=0.7)


    def create_plan(self, topic: str) -> List[str]:
        system_prompt = """You are a research planner. Break down the reserch topic into 3-5 specific, searchable subtasks.
        Each subtask should be a clear question or search query.

        Example:
        Topic: "Impact of AI on healthcare"
        subtasks:
        1. Current AI application in medical diagnosis
        2. AI in drug discovery and development
        3. Challenges and ethical concerns of AI in helathcare
        4. Future predictions for AI in healthcare industry
        """

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Research topic: {topic}\n\nCreate a research plan:")
        ]

        response = self.llm.invoke(messages)

        lines = response.content.strip().split('\n')
        subtasks = [lines.strip('0123456789. ') for line in lines if line.strip() and line[0].isdigit()]

        return subtasks

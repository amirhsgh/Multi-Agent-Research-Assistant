from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from typing import Dict


class MultiLLMRouter:
    """
    Routing tasks between multiple LLMs
    based on cost/speed/capability
    """

    def __init__(self):

        self.fast_llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0
        )

        self.smart_llm = ChatOpenAI(
            model="gpt-5",
            temperature=0
        )

        self.creative_llm = ChatAnthropic(
            model="claude-sonnet-4",
            temperature=0.7
        )

    def route(
        self,
        task_type: str
    ):
        """انتخاب مدل مناسب"""

        routing_table = {
            "search_summary": self.fast_llm,
            "classification": self.fast_llm,

            "reasoning": self.smart_llm,
            "planning": self.smart_llm,
            "critique": self.smart_llm,

            "writing": self.creative_llm,
            "report_generation": self.creative_llm
        }

        return routing_table.get(
            task_type,
            self.fast_llm
        )

    def invoke(
        self,
        task_type: str,
        prompt: str
    ) -> str:
        """اجرای task روی مدل مناسب"""

        llm = self.route(task_type)

        response = llm.invoke(prompt)

        return response.content
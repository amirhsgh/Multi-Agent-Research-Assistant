from langgraph.graph import StateGraph, END
from typing import TypedDict, List
import asyncio

from src.agents.parallel_searcher import ParallelSearchAgent
from src.routing.llm_router import MultiLLMRouter
from src.memory.vector_memory import VectorMemory
from src.human.approval import HumanApproval


class ResearchState(TypedDict):
    topic: str
    plan: List[str]
    search_results: List[dict]
    final_report: str
    approved: bool


class AdvancedResearchWorkflow:

    def __init__(self):

        self.router = MultiLLMRouter()
        self.memory = VectorMemory()
        self.approval = HumanApproval()

    async def parallel_search_node(
        self,
        state: ResearchState
    ):

        search_agent = ParallelSearchAgent(
            tavily_api_key="YOUR_API_KEY"
        )

        results = await search_agent.search_parallel(
            state["plan"]
        )

        return {
            "search_results": results
        }

    def approval_node(
        self,
        state: ResearchState
    ):

        summary = f"""
        Topic: {state['topic']}

        Planned Searches:
        {chr(10).join(state['plan'])}
        """

        approved = self.approval.request_approval(
            step_name="Research Execution",
            content=summary
        )

        return {
            "approved": approved
        }

    def report_node(
        self,
        state: ResearchState
    ):

        context = self.memory.get_context_for_topic(
            state["topic"]
        )

        prompt = f"""
        Previous Context:
        {context}

        Current Research:
        {state['search_results']}

        Generate professional report.
        """

        report = self.router.invoke(
            task_type="report_generation",
            prompt=prompt
        )

        self.memory.store_research(
            topic=state["topic"],
            content=report
        )

        return {
            "final_report": report
        }

    def build(self):

        graph = StateGraph(ResearchState)

        graph.add_node(
            "approval",
            self.approval_node
        )

        graph.add_node(
            "report",
            self.report_node
        )

        graph.set_entry_point("approval")

        graph.add_edge(
            "approval",
            "report"
        )

        graph.add_edge(
            "report",
            END
        )

        return graph.compile()
from typing import TypedDict, Annotated, List
from langgraph.graph import add_messages
from langchain_core.messages import BaseMessage


class ResearchState(TypedDict):
    messages : Annotated[List[BaseMessage], add_messages]
    research_topic : str
    research_plan : List[str]
    search_results : List[dict]
    summaries : list[str]
    final_report : str
    current_step : int
    max_iterations : int

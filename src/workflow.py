from langgraph.graph import StateGraph, END
from src.state import ResearchState

from src.agents.planner import PlannerAgent
from src.agents.searcher import SearchAgent
from src.agents.summarizer import SummarizerAgent
from src.agents.critic import CriticAgent

planner = PlannerAgent()
searcher = SearchAgent()
summarizer = SummarizerAgent()
critic = CriticAgent()


def planner_node(state: ResearchState):
    topic = state["research_topic"]

    plan = planner.create_plan(topic)

    return {
        "research_plan": plan,
        "current_step": 0
    }

def search_node(state: ResearchState):
    step = state["current_step"]
    plan = state["research_plan"]

    query = plan[step]

    results = searcher.search(query)

    all_results = state.get("search_results", [])

    all_results.append({
        "query": query,
        "results": results
    })

    return {
        "search_results": all_results
    }


def summarize_node(state: ResearchState):
    step = state["current_step"]

    current_data = state["search_results"][step]

    summary = summarizer.summarize(
        current_data["query"],
        current_data["results"]
    )

    summaries = state.get("summaries", [])
    summaries.append(summary)

    return {
        "summaries": summaries
    }


def should_continue(state: ResearchState):
    step = state["current_step"]
    total = len(state["research_plan"])

    if step + 1 >= total:
        return "finalize"

    return "continue"


def increment_step(state: ResearchState):
    return {
        "current_step": state["current_step"] + 1
    }


def finalize_node(state: ResearchState):
    report = "\n\n".join(state["summaries"])

    feedback = critic.critique(report)

    final_report = f"""
# Final Research Report

{report}

---

# Critic Feedback

{feedback}
"""

    return {
        "final_report": final_report
    }


builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("search", search_node)
builder.add_node("summarize", summarize_node)
builder.add_node("increment", increment_step)
builder.add_node("finalize", finalize_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "search")
builder.add_edge("search", "summarize")


builder.add_conditional_edges(
    "summarize",
    should_continue,
    {
        "continue": "increment",
        "finalize": "finalize"
    }
)


builder.add_edge("increment", "search")
builder.add_edge("finalize", END)

graph = builder.compile()
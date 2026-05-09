from dotenv import load_dotenv
from src.workflow import graph

load_dotenv()

topic = input("Enter research topic: ")

initial_state = {
    "research_topic": topic,
    "research_plan": [],
    "search_results": [],
    "summaries": [],
    "final_report": "",
    "current_step": 0,
    "max_iterations": 5,
    "messages": []
}

result = grapg.invoke(initial_state)

print("\n")
print(result["final_report"])


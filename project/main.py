from langgraph.graph import StateGraph

from models.state import GraphState

from agents.intake_agent import intake_agent
from agents.diagnostic_agent import diagnostic_agent
from agents.retrieval_agent import retrieval_agent
from agents.reasoning_agent import reasoning_agent


builder = StateGraph(GraphState)
builder.add_node("intake", intake_agent)
builder.add_node("diagnostic", diagnostic_agent)
builder.add_node("retrieval", retrieval_agent)
builder.add_node("reasoning", reasoning_agent)
builder.set_entry_point("intake")

builder.add_edge(
    "intake",
    "diagnostic"
)
builder.add_edge(
    "diagnostic",
    "retrieval"
)
builder.add_edge(
    "retrieval",
    "reasoning"
)
graph = builder.compile()

result = graph.invoke(
    {
        "user_input":
        """
        We are a SME retail company.

        We use Excel and Power BI.

        Reports are inconsistent.

        We do not have a data catalog.
        """
    }
)
print(result)

print("RETRIEVED KNOWLEDGE")

for chunk in result[
    "retrieved_knowledge"
]:

    print()

    print("-" * 80)

    print(chunk[:500])

    print()

print("=" * 80)
print("DIAGNOSIS")
print("=" * 80)

print(
    result["diagnosis"]
)
from langgraph.graph import StateGraph

from models.state import GraphState

from agents.intake_agent import intake_agent
from agents.diagnostic_agent import diagnostic_agent
from agents.technology_assessment_agent import technology_assessment_agent
from agents.retrieval_agent import retrieval_agent
from agents.reasoning_agent import reasoning_agent
from agents.strategy_agent import strategy_agent
from agents.dss_agent import dss_agent


builder = StateGraph(GraphState)
builder.add_node("intake", intake_agent)
builder.add_node("diagnostic", diagnostic_agent)
builder.add_node("technology_assessment", technology_assessment_agent)
builder.add_node("retrieval", retrieval_agent)
builder.add_node("reasoning", reasoning_agent)
builder.add_node("strategy", strategy_agent)
builder.add_node("dss", dss_agent)
builder.set_entry_point("intake")

builder.add_edge(
    "intake",
    "technology_assessment"
)
builder.add_edge(
    "technology_assessment",
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
builder.add_edge(
    "reasoning",
    "strategy"
)
builder.add_edge(
    "strategy",
    "dss"
)
graph = builder.compile()

result = graph.invoke(
    {
        "user_input":
        """
        We are a medium-sized retail company.

        We use Excel, SQL Server and Power BI.

        Different departments produce conflicting reports.

        Customer information is duplicated across systems.

        Data ownership is unclear.

        We do not have a data catalog.

        Business definitions vary among departments.

        Data quality problems are recurrent and require manual corrections.

        We lack formal governance processes.
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

print(result["technology_profile"])
print(result["strategy"])
print(result["final_response"])
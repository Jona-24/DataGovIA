from langgraph.graph import (
    StateGraph,
    START,
    END
)

from models.state import GraphState

from agents.intake_agent import intake_agent
from agents.technology_assessment_agent import technology_assessment_agent
from agents.diagnostic_agent import diagnostic_agent
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
    START,
    "intake"
)
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
builder.add_edge(
    "dss",
    END
)
graph = builder.compile()

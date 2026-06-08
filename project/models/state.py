from typing import TypedDict


class GraphState(TypedDict):

    user_input: str

    organization_context: dict

    capability_gaps: list

    retrieved_knowledge: list

    recommendations: list

    diagnosis: dict
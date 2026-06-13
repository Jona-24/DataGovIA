from typing import TypedDict


class GraphState(TypedDict):

    user_input: str

    organization_context: dict

    technology_profile: dict

    capability_gaps: list

    retrieved_knowledge: list

    recommendations: list

    diagnosis: dict

    strategy: dict

    final_response: str
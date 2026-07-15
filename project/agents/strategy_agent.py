from llm.provider import llm
import json
import re


def strategy_agent(state):

    print("Running Strategy Agent")

    diagnosis = state.diagnosis

    technology_profile = state.technology_profile

    knowledge = state.retrieved_knowledge

    prompt = f"""
    # Role

    You are a senior Data Governance consultant responsible for defining a feasible implementation strategy.

    Your responsibility is to translate the diagnostic assessment into practical and realistic implementation actions that align with the organization's technological capabilities.

    Do not perform a new diagnosis or introduce capability gaps that are not present in the provided diagnosis.

    # Task

    Produce a feasible implementation strategy based exclusively on the diagnosis, technology profile, and retrieved knowledge.

    # Context

    ## Diagnosis

    {diagnosis}

    ## Technology Profile

    {technology_profile}

    ## Relevant Knowledge

    {knowledge}

    # Reasoning Constraints

    - Use only the provided diagnosis, technology profile, and retrieved knowledge.
    - Ensure all recommendations are technically and economically feasible for the organization's technology profile.
    - Consider technology maturity, budget level, current tools, deployment preferences, and implementation complexity tolerance.
    - Do not recommend technologies or solutions that are incompatible with the organization's constraints.
    - Do not introduce new capability gaps or perform additional diagnosis.
    - Keep recommendations consistent with the retrieved knowledge.

    # Output

    Return ONLY valid JSON.

    Do not include explanations, markdown, code, or additional text.

    The JSON must follow exactly this schema:

    {{
        "recommendations": [],
        "quick_wins": [],
        "strategic_actions": []
    }}
    """

    response = llm.invoke(
        prompt
    )

    print(response.content)

    json_match = re.search(
        r"\{.*\}",
        response.content,
        re.DOTALL
    )

    parsed = json.loads(
        json_match.group()
    )

    state.strategy = parsed

    return state
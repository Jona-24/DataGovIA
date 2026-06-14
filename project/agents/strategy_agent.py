from llm.provider import llm
import json
import re


def strategy_agent(state):

    print("Running Strategy Agent")

    diagnosis = state.diagnosis

    technology_profile = state.technology_profile

    knowledge = state.retrieved_knowledge

    prompt = f"""
    You are a senior Data Governance consultant.

    Diagnosis:

    {diagnosis}

    Technology Profile:

    {technology_profile}

    Relevant Knowledge:

    {knowledge}

    Produce a feasible implementation strategy.

    Return ONLY valid JSON.

    Schema:

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
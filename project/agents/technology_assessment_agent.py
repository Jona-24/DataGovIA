from llm.provider import llm
import json
import re


def technology_assessment_agent(state):

    print("Running Technology Assessment Agent")

    context = state["organization_context"]

    prompt = f"""
    You are a senior Data Governance and Data Architecture consultant.

    Analyze the organization context.

    Infer missing information when reasonable.

    Use your professional judgement.

    Context:

    {context}

    Rules:

    - organization_size must be one of:
        SME
        Medium
        Enterprise

    - technical_maturity must be one of:
        Low
        Medium
        High

    - budget_level must be one of:
        Low
        Medium
        High

    - preferred_deployment must be one of:
        Cloud
        Hybrid
        On Premise

    - implementation_complexity_tolerance must be one of:
        Low
        Medium
        High

    Return ONLY valid JSON.

    Schema:

    {{
        "organization_size":"",
        "technical_maturity":"",
        "budget_level":"",
        "preferred_deployment":"",
        "current_tools":[],
        "implementation_complexity_tolerance":""
    }}
    """

    response = llm.invoke(prompt)

    json_match = re.search(
        r"\{.*\}",
        response.content,
        re.DOTALL
    )

    parsed = json.loads(
        json_match.group()
    )

    state["technology_profile"] = parsed

    return state
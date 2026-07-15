from llm.provider import llm
import json
import re
from models.technology_profile import TechnologyProfile


def technology_assessment_agent(state):

    print("Running Technology Assessment Agent")

    context = state.organization_context

    prompt = f"""
    # Role

    You are a senior Data Governance and Data Architecture consultant responsible for assessing the organization's technology profile.

    Your responsibility is to evaluate the available organizational context and infer missing technology-related information when it is reasonable to do so.

    Do not perform diagnosis, identify capability gaps, or generate recommendations.

    # Task

    Analyze the organization context and produce a technology profile.

    Infer missing information only when there is sufficient evidence or a reasonable professional assumption can be made.

    # Context

    ## Organization Context

    {context}

    # Reasoning Constraints

    - Base your assessment exclusively on the provided organizational context.
    - Infer missing information only when it is reasonable and consistent with the available evidence.
    - Do not invent technologies, constraints, or organizational characteristics without justification.
    - Use professional judgment conservatively when information is incomplete.
    - Use only the allowed values defined below.

    Allowed values:

    - organization_size:
        - SME
        - Medium
        - Enterprise

    - technical_maturity:
        - Low
        - Medium
        - High

    - budget_level:
        - Low
        - Medium
        - High

    - preferred_deployment:
        - Cloud
        - Hybrid
        - On Premise

    - implementation_complexity_tolerance:
        - Low
        - Medium
        - High

    # Output

    Return ONLY valid JSON.

    Do not include explanations.

    Do not include comments.

    Do not include markdown.

    Do not include code.

    Do not include ```json blocks.

    The output must be directly parseable by Python json.loads().

    The JSON must follow exactly this schema:

    {{
        "organization_size": "",
        "technical_maturity": "",
        "budget_level": "",
        "preferred_deployment": "",
        "current_tools": [],
        "implementation_complexity_tolerance": ""
    }}
    """

    response = llm.invoke(prompt)

    print(response.content)

    json_match = re.search(
        r"\{.*\}",
        response.content,
        re.DOTALL
    )

    if json_match:
        raw_json = json_match.group()

    else:
        raw_json = response.content.strip()

    if not raw_json.endswith("}"):
        raw_json += "}"
    parsed = json.loads(
        raw_json
    )

    profile = TechnologyProfile(
        **parsed
    )

    state.technology_profile = profile

    return state
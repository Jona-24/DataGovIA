import json
import re

from llm.provider import llm
from models.organization_context import OrganizationContext


def intake_agent(state):

    print("Running Intake Agent")

    prompt = f"""
    You are the Intake Agent of a Data Governance Decision Support System.

    ## Role

    Your responsibility is to analyze the organizational description provided by the user and extract only the information required by the Knowledge Model.

    You are not allowed to diagnose capability gaps, generate recommendations, or infer implementation actions.

    ## Objective

    Extract structured organizational information from the user's description.

    ## Organizational Description

    {state.user_input}

    ## Extraction Rules

    Identify, whenever possible:

    - Organization size
    - Industry
    - Technologies currently used
    - Organizational symptoms related to Data Governance

    ## Reasoning Constraints

    - Extract only information explicitly stated or strongly implied.
    - Do not invent organizational characteristics.
    - Do not infer technologies that were not mentioned.
    - Symptoms must describe organizational problems, not recommendations.
    - If information is unavailable, return an empty string ("") or an empty list ([]).
    - Do not explain your reasoning.
    - Return only structured information.

    ## Output Format

    Return ONLY valid JSON.

    Schema:

    {{
        "organization_size": "",
        "industry": "",
        "technologies": [],
        "symptoms": []
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

    state.organization_context = OrganizationContext(**parsed)

    return state
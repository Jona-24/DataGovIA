import json
import re

from llm.provider import llm
from models.organization_context import OrganizationContext


def intake_agent(state):

    print("Running Intake Agent")

    prompt = f"""
    Analyze the organization description.

    Return ONLY valid JSON.

    Schema:

    {{
      "organization_size": "",
      "industry": "",
      "technologies": [],
      "symptoms": []
    }}

    Description:

    {state.user_input}
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
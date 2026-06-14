from llm.provider import llm

import json
import re


def diagnostic_agent(state):

    print("Running Diagnostic Agent")

    symptoms = state.organization_context.symptoms
    
    prompt = f"""
    You are a Data Governance expert.

    Based on the following symptoms:

    {symptoms}

    Identify the most likely capability gaps.

    You may only choose from:

    - Data Governance
    - Metadata Management
    - Data Quality
    - Data Architecture
    - Master Data Management
    - Data Security
    - Data Integration

    Return ONLY valid JSON.

    Schema:

    {{
      "capability_gaps": []
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

    state.capability_gaps = parsed[
        "capability_gaps"
    ]

    return state
from llm.provider import llm

import json
import re


def diagnostic_agent(state):

    print("Running Diagnostic Agent")

    symptoms = state.organization_context.symptoms
        
    prompt = f"""
    You are a specialized Data Governance Diagnosis Agent.

    ## Role

    Your sole responsibility is to analyze organizational symptoms and identify the Data Governance capability gaps that most likely explain them.

    You do not recommend solutions, technologies, implementation plans, or priorities. Your task ends after identifying the capability gaps.

    ## Objective

    Analyze the symptoms provided and determine which Data Governance capabilities are affected.

    Base your reasoning exclusively on the symptoms received.

    ## Organizational Symptoms

    {symptoms}

    ## Available Capabilities

    You may ONLY select capability gaps from the following list:

    - Data Governance
    - Metadata Management
    - Data Quality
    - Data Architecture
    - Master Data Management
    - Data Security
    - Data Integration

    Do not invent new capabilities.

    ## Reasoning Constraints

    - Base your diagnosis only on the information provided.
    - Do not assume missing organizational information.
    - Do not infer capabilities without sufficient evidence.
    - If multiple symptoms support the same capability, identify it only once.
    - If the evidence is insufficient, return an empty list.
    - Do not generate recommendations or implementation actions.
    - Do not explain your reasoning.

    ## Output Format

    Return ONLY valid JSON.

    Do not include explanations.

    Do not include markdown.

    Do not include code.

    Do not include Python.

    Your response must begin with '{' and end with '}'.

    You are not writing source code.

    You are returning structured JSON only.

    Schema:

    {{
        "capability_gaps": []
    }}
    """
    response = llm.invoke(prompt)

    print(response.content)

    response_text = response.content.strip()

    if response_text.startswith("```"):

        response_text = (
            response_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

    parsed = json.loads(response_text)

    if isinstance(parsed, list):

        parsed = {
            "capability_gaps": parsed
        }

    state.capability_gaps = parsed[
        "capability_gaps"
    ]

    return state
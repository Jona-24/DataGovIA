from llm.provider import llm
import json
import re
from models.diagnosis import Diagnosis

def reasoning_agent(state):

    print("Running Reasoning Agent")

    context = state.organization_context

    gaps = state.capability_gaps
    
    knowledge = state.retrieved_knowledge

    prompt = f"""
    # Role

    You are a senior Data Governance consultant responsible for diagnosing organizational Data Governance capability gaps.

    Your responsibility is to analyze the identified capability gaps using the available organizational context and retrieved knowledge.

    Do not generate implementation strategies, recommendations, or action plans. Focus exclusively on the diagnostic assessment.

    # Task

    Produce a diagnosis based exclusively on the information provided.

    # Context

    ## Organization Context

    {context}

    ## Capability Gaps

    {gaps}

    ## Relevant Knowledge

    {knowledge}

    # Reasoning Constraints

    - Use only the provided organization context, capability gaps, and retrieved knowledge.
    - Do not invent facts or infer information that is not explicitly supported.
    - Do not introduce new capability gaps.
    - Do not generate recommendations or implementation strategies.
    - Keep the diagnosis consistent with the provided evidence.
    - If a capability gap is identified, represent it as a JSON object following the required schema.
    - Use the knowledge provided to assign appropriate gap identifiers and severity levels when supported.

    # Output

    Return ONLY valid JSON.

    Do not include explanations.

    Do not include markdown.

    Do not include code.

    Do not include ```json blocks.

    The output must be directly parseable by Python json.loads().

    The JSON must follow exactly this schema:

    {{
        "executive_summary": "",
        "identified_gaps": [
            {{
                "gap_id": "",
                "description": "",
                "severity": ""
            }}
        ],
        "business_impacts": [],
        "priority_level": "",
        "confidence": ""
    }}
    """

    response = llm.invoke(prompt)

    json_match = re.search(
        r"\{.*\}",
        response.content,
        re.DOTALL
    )
    print(response.content)
    
    parsed = json.loads(
        json_match.group()
    )
    for gap in parsed["identified_gaps"]:
        if "pattern_id" in gap:
            gap["gap_id"] = gap.pop(
                "pattern_id"
            )
        if "diagnosis" in gap:
            gap["description"] = gap.pop(
                "diagnosis"
            )

    diagnosis = Diagnosis(
        **parsed
    )


    state.diagnosis = parsed

    return state
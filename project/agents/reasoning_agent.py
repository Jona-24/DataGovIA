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
    You are a senior Data Governance consultant.

    Organization Context:

    {context}

    Capability Gaps:

    {gaps}

    Relevant Knowledge:

    {knowledge}

    Produce a diagnosis.

    Return ONLY valid JSON.

    Schema:

    {{
        "executive_summary":"",
        "identified_gaps":[],
        "business_impacts":[],
        "priority_level":"",
        "confidence":""
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
from llm.provider import llm
from models.dss_report import DSSReport


def dss_agent(state):

    print("Running DSS Agent")

    organization_context = state.organization_context

    technology_profile = state.technology_profile

    diagnosis = state.diagnosis

    strategy = state.strategy

    prompt = f"""
    You are an expert Data Governance consultant.

    Organization Context:

    {organization_context}

    Technology Profile:

    {technology_profile}

    Diagnosis:

    {diagnosis}

    Strategy:

    {strategy}

    Generate a professional report.

    Include:

    1. Executive Summary

    2. Main Findings

    3. Business Impact

    4. Recommendations

    5. Quick Wins

    6. Strategic Actions

    7. Impacted Business Metrics

    Return markdown.
    """

    response = llm.invoke(
        prompt
    )

    state.final_response = DSSReport(report=response.content)

    return state
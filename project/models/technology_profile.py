from pydantic import BaseModel


class TechnologyProfile(
    BaseModel
):

    organization_size: str

    technical_maturity: str

    budget_level: str

    preferred_deployment: str

    current_tools: list[str]

    implementation_complexity_tolerance: str
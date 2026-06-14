from pydantic import BaseModel


class OrganizationContext(
    BaseModel
):

    organization_size: str

    industry: str

    technologies: list[str]

    symptoms: list[str]
from pydantic import BaseModel


class IntakeResult(BaseModel):

    organization_size: str

    industry: str

    technologies: list[str]

    symptoms: list[str]
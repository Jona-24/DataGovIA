from pydantic import BaseModel
from models.capability_gap import CapabilityGap


class Diagnosis(BaseModel):

    executive_summary: str

    identified_gaps: list[CapabilityGap]

    business_impacts: list[str]

    priority_level: str

    confidence: str
from pydantic import BaseModel, Field
from typing import Optional

from models.organization_context import OrganizationContext
from models.technology_profile import TechnologyProfile
from models.diagnosis import Diagnosis
from models.strategy import Strategy
from models.dss_report import DSSReport


class GraphState(
    BaseModel
):

    user_input: str

    organization_context: OrganizationContext | None = None

    capability_gaps: list[str] = Field(
        default_factory=list
    )

    retrieved_knowledge: list[str] = Field(
        default_factory=list
    )

    technology_profile: TechnologyProfile | None = None

    diagnosis: Diagnosis | None = None

    strategy: Strategy | None = None

    final_response: DSSReport | None = None
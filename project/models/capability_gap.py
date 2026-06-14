from pydantic import BaseModel
from typing import Optional

class CapabilityGap(
    BaseModel
):

    gap_id: str

    description: str

    severity: Optional[str] = None
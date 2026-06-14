from typing import Optional
from pydantic import BaseModel


class Recommendation(
    BaseModel
):

    id: str

    description: str

    priority: Optional[str] = None

    effort: Optional[str] = None

    expected_benefit: Optional[str] = None
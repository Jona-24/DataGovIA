from pydantic import BaseModel
from models.recommendation import Recommendation
from models.strategic_action import StrategicAction


class Strategy(
    BaseModel
):

    recommendations: list[Recommendation]

    quick_wins: list[str]

    strategic_actions: list[StrategicAction]
from pydantic import BaseModel
from models.recommendation import Recommendation
from models.strategic_action import StrategicAction


class Strategy(BaseModel):

    recommendations: list[dict] = []

    quick_wins: list[dict] = []

    strategic_actions: list[dict] = []
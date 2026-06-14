from pydantic import BaseModel


class StrategicAction(
    BaseModel
):

    action: str

    priority: str

    description: str
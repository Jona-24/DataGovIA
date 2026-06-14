from pydantic import BaseModel


class DSSReport(
    BaseModel
):

    report: str
import json
from pathlib import Path
from pydantic import BaseModel
from pydantic import TypeAdapter
from models.state import GraphState


CASE_PATH = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
    / "cases"
    / "current_case.json"
)

CASE_PATH.parent.mkdir(
    exist_ok=True
)

def save_case(state):

    data = TypeAdapter(
        dict
    ).dump_python(
        state
    )

    with open(
        CASE_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )
    print()
    print("Saving case to:")
    print(CASE_PATH)
    print()

def load_case():

    print("Loading case...")
    print(CASE_PATH)
    print(CASE_PATH.exists())

    if not CASE_PATH.exists():
        return None

    with open(
        CASE_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    print(data)

    return data
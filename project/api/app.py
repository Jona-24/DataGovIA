from fastapi import FastAPI
from pydantic import BaseModel
from graph import graph
from utils.case_manager import load_case



app = FastAPI()

@app.get("/")
def root():

    return {
        "message": "Data Governance DSS API"
    }

class AnalysisRequest(
    BaseModel
):

    organization_description: str


@app.post(
    "/analyze"
)
def analyze(
        request: AnalysisRequest
):

    result = graph.invoke(
        {
            "user_input":
            request.organization_description
        }
    )

    return result

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

@app.get("/current_case")
def current_case():

    return load_case()
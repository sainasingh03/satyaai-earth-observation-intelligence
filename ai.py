from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import Field

from app.services.query_planner import QueryPlanner


router = APIRouter(
    prefix="/api/ai",
    tags=["AI"],
)


class AskEarthRequest(BaseModel):

    query: str = Field(
        min_length=3,
        max_length=1000,
    )


@router.post("/ask-earth")
def ask_earth(
    request: AskEarthRequest,
):

    try:

        planner = QueryPlanner()

        plan = planner.plan(
            request.query
        )

        return {
            "query": request.query,
            "plan": plan,
            "model": planner.llm.model,
            "mode": "MODEL-POWERED",
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error),
        )
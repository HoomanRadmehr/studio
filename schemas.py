from pydantic import BaseModel
from typing import Dict,TypedDict

class BusinessData(BaseModel):
    today: Dict[str, float | int]
    yesterday: Dict[str, float | int]


class AgentOutput(BaseModel):
    message: str


class StateSchema(TypedDict):
    business_data: BusinessData
    analysis: dict
    output: AgentOutput
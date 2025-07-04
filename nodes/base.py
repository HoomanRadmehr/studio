from pydantic import BaseModel
from typing import Dict, List


class BusinessDay(BaseModel):
    revenue: float
    cost: float
    number_of_customers: int


class BusinessData(BaseModel):
    today: BusinessDay
    yesterday: BusinessDay


class ProcessedMetrics(BaseModel):
    profit_status: str
    today_profit: float
    revenue_change_pct: float
    cost_change_pct: float
    today_cac: float
    cac_change_pct: float


class AgentOutput(BaseModel):
    profit_status: str
    alerts: List[str]
    recommendations: List[str]


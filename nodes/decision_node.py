from schemas import AgentOutput

def make_decision(analysis):
    if analysis["cac_ratio"] < 0.01:
        return AgentOutput(message="Warning: CAC too high compared to new customer acquisition.")
    elif analysis["revenue_growth"] > 0 and analysis["churn_improvement"] > 0:
        return AgentOutput(message="Business performance improving.")
    else:
        return AgentOutput(message="Performance needs improvement.")
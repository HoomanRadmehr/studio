def analyze_business_data(business_data):
    today = business_data.today
    yesterday = business_data.yesterday

    revenue_growth = today["revenue"] - yesterday["revenue"]
    cost_change = today["cost"] - yesterday["cost"]
    churn_change = yesterday["churned_customers"] - today["churned_customers"]
    cac_ratio = today["new_customers"] / today["cost"] if today["cost"] > 0 else 0

    return {
        "revenue_growth": revenue_growth,
        "cost_change": cost_change,
        "churn_improvement": churn_change,
        "cac_ratio": cac_ratio,
    }
from graph import business_graph

input_data = {
    "business_data": {
        "today": {
            "profit": 1000,
            "growth": 5,
            "churned_customers": 2,
            "revenue": 12000,
            "cost": 8000,
            "new_customers": 15
        },
        "yesterday": {
            "profit": 800,
            "growth": 3,
            "churned_customers": 1,
            "revenue": 11000,
            "cost": 7500,
            "new_customers": 10
        }
    }
}

if __name__ == "__main__":
    agent = business_graph
    result = agent.invoke(input_data)

    print("=== Agent Output ===")
    print(result["output"].model_dump_json(indent=2))

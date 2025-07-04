# Business AI Agent

This project is an AI-powered business data analyzer built using LangGraph. It processes business metrics such as profit, growth, churned customers, revenue, and costs to generate insights and alerts.

## Features

- Analyze daily business data (profit, growth, churn rate, revenue, costs, etc.)
- Generate warnings and alerts based on business performance
- Designed to be extensible for various business analytics use cases

## Usage

The agent consumes business data in the following format:

```json
{
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

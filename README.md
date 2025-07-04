# 📊 Business AI Agent

This project implements a basic business intelligence agent using [LangGraph](https://github.com/langchain-ai/langgraph), designed to analyze key business metrics and provide actionable feedback. It supports modular logic for analyzing profit, churn, growth, and other signals.

---

## 🚀 Features

- Analyzes business KPIs like profit, churn, revenue growth, and CAC.
- Provides feedback and alerts based on performance trends.
- Structured using LangGraph's graph-based workflow.
- Easily testable and extendable.

---

## 🧪 Test Coverage

The project includes unit tests that cover different business scenarios:

- 📈 Positive profit and growth
- ⚠️ Negative profit and churn increase
- 🚨 Alert on CAC or other cost inefficiencies

Run tests with:

```bash
python3 -m unittest discover tests/
```

---

## 🧠 Example Usage

To run the agent with example input:

```bash
python3 main.py
```

Example input structure:

```python
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
```

---

## 🛠️ Future Improvements

This project is designed to be extended into a production-ready system:

- ✅ **Database Integration**  
  The agent can be improved to automatically gather and analyze business data from databases such as PostgreSQL or MongoDB.

- ✅ **API Support**  
  Input and output can be handled via REST or GraphQL APIs for integration with web or mobile applications.

> ⚠️ **Note**: These features were **not implemented** in this version, as this is a test task focused on demonstrating core logic and reasoning.

---

## 🐳 Docker Support

You can build and run the project in a container:

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
```

### Build & Run

```bash
docker build -t business-agent .
docker run business-agent
```

---

## 📂 File Structure

```
business_ai_agent/
├── main.py
├── graph.py
├── schemas.py
├── nodes/
│   ├── analysis_node.py
│   └── input_node.py
├── tests/
│   └── test_agent.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 📄 License

This code is provided for demonstration and testing purposes.

import unittest
from graph import business_graph 
from schemas import AgentOutput  

class TestBusinessAgent(unittest.TestCase):

    def setUp(self):
        self.input_data = {
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

    def test_positive_profit_and_growth(self):
        result = business_graph.invoke(self.input_data)
        output = result["output"]
        self.assertIsInstance(output, AgentOutput)
        self.assertIn("message", output.model_dump())
        self.assertIn("warning", output.message.lower())

    def test_negative_profit_warning(self):
        input_data = {
            "business_data": {
                "today": {
                    "profit": -500,
                    "growth": -2,
                    "churned_customers": 5,
                    "revenue": 5000,
                    "cost": 5500,
                    "new_customers": 5
                },
                "yesterday": {
                    "profit": 1000,
                    "growth": 3,
                    "churned_customers": 1,
                    "revenue": 7000,
                    "cost": 6500,
                    "new_customers": 8
                }
            }
        }
        result = business_graph.invoke(input_data)
        output = result["output"]
        self.assertIsInstance(output, AgentOutput)
        self.assertIn("warning", output.message.lower())

    def test_cac_alert_triggered(self):
        input_data = {
            "business_data": {
                "today": {
                    "profit": 500,
                    "growth": 0,
                    "churned_customers": 10,
                    "revenue": 9000,
                    "cost": 8500,
                    "new_customers": 3
                },
                "yesterday": {
                    "profit": 600,
                    "growth": 1,
                    "churned_customers": 1,
                    "revenue": 9500,
                    "cost": 8000,
                    "new_customers": 12
                }
            }
        }
        result = business_graph.invoke(input_data)
        output = result["output"]
        self.assertIsInstance(output, AgentOutput)
        self.assertIn("warning", output.message.lower())

if __name__ == "__main__":
    unittest.main()

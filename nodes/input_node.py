from schemas import BusinessData

class InputNode:
    def __call__(self, input_payload):
        raw_data = input_payload.get("business_data", {})
        business_data = BusinessData(**raw_data)
        return {"business_data": business_data}
from langgraph.graph import StateGraph, END
from schemas import StateSchema
from nodes.input_node import InputNode
from nodes.analysis_node import analyze_business_data
from nodes.decision_node import make_decision

builder = StateGraph(StateSchema)

builder.add_node("input", InputNode())
builder.add_node("analyze", lambda state: {"analysis": analyze_business_data(state["business_data"])} )
builder.add_node("decide", lambda state: {"output": make_decision(state["analysis"])} )

builder.set_entry_point("input")
builder.add_edge("input", "analyze")
builder.add_edge("analyze", "decide")
builder.add_edge("decide", END)

business_graph = builder.compile()

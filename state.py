# Langchain = Tools + LLMs + Chains
# LangGraph = State + workflow + Decision Making

# User Question
#       |
#       v
#  Retrieve Docs
#       |
#       v
#  Evaluate Docs
#       |
#       +----> Good Docs ----> Generate Answer
#       |
#       +----> Bad Docs ----> Rewrite Query
#                               |
#                               v
#                          Retrieve Again

# By using LangGraph we can easily buld decision making workflow


from typing import TypedDict
from langgraph.graph import StateGraph, START, END



class State(TypedDict):
    a : int
    b : int 
    add_result : int
    sub_result : int
    mul_result : int
    div_result : int

# Define tools


def addition(a: int, b: int) -> int:
    return a + b

def addition_node(state:State):
    a = state['a']
    b = state['b']
    result = addition(a,b)

    return {
        'add_result':result
    }

def subtraction(a: int, b: int) -> int:
    return a - b

def sub_node(state:State):
    a = state['a']
    b = state['b']
    result = subtraction(a,b)
    return {
        'sub_result':result 
    }

def multiply(a: int, b: int) -> int:
    return a * b

def mul_node(state:State):
    a = state['a']
    b = state['b']
    result = multiply(a,b)
    return {
        'mul_result':result 
    }


def divide(a: int, b: int) -> float:
    return a / b

def div_node(state:State):
    a = state['a']
    b = state['b']
    result = divide(a,b)
    return {
        'div_result':result 
    }

graph = StateGraph(State)

graph.add_node('addition', addition_node)
graph.add_node('subtraction', sub_node)
graph.add_node('multiply', mul_node)
graph.add_node('divide', div_node)

graph.add_edge(START, 'addition')
graph.add_edge('addition', 'subtraction')
graph.add_edge('subtraction', 'multiply')
graph.add_edge('multiply', 'divide')
graph.add_edge('divide', END)
graph = graph.compile()
result = graph.invoke(
    {
        "a": 10,
        "b": 20
    }
)
print(result)






from typing import TypedDict
from langgraph.graph import StateGraph, START, END



class State(TypedDict):
    a : int
    b : int 
    mult : int
    div : int

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

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    return a / b

graph = StateGraph(State)

graph.add_node('addition', addition)
from typing import TypedDict
from langgraph.graph import StateGraph, START, END



class State(TypedDict):
    add : int
    sub : int 
    mult : int
    div : int

# Define tools


def addition(a: int, b: int):
    return a + b

def subtraction(a: int, b: int):
    return a - b

def multiply(a: int, b: int):
    return a * b

def divide(a: int, b: int):
    return a / b

graph = StateGraph(State)

graph.add_node('addition', addition)
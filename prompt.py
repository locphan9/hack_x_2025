import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import re
import pickle
import os
import json
from typing import List, Dict

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from langchain_community.graphs import ArangoGraph
from langchain_community.chains.graph_qa.arangodb import ArangoGraphQAChain
from langchain_core.tools import tool

# 5. Define the Text to NetworkX/cuGraph Tool
# Note: It is encouraged to experiment and improve this section! This is just a placeholder:
global_var = None
G = None
with open('book_graph.gpickle', 'rb') as f:
    G = pickle.load(f)
    

schemas = {
  "node_types": {
    "book": {
      "count": 500,
      "attributes": [
        "authors",
        "average_rating",
        "book_id",
        "description",
        "publication_year",
        "title",
        "url"
      ]
    },
    "genre": {
      "count": 10,
      "attributes": [
        "name"
      ]
    }
  },
  "edge_types": [
    {
      "source_type": "genre",
      "relationship": "has_book",
      "target_type": "book",
      "count": 1384
    }
  ],
  "summary": {
    "total_nodes": 510,
    "total_edges": 1384,
    "node_type_counts": {
      "book": 500,
      "genre": 10
    },
    "node_attributes": [
      "name",
      "description",
      "authors",
      "average_rating",
      "url",
      "title",
      "publication_year",
      "book_id"
    ],
    "edge_attributes": []
  }
}

@tool
def text_to_nx_algorithm_to_text(query: str) -> List[Dict[str,str]]:
    """This tool is available to invoke a NetworkX Algorithm on
    the NetworkX Graph. You are responsible for accepting the
    Natural Language Query, establishing which algorithm needs to
    be executed, executing the algorithm, and translating the results back
    to Natural Language, with respect to the original query. For final response, you must
    return a string containing a list of dictionaries List[Dict[str,str]]

    """
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o")

    ######################
    print("1) Generating NetworkX code")

    text_to_nx = llm.invoke(f"""
    I have a NetworkX Graph called `G`. It has the following schema: {schemas}

    I have the following graph analysis query: {query}.

    Analyze the `keyword`, `genre`, and `title` to generate Python code.
    
    Generate the Python Code required to answer the query using the `G` object.

    Be very precise on the NetworkX algorithm you select to answer this query. Think step by step.

    Only assume that networkx is installed, and other base python dependencies.
    
    Always set the last variable as `FINAL_RESULT`, which represents the answer to the original query.

    Only provide python code that I can directly execute via `exec()`. Do not provide any instructions.
    
    Make sure the `FINAL_RESULT` is a json string containing the title book["title"], and the link book["url"]

    Make sure that `FINAL_RESULT` stores a short & concise answer. Avoid setting this variable to a long sequence.

    Consider slicing if `FINAL_RESULT` may exceed limit_rate
    Your code:
    """).content
    text_to_nx_cleaned = re.sub(r"^```python\n|```$", "", text_to_nx, flags=re.MULTILINE).strip()

    print('-'*10)
    print(text_to_nx_cleaned)
    print('-'*10)

    ######################

    print("\n2) Executing NetworkX code")
    global_vars = {"G": G, "nx": nx}
    local_vars = {}

    try:
        exec(text_to_nx_cleaned, global_vars, local_vars)
        text_to_nx_final = text_to_nx
    except Exception as e:
        print(f"EXEC ERROR: {e}")
        return f"EXEC ERROR: {e}"

        # TODO: Consider experimenting with a code corrector!
        attempt = 1
        MAX_ATTEMPTS = 3

        # while attempt <= MAX_ATTEMPTS
            # ...

    print('-'*10)
    FINAL_RESULT = local_vars["FINAL_RESULT"]
    # print(f"FINAL_RESULT: {FINAL_RESULT}")
    print('-'*10)
    ######################

    return FINAL_RESULT

tools = [text_to_nx_algorithm_to_text]


def convert(query:str) -> List:
    """
    You are responsible for converting query in string format to a more structured List format
    """
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    response = llm.invoke(
    f"""
    I have an input {query} that is currently in string format.
    
    Please help me extract all book title and book url

    Make sure you give no further instruction

    And please help me output the final response in JSON string format that is easy for me to run json.load. Thank you
    """
    ).content
    return response
def query_graph(query):
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o")
    app = create_react_agent(llm, tools)
    final_state = app.invoke({"messages": [{"role": "user", "content": query}]})
    return final_state["messages"][-1].content
from flask import Flask, render_template, url_for, request
from prompt import query_graph
app = Flask(__name__)


# import os
# import pandas as pd
# import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt
# from random import randint
# import re
# import pickle
# import os

# from langgraph.prebuilt import create_react_agent
# from langgraph.checkpoint.memory import MemorySaver
# from langchain_openai import ChatOpenAI
# from langchain_community.graphs import ArangoGraph
# from langchain_community.chains.graph_qa.arangodb import ArangoGraphQAChain
# from langchain_core.tools import tool

# G = None
# with open('book_graph.gpickle', 'rb') as f:
#     G = pickle.load(f)


# schema = {
#   "node_types": {
#     "book": {
#       "count": 500,
#       "attributes": [
#         "authors",
#         "average_rating",
#         "book_id",
#         "description",
#         "publication_year",
#         "title",
#         "url"
#       ]
#     },
#     "genre": {
#       "count": 10,
#       "attributes": [
#         "name"
#       ]
#     }
#   },
#   "edge_types": [
#     {
#       "source_type": "genre",
#       "relationship": "has_book",
#       "target_type": "book",
#       "count": 1384
#     }
#   ],
#   "summary": {
#     "total_nodes": 510,
#     "total_edges": 1384,
#     "node_type_counts": {
#       "book": 500,
#       "genre": 10
#     },
#     "node_attributes": [
#       "name",
#       "description",
#       "authors",
#       "average_rating",
#       "url",
#       "title",
#       "publication_year",
#       "book_id"
#     ],
#     "edge_attributes": []
#   }
# }


# llm = ChatOpenAI(temperature=0, model_name="gpt-4o")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        user_input = request.form.get("search_query")  # Get input from form
        result = query_graph(user_input)  # Pass to function x
        if result:
            return render_template("index.html", result=str(result))  # Render result
        else:
            print(1)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
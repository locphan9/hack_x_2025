from prompt import query_graph, global_var, convert
import json
# a = query_graph("What is your favorite fruit?")
# b = query_graph("Return book with keyword Donovan")
# c = query_graph("Return books with mystery genre in graph dataset G")
a = query_graph('Crime books')

b = convert(a)
k = b.replace('```json\n', '').replace('\n```', '')
res = json.loads(k)
print(b)

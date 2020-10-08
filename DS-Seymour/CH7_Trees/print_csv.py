import pandas as pd
import networkx as nx
input_data = pd.read_csv('test.csv', index_col=0)
G = nx.DiGraph(input_data.values)
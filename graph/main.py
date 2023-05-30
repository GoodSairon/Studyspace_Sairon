import networkx as nx
import pandas as pd

def from_town_to_town(first_town_def, second_town_def):

    towns = nx.dijkstra_path(G, first_town_def, second_town_def)
    distance = 0
    print(nx.dijkstra_path(G, first_town_def, second_town_def))
    print(nx.dijkstra_path_length(G, first_town_def, second_town_def))
    for i in range(0, len(towns)-1):
        distance = distance + int(G[towns[i]][towns[i+1]].get('weigth'))
    print(distance)

G = nx.DiGraph()

data = pd.read_csv('cities.csv', delimiter = ';', names = ['first_town', 'second_town', 'distance'], encoding = 'latin-1' )

print(data)

first_town, second_town, distance = data.first_town, data.second_town, data.distance

for a, b, c in zip(first_town, second_town, distance):

    G.add_edge(a, b, weigth = int(c))

print(G)

a, b = input(), input()

from_town_to_town(a, b)


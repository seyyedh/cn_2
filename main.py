""" Se77edH
*** Seyyed Hassan Yajadda
*** March 2021
"""


import networkx as nx
import csv
import operator
import matplotlib.pyplot as plt
from scipy import sparse


file_bitcoin = "soc-sign-bitcoinotc.csv"
file_freindly = "friendly edge.csv"
file_infect_dublin = "infect-dublin.csv"

"""define network"""
with open(file_freindly) as infile:
    csv_reader = csv.reader(infile)
    G = nx.DiGraph(csv_reader)


""" Simple metrics """
N = G.number_of_nodes()
nodes = "number of nodes: " + str(N) + "\n"
edges = "number of edges: " + str(G.number_of_edges()) + "\n"
average_degree = "average degree connectivity: " + str(nx.average_degree_connectivity(G)) + "\n"
density = "density of G: " + str(nx.density(G)) + "\n"
average_clustering = "average clustering coefficient: " + str(nx.average_clustering(G)) + "\n"
transitivity = "Transitivity of Graph: " + str(nx.transitivity(G)) + "\n"
assortativity = "Assortativity(degree correlation) of G: " + str(nx.degree_assortativity_coefficient(G)) + "\n"

print(nx.average_degree_connectivity(G))
""" plot the graph """
# pos=nx.shell_layout(G)
# nx.draw(G,pos)
# plt.savefig('new.png')



""" top 5 nodes based on 4 different centrality measurements and Network centralization(based on 4 metrics) """
degree_centrality = nx.degree_centrality(G)
degree_centrality_5 = "Degree centrality (top 5 nodes): " + str(dict(sorted(degree_centrality.items(), key=operator.itemgetter(1), reverse=True)[:5])) + "\n"
deg_star = list(dict(sorted(degree_centrality.items(), key=operator.itemgetter(1), reverse=True)[:1]).values())[0]
degs = list(dict(sorted(degree_centrality.items(), key=operator.itemgetter(1), reverse=True)[:]).values())[:]

deg_sigma = 0
for i in degs:
    deg_sigma = deg_sigma + (deg_star - i)
degree_centralization = float(deg_sigma / ((N-1)*(N-2)))
degree_centralization_print = "Network centralization (Degree): " + str(degree_centralization) + "\n"


betweenness_centrality = nx.betweenness_centrality(G)
betweenness_centrality_5 = "betweenness centrality (top 5 nodes): " + str(dict(sorted(betweenness_centrality.items(), key=operator.itemgetter(1), reverse=True)[:5])) + "\n"
bet_star = list(dict(sorted(betweenness_centrality.items(), key=operator.itemgetter(1), reverse=True)[:1]).values())[0]
bets = list(dict(sorted(betweenness_centrality.items(), key=operator.itemgetter(1), reverse=True)[:]).values())[:]

bet_sigma = 0
for i in bets:
    bet_sigma = bet_sigma + (bet_star - i)
betweenness_centralization = float(bet_sigma / ((N-1)*(N-2)))
betweenness_centralization_print = "Network centralization (betweenness): " + str(betweenness_centralization) + "\n"



pagerank_centrality = nx.pagerank(G)
pagerank_centrality_5 = "Degree centrality (top 5 nodes): " + str(dict(sorted(pagerank_centrality.items(), key=operator.itemgetter(1), reverse=True)[:5])) + "\n"
page_star = list(dict(sorted(pagerank_centrality.items(), key=operator.itemgetter(1), reverse=True)[:1]).values())[0]
pages = list(dict(sorted(pagerank_centrality.items(), key=operator.itemgetter(1), reverse=True)[:]).values())[:]

page_sigma = 0
for i in pages:
    page_sigma = page_sigma + (page_star - i)
pagerank_centralization = float(page_sigma / ((N-1)*(N-2)))
pagerank_centralization_print = "Network centralization (Pagerank): " + str(pagerank_centralization) + "\n"



closeness_centrality = nx.closeness_centrality(G)
closeness_centrality_5 = "Closeness centrality (top 5 nodes): " + str(dict(sorted(closeness_centrality.items(), key=operator.itemgetter(1), reverse=True)[:5])) + "\n"
close_star = list(dict(sorted(closeness_centrality.items(), key=operator.itemgetter(1), reverse=True)[:1]).values())[0]
closes = list(dict(sorted(closeness_centrality.items(), key=operator.itemgetter(1), reverse=True)[:]).values())[:]

close_sigma = 0
for i in closes:
    close_sigma = close_sigma + (close_star - i)
closeness_centralization = float(close_sigma / ((N-1)*(N-2)))
closeness_centralization_print = "Network centralization (Closeness): " + str(closeness_centralization) + "\n"



# with open("friendly_netwrokX_report.txt",'w') as file:
#     file.write("Report of friendly network" + "\n" + "*** By Seyyed Hassan Yajadda ***" + "\n\n\n")
#     file.write(nodes
#                 + edges
#                 + average_degree
#                 + density
#                 + average_clustering
#                 + transitivity
#                 + assortativity
#                 + degree_centrality_5
#                 + betweenness_centrality_5
#                 + closeness_centrality_5
#                 + pagerank_centrality_5
#                 + degree_centralization_print
#                 + betweenness_centralization_print
#                 + closeness_centralization_print
#                 + pagerank_centralization_print)
#     file.close()







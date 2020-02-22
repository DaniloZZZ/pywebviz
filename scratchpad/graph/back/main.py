from libvis.modules import BaseModule
import networkx as nx
from networkx.readwrite import json_graph
import json


def graph_to_d3json(graph):
    """
    Converts a graph to json node-link file
    res: string
            converted json string
    """
    data = json_graph.node_link_data(graph)
    res = json.dumps(data)
    return res



class graph(BaseModule):
    name="graph"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def vis_get(self, key):
        value = self[key]
        value = graph_to_d3json(value)
        print('sending value to front: ', key, value)
        return value

    def vis_set(self, key, value):
        super().vis_set(key, value) # same as self[key] = value
        print('updated value form front: ', key, value)

    @classmethod
    def test_object(cls):
        n = cls()
        n.graph = nx.petersen_graph()
        n.graph = nx.barabasi_albert_graph(50, 1)

        return n

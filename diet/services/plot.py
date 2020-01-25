import pandas as pd
import matplotlib as m
import matplotlib.pyplot as mp
from diet.models.weights import Weights

class Graph:
    def __init__(self):
        table = Weights.query.all()
        self.df = pd.DataFrame(
            [(row.date, float(row.weight)) for row in table],
            columns=['date', 'weight']
        )

    def plot_graph(self, graph_path):
        self.df.plot(x='date')
        mp.grid(which='major', color='black', linestyle=':')
        m.pyplot.savefig(graph_path)

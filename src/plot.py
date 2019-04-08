import pandas as p
import matplotlib as m
import matplotlib.pyplot as mp


class Graph:
    def __init__(self):
        self.df = p.read_csv('weight.csv')

    def plotGraph(self):
        self.df.plot(x='date')
        mp.grid(which='major', color='black', linestyle=':')

        m.pyplot.savefig("weight.png")

"""
A simple 2D potential with customisable x and y basins
"""
import numpy as np
import matplotlib.pyplot as plt

class TwoDWell:
    def __init__(self, **kwargs):
        self.g1 = kwargs.get('g1', 1)
        self.g2 = kwargs.get('g2', -10)
        self.g3 = kwargs.get('g3', -10)
        self.a1 = kwargs.get('a1', -30)
        self.a2 = kwargs.get('a2', -3)
        self.b1 = kwargs.get('b1', -30)
        self.b2 = kwargs.get('b2', -3)
        self.x0 = kwargs.get('x0', 0.4)
        self.y0 = kwargs.get('y0', 0)

    def forces(self, x, y):

        t1 = self.g1*(x*x + y*y)**2
        t1dx = self.g1*2*(x*x + y*y)*2*x
        t1dy = self.g1*2*(x*x + y*y)*2*y

        t2 = self.g2*np.exp(self.a1*(x-self.x0)**2 + self.a2*(y-self.y0)**2)
        t2dx = t2*self.a1*2*(x-self.x0)
        t2dy = t2*self.a2*2*(y-self.y0)

        t3 = self.g3*np.exp(self.b1*(x+self.x0)**2 + self.b2*(y+self.y0)**2)
        t3dx = t3*self.b1*2*(x+self.x0)
        t3dy = t3*self.b2*2*(y+self.y0)

        energy = t1+t2+t3
        fx = -(t1dx + t2dx + t3dx)
        fy = -(t1dy + t2dy + t3dy)

        return fx, fy, energy

    def energy(self, x, y):

        t1 = self.g1*(x**2 + y**2)**2

        t2 = self.g2*np.exp(self.a1*(x-self.x0)**2 + self.a2*(y-self.y0)**2)

        t3 = self.g3*np.exp(self.b1*(x+self.x0)**2 + self.b2*(y+self.y0)**2)

        energy = t1+t2+t3
        return energy
    
    def plot(self, x_range=(-1,1), y_range=(-1,1), steps=1000, cmap="viridis", levels=20):
        x = np.linspace(x_range[0], x_range[1], steps)
        y = np.linspace(y_range[0], y_range[1], steps)
        X, Y = np.meshgrid(x, y)
        Z = self.energy(X, Y)
        plt.contourf(X, Y, Z, levels, cmap='viridis');
        
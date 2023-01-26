import numpy as np
from simpledescent.potential import TwoDWell
import matplotlib.pyplot as plt

class Minimisation:
    def __init__(self, potential=TwoDWell):
        self.potential = potential()
        self.positions = None
        self.energies = None
        self.minimum = None
    
    def minimise(self, initial_position, nsteps=10000, 
                 learning_rate=0.01, tolerance=1e-6):
        px = initial_position[0]
        py = initial_position[1]
        positions_x = []
        positions_y = []
        energies = []
        positions_x.append(px)
        positions_y.append(py)
        
        for i in range(nsteps):           
            fx, fy, energy = self.potential.forces(px, py)
            energies.append(energy)
            ediffx = learning_rate*fx
            ediffy = learning_rate*fy
            if np.all(np.abs([ediffx, ediffy])) <= tolerance:
                print("Reached threshold")
                break
            px += ediffx
            py += ediffy
            positions_x.append(px)
            positions_y.append(py)
        else:
            print("Steps finished, did not find minimum")
        self.positions = [positions_x, positions_y]
        self.energies = np.array(energies)
        position = [px, py]
        self.minimum = position
        return position
    
    def plot(self, x_range=(-1,1), y_range=(-1,1), steps=1000, cmap="viridis", levels=20):
        self.potential.plot(x_range=x_range, y_range=y_range, steps=steps, cmap=cmap, levels=levels)
        plt.plot(self.positions[0], self.positions[1],
                c="#f57c00")
        plt.scatter(self.positions[0][0], self.positions[1][0],
                   c="#f57c00", label="start")
        plt.scatter(self.positions[0][-1], self.positions[1][-1],
                   c="#b71c1c", label="stop")
        plt.xlim(x_range[0], x_range[-1])
        plt.ylim(x_range[0], x_range[-1])
        plt.legend()
        
    
import argparse as ap
from simpledescent.potential import TwoDWell
from simpledescent.minimise import Minimisation

def main():
    arg = ap.ArgumentParser()
    
    #argument name of input file
    arg.add_argument("-p", "--position", required=True,
                    nargs=2, type=float,
                    help="initial position")

    arg.add_argument("-n", "--nsteps", required=False, type=int, default=10000,
    help="number of minimisation steps")
    
    arg.add_argument("-l", "--lrate", required=False, type=float, default=0.002,
    help="learning rate")

    #parse arguments
    args = vars(arg.parse_args())
    px = args["position"][0]
    py = args["position"][1]
    nsteps = args["nsteps"]
    lrate = args["lrate"]
    
    #run minimisation
    mini = Minimisation()
    res = mini.minimise([px, py], learning_rate=lrate,
                 nsteps=nsteps)
    print(f'{res[0]} {res[1]}')
    

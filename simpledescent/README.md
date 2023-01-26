# Simpledescent

As the name says, `simpledescent` is a small code to find the local minimum of a given potential using [gradient descent algorithm](https://en.wikipedia.org/wiki/Gradient_descent). It is developed to be used as an example.

## Installation

```
python setup.py install
```

## Use

### In a notebook

```
from simpledescent.minimise import Minimisation

mini = Minimisation()
mini.minimise([-0.75, 0.25], learning_rate=0.002)
mini.plot()
```

The potential used is a simple 2D well potential. The potential is defined in `simpledescent/potential.py`. You can also add custom potentials there.  In the above example, the potential can also be optionally defined:

```
from simpledescent.potential import TwoDWell
from simpledescent.minimise import Minimisation

mini = Minimisation(potential=TwoDWell)
mini.minimise([-0.75, 0.25], learning_rate=0.002)
mini.plot()
```

### From command line

Simpledescent also provides a command line interface.

```
simpledescent --help
```

The same example as above can be run using:

```
simpledescent --position -0.75 0.25
```
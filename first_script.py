import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser


def parabolaEquation():
    x: int = range(-50, 50)
    y: int = [x*x for x in x]
    str = 'y=x^2'

    plt.plot(x, y, label=str)
    plt.title('Graph of y=x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
    return str


def slopeEquation():
    x: int = np.linspace(-5, 5, 100)
    y: int = 2*x+1
    str = 'y=2x+1'

    plt.plot(x, y, '-r', label=str)
    plt.title('Graph of y=2x+1')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
    return str


def graphBuilder(graph, x):
    if (graph == 'y=2x+1'):
        x: int = x
        y = 2*x+1
        print("The answer is:", y)
        slopeEquation()
    elif graph == 'y=x^2':
        x: int = x
        y = x*x
        print("The answer is:", y)
        parabolaEquation()
    else:
        print("Such graphic does not exist yet")
    return graph


def parse_args():
    parser = ArgumentParser(
        description='A program to parse arguments provided by the user'
    )
    parser.add_argument(
        '-gr',
        '--graph',
        type=str,
        required=True,
        help='The graph that should be displayed.' +
        'Input the equation with no spaces'
    )
    parser.add_argument(
        '-x',
        '--x_value',
        required=False,
        type=int,
        help='The x value to calculate the equation'
    )
    return parser.parse_args()


def test_graphBuilder():
    assert parabolaEquation() == 'y=x^2'


if __name__ == '__main__':
    args = parse_args()
    graph = args.graph
    x = args.x_value

    graphBuilder(graph, x)

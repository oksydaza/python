import matplotlib.pyplot as plt
import numpy as np

def plot_function(equation):
    """
    Function plot equation from given argument. 
    """
    x = np.linspace(-5,5,100)
    y = eval(equation)
    plt.plot(x, y, '-r', label=equation)
    plt.title(f'Graph of {equation}')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_function("x**2 - 6*x + 3")

import numpy as np
from numpy.typing import NDArray
from matplotlib.axes import Axes

BLUE = "#376EB5"
ORANGE = "#ED7800"
PURPLE = "#CA8DFD"
GREY = "#8C8C8C"

XLIMS = np.array((93.7, 107.3))


def plot_histogram(ax: Axes, x: NDArray, y: NDArray, **plot_kwargs):
    kwargs = plot_kwargs.copy()
    if "color" in kwargs:
        color = kwargs.pop("color")
        kwargs["c"] = color
    kwargs.setdefault("c", BLUE)
    ax.plot(x, y, "o", **kwargs)
    for x_, y_ in zip(x, y):
        ax.plot((x_, x_), (0, y_), c=kwargs["c"], lw=0.8)

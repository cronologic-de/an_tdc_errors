import numpy as np
from numpy.typing import NDArray
from matplotlib.axes import Axes

BLUE = "#376EB5"
ORANGE = "#ED7800"
PURPLE = "#CA8DFD"
GREY = "#8C8C8C"

XLIMS = np.array((93.7, 107.3))


def plot_histogram(ax: Axes, x: NDArray, y: NDArray, **plot_kwargs):

    # edges = x
    # edges = np.append(edges, x[-1] + 1.0)

    # x_ = np.repeat(edges, 2)
    # y_ = np.empty_like(x_, dtype=np.float64)
    # y_[0] = 0
    # y_[1:-1] = np.repeat(y, 2)
    # y_[-1] = 0
    # kwargs = plot_kwargs.copy()
    # if "color" not in kwargs and "c" not in kwargs:
    #     kwargs["c"] = BLUE
    # ax.plot(x_, y_, "-", **kwargs)

    kwargs = plot_kwargs.copy()
    if "color" in kwargs:
        color = kwargs.pop("color")
        kwargs["c"] = color
    kwargs.setdefault("c", BLUE)
    ax.plot(x, y, "o", **kwargs)
    for x_, y_ in zip(x, y):
        ax.plot((x_, x_), (0, y_), c=kwargs["c"], lw=0.8)


def plot_dt(ax: Axes, t0, t1, timespan_0, timespan_width):
    y = 0.4

    arrowprops = dict(arrowstyle="<->", shrinkA=0, shrinkB=0, color=ORANGE)
    ax.annotate("", xy=(t0, y), xytext=(t1, y), arrowprops=arrowprops)
    ax.text(
        timespan_0 + timespan_width / 2.0,
        y + 0.1,
        f"$dT$ (measured) = {t1-t0:.0f}",
        color=ORANGE,
        ha="center",
    )

import numpy as np
import mplutils as mplu
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from typing import Final

import plots


CRONOBLUE: Final = "#376eb5"
CRONOORANGE: Final = "#ed7800"
GREY: Final = "#8c8c8c"


def load_data() -> NDArray[np.float64]:
    return np.loadtxt("cable_delay_hist_xTDC4.dat").T


def plot():
    data_ths = load_data()

    plt.style.use("cronostyle.mplstyle")
    plt.rcParams["axes.spines.left"] = True
    plt.rcParams["axes.spines.bottom"] = True
    plt.rcParams["axes.spines.top"] = True
    plt.rcParams["axes.spines.right"] = True
    plt.rcParams["font.size"] = 9.0

    layout_engine = mplu.FixedLayoutEngine(
        margin_pads_pts=(25, 5, 5, 5), col_pads_ignore_labels=True, col_pads_pts=3
    )
    fig, axs = plt.subplots(nrows=1, ncols=4, layout=layout_engine)

    fig.suptitle("xTDC4 – Cable Delay Measurements")

    titles = [f"Channel {which}" for which in "ABCD"]

    for i, ax in enumerate(axs):
        xs_ths = data_ths[2 * i + 0]
        ys_ths = data_ths[2 * i + 1]
        xmax = xs_ths[np.argmax(ys_ths)]
        xs_ths -= xmax
        ys_ths = ys_ths / np.sum(ys_ths) * 100.0  # percent
        x = xs_ths[ys_ths != 0]
        y = ys_ths[ys_ths != 0]
        plots.plot_histogram(ax, x, y, c=CRONOBLUE)

        ax.set_xlim(-2.8, 2.8)
        ax.set_title(titles[i])

    for ax in axs:
        ax.set_ylim(0, axs[3].get_ylim()[1])
        mplu.set_axes_size(1.0, aspect=3, ax=ax)
        ax.xaxis.set_major_locator(MultipleLocator(1))

    for ax in axs[1:]:
        ax.set_yticklabels([])

    axs[0].set_ylabel("Intensity (%)")
    axs[2].set_xlabel("Relative delay (bins)")
    axs[2].xaxis.set_label_coords(0, -0.055)

    fig.savefig("output/cable_delay_hist_xTDC4.pdf")
    fig.savefig("../_figures/cable_delay_hist_xTDC4.svg")

    plt.close()


if __name__ == "__main__":
    plot()

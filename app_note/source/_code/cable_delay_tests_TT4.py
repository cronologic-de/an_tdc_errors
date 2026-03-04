import numpy as np
import matplotlib.pyplot as plt
import mplutils as mplu
from matplotlib.ticker import MultipleLocator

import plots

FNAME = "cable_delay_tests_TT4"
VARIANT_NAMES = [f"TimeTagger4-{v}G" for v in ("10", "5", "2.5", "1.25")]
CHANNEL_NAMES = [f"Channel {c}" for c in "ABCD"]
XLIMS = -18, 18
XTICKS = -16, -8, 0, 8, 16
XTICKLABELS = ["", "$-$8", "0", "8", "16"]

DataArray = np.ndarray[tuple[int, int, int, int], np.dtype[np.float64]]


def print_data(data: DataArray) -> None:
    for variant_data, variant_name in zip(data, VARIANT_NAMES):
        print(f"\n{variant_name}")
        for channel_data, channel_name in zip(variant_data, CHANNEL_NAMES):
            print(channel_name)
            print(channel_data)


def load_data() -> DataArray:
    """
    Load data from FNAME.csv

    Returns a numpy array of shape (4, 4, 2, 4)
    - 1st index is TimeTagger Type (10G, 5G, 2.5G, 1.25G)
    - 2nd index is Channel (A, B, C, D)
    - 3rd index is (bin, value)
    """
    data = np.loadtxt(f"{FNAME}.csv", delimiter=",", skiprows=1).T
    data = data.reshape((4, 4, 2, -1))
    return data


def normalize_to_100(data: DataArray) -> DataArray:
    for variant_data in data:
        for channel_data in variant_data:
            # data_without_nan = channel[1].copy()
            # data_without_nan[np.isnan(data_without_nan)] = 0
            channel_data[1] /= np.sum(channel_data[1]) / 100.0
    return data


def shift_data(data: DataArray) -> DataArray:
    for v, variant in enumerate(data):
        for c, channel_data in enumerate(variant):
            peak_pos = channel_data[0, np.argmax(channel_data[1])]
            data[v, c, 0] -= peak_pos
    return data


def main():
    data = load_data()
    data = normalize_to_100(data)
    data = shift_data(data)

    layout_engine = mplu.FixedLayoutEngine(col_pads_ignore_labels=True, col_pads_pts=3)

    plt.style.use("cronostyle.mplstyle")
    plt.rcParams["axes.spines.left"] = True
    plt.rcParams["axes.spines.bottom"] = True
    plt.rcParams["axes.spines.top"] = True
    plt.rcParams["axes.spines.right"] = True
    plt.rcParams["font.size"] = 9.0

    fig, axs = plt.subplots(4, 4, layout=layout_engine)

    for v, vname in enumerate(VARIANT_NAMES):
        ymax = data[v, :, 1].max()
        axs[v, 0].text(
            0.0,
            1.10,
            vname,
            transform=axs[v, 0].transAxes,
            clip_on=False,
            fontsize="large",
        )
        for c, cname in enumerate(CHANNEL_NAMES):
            ax = axs[v, c]

            ax.set_title(cname)

            x, y = data[v, c]
            x = x[y != 0]
            y = y[y != 0]

            plots.plot_histogram(ax, x, y)
            mplu.set_axes_size(1.00, aspect=3.0, ax=axs[v, c])
            ax.set_xlim(-17, 17)
            ax.xaxis.set_major_locator(MultipleLocator(8))
            ax.set_ylim(0, ymax * 1.05)

    for ax in axs[:, 1:].flat:
        ax.set_yticklabels([])
        ax.set_xticks(XTICKS, XTICKLABELS)

    for ax in axs[:, 0]:
        ax.set_ylabel("Intensity (%)")
        ax.set_xticks(XTICKS, ("$-$16", *XTICKLABELS[1:]))
    for ax in axs[:, 2]:
        ax.set_xlabel("Relative delay (LSB)")
    for ax in axs[:, 2]:
        ax.xaxis.set_label_coords(0, -0.055)

    fig.savefig(f"output/{FNAME}.pdf")
    fig.savefig(f"../_figures/{FNAME}.svg")


if __name__ == "__main__":
    main()

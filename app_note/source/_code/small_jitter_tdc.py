from typing import Any

import numpy as np
from numpy.typing import NDArray
import mplutils as mplu
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

import tdc
import plots


def create_frame(fname_output: str) -> None: ...


def simulate_cable_delay_test(
    dt: float, n_measurements: int, jitter
) -> tuple[NDArray, NDArray]:
    rng = np.random.default_rng(5789161036159503)
    times_start = rng.random(n_measurements)
    times_stop = times_start + dt

    dts_measured = tdc.measure_dt(times_start, times_stop, jitter_std=jitter)

    values, counts = np.unique(dts_measured, return_counts=True)
    counts = counts / n_measurements * 100

    return values, counts


def cable_delay_test_histogram():

    plt.style.use("cronostyle.mplstyle")

    layout_engine = mplu.FixedLayoutEngine()
    fig, ax = plt.subplots(1, 1, layout=layout_engine)

    delta_times = (95.3, 100.3, 105.3)
    jitters = (0.05, 0.1, 0.20)
    colors = (plots.BLUE, plots.ORANGE, plots.PURPLE)

    for dt, jitter, color in zip(delta_times, jitters, colors):
        values_0, counts_0 = simulate_cable_delay_test(dt, 1_000_000, jitter)
        label = r"$\sigma_{\mathrm{Jitter}}$ = " f"{jitter*100:.0f}%"
        plots.plot_histogram(ax, values_0, counts_0, c=color, label=label)

    ax.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0))
    mplu.set_axes_size(4, aspect=3 / 4)

    ax.set_ylim(bottom=0)

    ax.axvline(97.5, color=plots.GREY, lw=0.8, ls="--")
    ax.axvline(102.5, color=plots.GREY, lw=0.8, ls="--")
    ax.set_xlim(plots.XLIMS)
    ax.set_xticks(
        np.arange(94, 107.5, 1),
        (
            "",
            "100",
            "101",
            "",
            "",
            "99",
            "100",
            "101",
            "",
            "",
            "99",
            "100",
            "101",
            "102",
        ),
    )

    ax.set_xlabel("measured start minus stop time (bins)")
    ax.set_ylabel("intensity (%)")

    fig.savefig("../_figures/small_jitter_tdc_histogram.svg")
    plt.show()


def main():
    cable_delay_test_histogram()


if __name__ == "__main__":
    main()

import numpy as np
from numpy.typing import NDArray

rng = np.random.default_rng(42)


def measure(times: NDArray[np.float64], jitter_std: float) -> NDArray[np.int_]:
    if jitter_std > 0.0:
        noise = rng.normal(scale=jitter_std, size=times.shape)
        times += noise
    return (times // 1).astype(int)


def measure_dt(
    times_start: NDArray[np.float64], times_stop: NDArray[np.float64], jitter_std: float
) -> NDArray[np.int_]:
    t0 = measure(times_start, jitter_std)
    t1 = measure(times_stop, jitter_std)
    return t1 - t0

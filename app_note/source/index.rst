==========================================
Application Note – Quantization vs. Jitter
==========================================

.. admonition:: In this App-Note

    In this application note, we will highlight the effects of quantization errors
    and jitter on classic start-stop time-to-digital converters.
    

Performance Test - Measuring a Constant Delay
=============================================

Measuring a constant delay is a good way to test the performance of a classic
start-stop time-to-digital converter (TDC), such as the
`xHPTDC8 <https://www.cronologic.de/product/xhptdc8-pcie>`__,
`xTDC4 <https://www.cronologic.de/product/xtdc4>`__,
and `TimeTagger4 <https://www.cronologic.de/product/timetagger>`__
devices sold by `cronologic <https://www.cronologic.de>`__.

One way to measure constant delays is to repeatedly measure the delay caused by
a long cable:
A signal is split into two.
Then, the timing of the first signal is measured by the *start* channel of the TDC.
The second signal is delayed by sending it through a long cable,
then its timing is measured by the *stop* channel.
This measurement is repeated many times and a histogram is filled with the measured
difference of the *stop time* minus the *start time*.

The shape of the output histogram will depend on two factors:
the bin size and the accuracy of measuring the exact start and stop times.
In particular, the ratio between bin size and accuracy will be of interest in this
application note.

The distinction between the two factors is critical, as we will show in this
application note. The bin size causes a *quantization error*. Other error sources
that keep us from accurately measuring real times are referred to as *jitter*.
Jitter can be caused by many things, for example, it may be the caused by the jitter
of an external reference clock, the different
triggering times of the start/stop channels due to noisy signals, or unequally sized
TDC bins.
All these errors are combined are simply referred to as “jitter” throughout.

.. note::
    In this application note, everything will be given in units of the bin size,
    that is, the bin size is 1.

Case 1 - Perfect TDC
====================

For reference, let's assume we have a perfect TDC that has absolute accuracy, that is,
absolutely no jitter is present.


We first will assume that there are no timing errors of our TDC.
Such a TDC quantizes continuous times perfectly into discrete bins (of bin size 1).

If we now want to measure a constant delay of, let's say, *ΔT* = 100.3.
Let the start times *t*\ :sub:`start` be continuous.
The stop times are *t*\ :sub:`start` = *t*\ :sub:`stop` + *ΔT*.

In our example of *ΔT* = 100.3, we will get two possible measurements:
100 or 101. To understand this, consider the following two start times

**Example 1:** *t*\ :sub:`start` = 0.1 and *t*\ :sub:`stop` = 0.1 + 100.3 = 100.4
    Due to the quantization of times into bins of size 1, the TDC will measure
    *t*\ :sub:`start,TDC` = 0, *t*\ :sub:`stop,TDC` = 100,
    and *ΔT*\ :sub:`TDC` = 100 – 0 = **100**.

**Example 2**: *t*\ :sub:`0` = 0.9 and *t*\ :sub:`1` = 0.9 + 100.3 = 101.2
    Now
    *t*\ :sub:`start,TDC` = 0, *t*\ :sub:`stop,TDC` = 101,
    and *ΔT*\ :sub:`TDC` = 101 – 0 = **101**.
    
Note that in the two examples above, there are *no error sources besides the
quantization error*.
A perfect TDC will always measure two discrete values for a constant delay (unless
the delay is an *exact* multiple of the bin size) and the relative intensity of these
values depends on the actual delay.

The following graphic shows the final histogram after simulating
one million measurements of various *ΔT* with a perfect TDC.
As one can see, the relative intensity of the bins changes, but there are always 2 bins
in the histogram.

.. image:: _figures/perfect_tdc_histogram.svg
    :align: center
    :alt: Constant-delay histogram of a perfect TDC.

Note that from the above histogram, one cannot estimate the error that results from
general jitter, as the histogram is purely the result of the quantization.
For example, the standard deviation of the blue data (with *ΔT* = 95.5) is 0.5,
however, timing errors due to general jitter are *zero*
(as per definition of the simulation).


Case 2 - TDC Dominated by Quantization Error
============================================

The following animation and graphic performs is based on the same simulations of
**Case 1**, except that now, before the real times are quantized, a small
error (jitter) is added to them.

In particular, the jitter follows a normal distribution with a standard deviation
of 0.05/0.1/0.2 bins.

In the figure, a constant delay of 100.3 is measured multiple times and the magnitude
of the jitter is increased from 5% to 15% of the bin size. One can see that at 5%,
the histogram is virtually identical to the ideal case shown above. With increasing
jitter, more output values appear and the histogram starts to differ more substantially
from the ideal case.

.. image:: _figures/small_jitter_tdc_histogram.svg
    :align: center
    :alt: Constant-delay histogram of a TDC dominated by quantization error.

Case 3 - TDC Dominated by Jitter
================================

Increasing the jitter (relative to the bin size) further yields histograms that are
dominated by the jitter.

In the following figure, measurement of a constant delay of 100.3 is simulated
multiple times with the same method as in *Case 2*, but with jitter magnitudes
comparable or much larger than the binsize.

.. image:: _figures/large_jitter_tdc_histogram.svg
    :align: center
    :alt: Constant-delay histogram of a TDC dominated by jitter.

Note that, as these histograms are dominated by the jitter and *not* the quantization
error, one can estimate the magnitude of the jitter from the histograms. For example,
the standard deviation of the purple histogram data
(with :math:`\sigma_{\mathrm{Jitter}}` = 500%) is :math:`\sigma_{\mathrm{Hist}}` = 708%,
close to the expectation of :math:`\sqrt{2} \times \sigma_{\mathrm{Jitter}}` 
(since the TDC performs two measurements, start and stop, the jitter
applies twice, ergo the expected standard deviation of the histogram data is a
factor :math:`\sqrt{2}` larger than the standard deviation of the jitter).


Animation of the measurement principle
======================================

The following animation visualizes the measurement principle of a classic start-stop
TDC.

On the left, the constant delay *ΔT* is represented by a blue ruler with fixed length.
The start (and stop) times increase continuously and are quantized by the TDC.
The resulting *measured* *ΔT* is shown by the orange double-arrow above the ruler.

On the right, a histogram of continuously measured delay times is shown.

The top row of the animation represents a perfect TDC. Each time gets sorted correctly
into perfectly sized bins. The bottom row represents a TDC with significant jitter.
The error due to the jitter is represented by differently sized bins, causing more
values to appear in the histogram.

TODO: fix units in animation to be consistent with the app note. At the moment top row
and bottom row have different bin sizes (which is confusing)

.. video:: _figures/fixed_vs_variable_binsize_100dpi.mp4
    :align: center
    :autoplay:
    :loop:
# spikes [![PyPI version](https://badge.fury.io/py/spikes.svg)](https://badge.fury.io/py/spikes) [![Build Status](https://travis-ci.org/eendroroy/spikes.svg?branch=master)](https://travis-ci.org/eendroroy/spikes)
A command line tool to display bar-chart.

## installation
use pip

    pip install spikes

## usage

    spike 2 4 3 7 2 9
    ▂▄▃▆▂█

use more than 1 line to display the chart

    spike -l 3   2 4 3 7 2 9
       ▃ █
     ▃ █ █
    ▅███▅█

read from stdin

    spike
    2 4 3 7 2 9
    # press Ctrl-D
    ▂▄▃▆▂█

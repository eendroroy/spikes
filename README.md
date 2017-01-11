# spikes

[![Join the chat at https://gitter.im/eendroroy/spikes](https://badges.gitter.im/eendroroy/spikes.svg)](https://gitter.im/eendroroy/spikes?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![PyPI version](https://badge.fury.io/py/spikes.svg)](https://badge.fury.io/py/spikes)
[![Build Status](https://travis-ci.org/eendroroy/spikes.svg?branch=master)](https://travis-ci.org/eendroroy/spikes)
[![Code Climate](https://codeclimate.com/github/eendroroy/spikes/badges/gpa.svg)](https://codeclimate.com/github/eendroroy/spikes)

A tool to display bar-chart anywhere.

## installation
use pip

    $ pip install spikes

## usage

    $ spike 2 4 3 7 2 9
    ▂▄▃▆▂█

    $ spike .1 .5 .9 2.5
    ▁▂▃█

use more than 1 line to display the chart

    $ spike -l 3   2 4 3 7 2 9
       ▃ █
     ▃ █ █
    ▅███▅█

read from stdin

    $ spike
    > 2 4 3 7 2 9
    > # press Ctrl-D
    ▂▄▃▆▂█

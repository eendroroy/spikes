**spikes**
==========

.. image:: https://badges.gitter.im/eendroroy/spikes.svg
    :target: https://gitter.im/eendroroy/spikes?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
.. image:: https://badge.fury.io/py/spikes.svg
    :target: https://badge.fury.io/py/spikes
.. image:: https://travis-ci.org/eendroroy/spikes.svg?branch=master
    :target: https://travis-ci.org/eendroroy/spikes
.. image:: https://codeclimate.com/github/eendroroy/spikes/badges/gpa.svg
    :target: https://codeclimate.com/github/eendroroy/spikes)
.. image:: https://codecov.io/gh/eendroroy/spikes/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/eendroroy/spikes

A tool to display bar-chart anywhere.

**installation**

use pip

::

.   $ pip install spikes

**usage**

:: 

.   $ spike 2 4 3 7 2 9
.   ▂▄▃▆▂█
.
.   $ spike .1 .5 .9 2.5
.   ▁▂▃█


use more than 1 line to display the chart

::

.   $ spike -l 3   2 4 3 7 2 9
.      ▃ █
.    ▃ █ █
.   ▅███▅█


read from stdin

::

.   $ spike
.   > 2 4 3 7 2 9
.
.   > # press Ctrl-D
.   ▂▄▃▆▂█


**use with git**
commit count per day:

::

.   $ git log | grep Date | awk '{print " : "$4" "$3" "$6}' | uniq -c | awk '{print $1}' | spike
.
.   ▁▄▅▁▁▂▁▁▂▄▄▇▃█▁▁▁▁▁▁▁


commit count per author

::

.   $ git log | grep Author | awk '{print $NF}' | sort | uniq -c | awk '{print $1}' | spike -l4
.
.   █
.   █
.   █  ▁
.   █▅▁█▅▂▆▄█


**license**

*MIT*

.. image:: https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Feendroroy%2Fspikes.svg?type=large
    :target: https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Feendroroy%2Fspikes?ref=badge_large

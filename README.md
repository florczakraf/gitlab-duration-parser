![Latest version](https://img.shields.io/pypi/v/gitlab-duration-parser.svg)
[![Build Status](https://travis-ci.org/florczakraf/gitlab-duration-parser.svg?branch=master)](https://travis-ci.org/florczakraf/gitlab-duration-parser)
![Supported Pythons](https://img.shields.io/pypi/pyversions/gitlab-duration-parser.svg)

# gitlab-duration-parser

A simple Gitlab time-tracking message parser

## Rationale
Gitlab's api still [doesn't provide a reliable way of getting the time-tracking
statistics](https://gitlab.com/gitlab-org/gitlab-ce/issues/42534) so one has to
manually parse the issues and merge requests in order to do get detailed information.
Currently only the totals for estimates and spent time are available.

Time-tracking `notes` (comments in Gitlab's jargon) come in the following flavors:
```python
'added 2h of time spent at 2019-06-06'
'subtracted 3w 2d 1h of time spent at 2019-06-08'
```

## API
The module provides only one function -- `parse(s)`. It returns number of seconds
based on the provided string. It will return negative number in case of subtracting
time. In case of parsing error, 0 will be returned.

## Usage snippet
```python
import datetime
import gitlab_duration_parser

# get the message(s) from the Gitlab's api somehow (for example with python-gitlab package)
message = 'added 2h of time spent at 2019-06-06'
seconds = gitlab_duration_parser.parse(message)

# after calculations you can use datetime.timedelta(seconds=...)
# to convert the seconds back to something more usable
str(datetime.timedelta(seconds=seconds*0.8))  # Steve always rounds his times up
# --> '1:36:00'
```

## Test
Get `tox`, supported python interpreters and just:
```
tox
```

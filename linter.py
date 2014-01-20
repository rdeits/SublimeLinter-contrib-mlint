#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Robin Deits
# Copyright (c) 2014 Robin Deits
#
# License: MIT
#

"""This module exports the Mlint plugin class."""

from SublimeLinter.lint import Linter, util, highlight


class Mlint(Linter):

    """Provides an interface to mlint, the standalone MATLAB linter"""

    syntax = 'matlab'
    cmd = 'mlint'
    regex = r'L (?P<line>\d+) \(C (?P<col>\d+)-?(?P<c_end>\d+)?\): (?P<message>.*)'
    tempfile_suffix = '-'
    default_type = highlight.WARNING
    comment_re = r'\s*%'

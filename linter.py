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

    """Provides an interface to mlint."""

    syntax = 'matlab'
    cmd = 'mlint @'
    executable = 'mlint'
    regex = r'L (?P<line>\d+) \(C (?P<col>\d+)-?(?P<c_end>\d+)?\): (?P<message>.*)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    default_type = highlight.WARNING
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*%'

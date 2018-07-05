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

import SublimeLinter
from SublimeLinter.lint import Linter, util

if getattr(SublimeLinter.lint, 'VERSION', 3) > 3:
    from SublimeLinter.lint import const
    WARNING = const.WARNING
else:
    from SublimeLinter.lint import highlight
    WARNING = highlight.WARNING

class Mlint(Linter):

    """Provides an interface to mlint, the standalone MATLAB linter"""

    syntax = 'matlab'
    cmd = ('mlint', '$file')
    regex = (r'L (?P<line>\d+) \(C (?P<col>\d+)-?(?P<c_end>\d+)?\)'
             r'((?P<error>: Parse error at [^:]*:)|(?P<warning>: ))'
             r'(?P<message>.*)')
    tempfile_suffix = '-'
    default_type = WARNING
    comment_re = r'\s*%'
    error_stream = util.STREAM_STDERR

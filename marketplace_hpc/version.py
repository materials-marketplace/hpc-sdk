#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module contains project version information.
"""

try:
    from dunamai import Version, get_version

    __version__ = Version.from_git().serialize()
except RuntimeError:
    __version__ = get_version("hpc-sdk").serialize()
except ImportError:
    __version__ = "v0.2.1"

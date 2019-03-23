#!/usr/bin/env python
import os
import public


@public.add
def pgrep(pattern):
    """return a list with process IDs which matches the selection criteria"""
    args = ["pgrep", str(pattern)]
    out = os.popen(" ".join(args)).read().strip()
    return list(map(int, out.splitlines()))

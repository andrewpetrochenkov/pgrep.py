#!/usr/bin/env python
import pgrep

pid = pgrep.pgrep("not-existing-process")
print(pid)

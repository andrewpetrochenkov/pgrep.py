<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/pgrep.svg?maxAge=3600)](https://pypi.org/project/pgrep/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/pgrep.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/pgrep.py/actions)

### Installation
```bash
$ [sudo] pip install pgrep
```

#### Examples
```python
>>> import pgrep
>>> pgrep.pgrep("Finder")
[322]

>>> pgrep.pgrep("bash")
[416, 434, 30681, 30918]

>>> pgrep.pgrep("not-existing-process")
[]
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
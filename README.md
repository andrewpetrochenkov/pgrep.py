<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/pgrep.svg?longCache=True)](https://pypi.org/project/pgrep/)
[![](https://img.shields.io/pypi/v/pgrep.svg?maxAge=3600)](https://pypi.org/project/pgrep/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/pgrep.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/pgrep.py/)

#### Installation
```bash
$ [sudo] pip install pgrep
```

#### Functions
function|`__doc__`
-|-
`pgrep.pgrep(pattern)` |return a list with process IDs which matches the selection criteria

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
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>
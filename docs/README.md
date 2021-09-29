# API JSON documentation

These files are provided to be processed by [`generator.py`](../generator.py)
in order to create a usable Python wrapper offline.
However, the most up to date wrapper will require reading the most recent
`api.json` file from the online [lbry-sdk](https://github.com/lbryio/lbry-sdk/tree/master/docs)
repository.

Nevertheless, if the `api.json` file in the repository contains errors
the produced wrapper will have syntax errors, and will not work.
In this case it's best to use the included `api.json` here.

## Current

Version 2.0 of `pybry` is from September 2021.
The format of the JSON file that it requires has changed since 2018.
The included [`api.json`](./api.json) file
is from commit c2113382 of the [lbry-sdk](https://github.com/lbryio/lbry-sdk/tree/c2113382/docs)
repository.

## Obsolete

Version 1.6.4 of `pybry` is from October 2018 (commit af86805a80).
The included [`api.json-1.6.4`](./api.json-1.6.4) file
is from commit c753a582 of the [lbry-sdk](https://github.com/lbryio/lbry-sdk/tree/c753a582/docs)
repository.

This file can no longer be processed by v2.0 of `generator.py`
as the information is organized in a different way.

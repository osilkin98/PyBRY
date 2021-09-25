# API JSON documentation

These files are provided to be processed by [`generator.py`](../generator.py)
in order to create a usable Python wrapper offline.
However, the most up to date wrapper will require reading the most recent
`api.json` file from the online [lbry-sdk](https://github.com/lbryio/lbry-sdk/tree/master/docs)
repository.

## Current

Version 2.0 of `pybry` is from September 2021.
The format of the JSON file that it requires has changed since 2018.
The included [`api.json`](./api.json) file
is from commit e1e76005 of the [lbry-sdk](https://github.com/lbryio/lbry-sdk/tree/e1e76005/docs)
repository.

This JSON file has an error in the information of the `file_list` command.
The argument `blobs_in_stream` has the incorrect name `blobs_in_stream<blobs_in_stream>`,
and thus `generator.py` produces an API wrapper with incorrect Python syntax.

Therefore, this [`api.json`](./api.json) file was manually edited
to fix this issue, and thus is not identical to the file
in the [lbry-sdk](https://github.com/lbryio/lbry-sdk/tree/e1e76005/docs)
repository.

Once an improved `api.json` is in the official repository, it will be copied
to this directory.

## Obsolete

Version 1.6.4 of `pybry` is from October 2018 (commit af86805a80).
The included [`api.json-1.6.4`](./api.json-1.6.4) file
is from commit c753a582 of the [lbry-sdk](https://github.com/lbryio/lbry-sdk/tree/c753a582/docs)
repository.

This file can no longer be processed by v2.0 of `generator.py`
as the information is organized in a different way.

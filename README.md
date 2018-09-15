# PyBry, a Python API Wrapper for lbry & lbrycrd

PyBry is a wrapper for the [lbry daemon](https://github.com/lbryio/lbry) and 
[lbrycrd daemon](https://github.com/lbryio/lbrycrd) API for Python 3.x

(Python 2 support will be added very soon)


## Usage
Import `LbryApi` or `LbrycrdApi` into your project and simply use the 
`call(method, params)` to interact with the respective API.

## Example:

```python
from lbry_api import LbryApi

lbry = LbryApi()

response = lbry.call("claim_list", {"name": "bellflower"})
```
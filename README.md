# PyBRY, a Python API Wrapper for lbry & lbrycrd

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build: Passing](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

PyBry is a wrapper for the [lbry daemon](https://github.com/lbryio/lbry) and 
[lbrycrd daemon](https://github.com/lbryio/lbrycrd) API for Python 3.x

(Python 2 support will be added very soon)

## Installation
```bash
# Simply clone the repository somewhere
$ git clone https://github.com/osilkin98/pybry

# Change directories into the newly created repository
$ cd PyBRY/

# Now you simply run the setup.py file:
$ python3 setup.py install
```

And you're done!


## Usage

Import `LbryApi` or `LbrycrdApi` from `pybry` into your project and simply use the 
`call(method, params)` to interact with the respective API.


For Normal Lbry:

```python
from pybry import LbryApi

# Initialize the API
lbry = LbryApi()

# Call the method you want as a str
response = lbry.call("claim_list", {"name": "bellflower"})
```

For Lbrycrd:
```python
from pybry import LbrycrdApi

# Provide the username and password
lbrycrd = LbrycrdApi("username", "password")

# Just specify the method and the parameters
response = lbrycrd.call("wallet_unlock", {"password", "wallet_password"})

```



For the 
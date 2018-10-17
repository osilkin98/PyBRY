# PyBRY, a Python API Wrapper for lbry & lbrycrd

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/b/osilkin98/pybry.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/b/osilkin98/pybry/context:python)

PyBry is a wrapper for the [lbry daemon](https://github.com/lbryio/lbry) and 
[lbrycrd daemon](https://github.com/lbryio/lbrycrd) API for Python 3.x

(Python 2 support will be added very soon)

## Installation

### Using pip

```bash
$ pip install pybry
```

### Manually Cloning the Repository

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
response = lbrycrd.call("wallet_unlock", {"wallet_username", "wallet_password"})

```
*Note: You have to have the `lbry-daemon` running in the background to use these, simply execute those and 
you'll be able to make requests efficiently.

## Future: Code Generation
Code generation for `lbryd_api` is a feature that is ready to be implemented,
 (in the [`generator.py`](pybry/_generator.py) file).
However the file itself cannot be used to generate working code due to to a couple of flaws in the actual
[documentation file](https://github.com/lbryio/lbry/blob/master/docs/api.json) as 
documented [here](https://github.com/lbryio/lbry/pull/1469). 

If you would like to use it so you can have
proper function names and parameters for your code, you may do so. Simply run 
`$ python setup.py build_py` and then delete all instances of `<amount>` and `<file_name>` found in 
your `lbryd_api.py` file. Then you're done!
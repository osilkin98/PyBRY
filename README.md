# PyBRY, a Python API wrapper for lbrynet and lbrycrd

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

PyBry is a Python 3 wrapper for the [lbrynet](https://github.com/lbryio/lbry-sdk) and
[lbrycrd](https://github.com/lbryio/lbrycrd) daemons from the LBRY project.
It allows calling the methods of these daemons inside Python programs.

## Installation

You must have the LBRY Desktop application or the `lbrynet` client.
Get them from [lbry.com/get](https://lbry.com/get).

The `lbrycrd` blockchain can be downloaded from the
[lbrycrd](https://github.com/lbryio/lbrycrd) repository.

### Cloning the repository

Clone the repository into a user-writeable directory:
```bash
git clone https://github.com/osilkin98/PyBRY
```

### Make

Change into the newly created repository, and run the `Makefile`:
```sh
cd PyBRY/
make
```

The generated API wrapper will be written to `pybry/lbryd_api.py`.

By default the API wrapper is created from the included `docs/api.json` file.
These are equivalent:
```sh
make
make build_local
```

To create the latest wrapper you must use the latest `api.json` directly
from the [lbry-sdk](https://github.com/lbryio/lbry-sdk/tree/master/docs)
repository. This can be done with a single instruction:
```sh
make build_online
```

However, if the online JSON file has errors, the generated wrapper
may also contain syntax errors, and it will not work
when used in a Python program.
In this case, clean the generated API, and use the local `api.json`
that is guaranteed to work:
```sh
make clean
make
```

Read the [docs/README.md](./docs) file for more information.

To use the new wrapper code, copy the [`pybry/`](./pybry) directory,
and place it inside a `site-packages` directory that is searched by Python.
This can be in the user's home directory,
```
/home/user/.local/lib/python3.8/site-packages/pybry
```

or in a system-wide directory:
```
/usr/local/lib/python3.8/dist-packages/pybry
/usr/lib/python3/dist-packages/pybry
```

You can also modify the `PYTHONPATH` environmental variable
to include the parent directory where `pybry` is located:
```sh
PYTHONPATH=/opt/git/PyBRY:$PYTHONPATH
```

### Setuptools

Insted of using the `Makefile`, we can use `setuptools` as well:
```
python3 setup.py build_local
python3 setup.py build_online
python3 setup.py clean
```

However, since `setup.py` imports `pybry`, and this imports
the existing `lbryd_api.py`, the entire `setup.py` may fail
on import if `lbryd_api.py` has syntax errors.
For this reason, using the `Makefile` is preferred.

### Older installation

There is a `pybry` package available in PyPI.
However, this corresponds to the 1.6.4 version, and thus it is not up to date.
```bash
pip install --user pybry
```

## Usage

### API for lbrynet

Make sure the `lbrynet` daemon is running either by launching
the full LBRY Desktop application, or by starting the console `lbrynet`
program.
```sh
lbrynet start
```

#### Using the generated wrapper

The wrapper generates all functions from the `lbrynet` documentation,
and produces documented Python code.

Import the library, initialize the main class, and then call its methods,
which have the same name and arguments as described in the documentation.
```py
import pybry
lbry = pybry.LbrydApi()
response = lbry.claim_search(name="LBRYPlaylists")
```

Since the code is properly documented, if you ask for its documentation
in an integrated development environment (IDE),
or if you go to read it for yourself, it'll appear like this:
```py
response = lbry.account_balance()

Return the balance of an account
Params:
account_id – If provided only the balance for this account will be given (Optional)
address – If provided only the balance for this address will be given (Optional)
include_unconfirmed – Include unconfirmed (Optional)
Returns:
(decimal) amount of lbry credits in wallet(decimal) amount of lbry credits in wallet
```

Note that at the moment the return information is not available,
as the API JSON files don't contain this information in a standardized way.

#### Calling the API manually

All the wrapper code does is make requests to the running `lbrynet` daemon.
Therefore, if there is no proper wrapper for a particular method
(because it was generated by an outdated `api.json`, for example),
a simple message can be sent to the daemon just like with using
the `requests` library or `curl`.
```py
method = "claim_search"
message = {"name": "LBRYPlaylists"}

response = lbry.call(method, message)
```

### API for lbrycrd

Initialize the daemon with a username and password
and send messages just like with using the `requests` library.
```py
import pybry
lbrycrd = pybry.LbrycrdApi("username", "password")

method = "wallet_unlock"
message = {"wallet_username", "wallet_password"}
response = lbrycrd.call(method, message)
```

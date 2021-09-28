"""Static constants that the code generator will use.

These constants will be used when generating the API wrappers,
and they will also be used inside the wrappers.
"""
import os

__version__ = "2.1.0"

# This is the URL for the online `lbrynet` API documentation
LBRY_API_RAW_JSON_URL = "https://raw.githubusercontent.com/lbryio/lbry/master/docs/api.json"

# At the moment there is no online `lbrycrd` API documentation
# LBRYCRD_API_RAW_JSON_URL = ""

# Input and output directories
TEMPLATE_DIR = "template"
PKG_DIR = NAME = "pybry"

# Template file and generated module.
# The template file will be read and should not be overwritten.
# The generated module will be created or overwritten.
LBRYD_BASE_FPATH = os.path.join(TEMPLATE_DIR, "_lbryd_api.py")
LBRYD_FPATH = os.path.join(PKG_DIR, "lbryd_api.py")

LBRYCRD_BASE_FPATH = os.path.join(TEMPLATE_DIR, "_lbrycrd_api.py")
LBRYCRD_FPATH = os.path.join(PKG_DIR, "lbrycrd_api.py")

# Variable used to map the data types in the API documentation
# for the generated docstrings in the written API wrapper.
DTYPE_MAPPING = {'list': "list",
                 'decimal': "float",
                 'float': "float",
                 'bool': "bool",
                 'int': "int",
                 'dict': "dict",
                 'str': "str",
                 'string': "str",
                 'str, list': "list",
                 'str or list': "list",
                 'date': "str"}

# Default address for the running `lbrynet` and `lbrycrd` daemons
LBRYD_SERVER_ADDRESS = "http://localhost:5279"
LBRYCRD_SERVER_ADDRESS = "http://localhost:9245"


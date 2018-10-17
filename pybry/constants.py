

# Defines server constants so they dont get altered by other files
LBRYD_SERVER_ADDRESS = "http://localhost:5279"
LBRYCRD_SERVER_ADDRESS = "http://localhost:9245"

# This is the URL for the lbryd API documentation
LBRY_API_RAW_JSON_URL = "https://raw.githubusercontent.com/lbryio/lbry/master/docs/api.json"

DTYPE_MAPPING = {'list': "list",
                 'decimal': "float",
                 'float': "float",
                 'bool': "bool",
                 'int': "int",
                 'dict': "dict",
                 'str': "str"}

# LBRYCRD documentation doesn't exist at least that I could find
# LBRYCRD_API_RAW_JSON_URL = ""


LBRYD_FPATH = "pybry/lbryd_api.py"

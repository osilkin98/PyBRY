"""Module to generate the API wrappers for lbrynet and lbrycrd.

This module can be executed directly or called from a building system
like `Makefile` or `setuptools`.
"""
import ast
import json
import os
import shutil
import sys
import urllib.request
import urllib.error
from pybry.constants import (LBRY_API_RAW_JSON_URL,
                             DTYPE_MAPPING,
                             __LBRYD_BASE_FPATH__,
                             LBRYD_FPATH)


def get_lbry_api_function_docs(url=LBRY_API_RAW_JSON_URL, doc=None):
    """Scrapes the given input in JSON format to obtain the lbrynet API.

    :param str url: URL to the documentation we need to obtain,
     pybry.constants.LBRY_API_RAW_JSON_URL by default
    :return: List of functions retrieved from the `url` given
    :rtype: list
    """
    try:
        if doc:
            with open(doc, "r") as api_file:
                contents = api_file.read()
        else:
            # Grab the page content
            docs_page = urllib.request.urlopen(url)

            # Read the contents of the actual url we grabbed and decode them into UTF-8
            contents = docs_page.read().decode("utf-8")

        # Return the contents loaded as JSON
        return json.loads(contents)

        # If we get an exception, simply exit
    except urllib.error.URLError as err:
        print(f"Cannot open URL for reading; {err} '{url}'")
    except (FileNotFoundError, PermissionError) as err:
        print(f"Cannot open file for reading; {err}")
    except Exception as err:
        print(f"{err}, url='{url}', doc='{doc}'")

    return []


def generate_method_definition(func):
    """Generates the body for the given function.

    :param dict func: dict of a JSON-Formatted function as defined by the API docs
    :return: A String containing the definition for the function as it should be written in code
    :rtype: str
    """
    indent = 4

    # initial definition
    method_definition = (" " * indent) + "def " + func["name"]

    # Here we just create a queue and put all the parameters
    # into the queue in the order that they were given,
    params_required = [
        param for param in func["arguments"] if param["is_required"]
    ]
    params_optional = [
        param for param in func["arguments"]
        if not param["is_required"]
    ]

    # Open the parameter definitions
    method_definition += "(self, "

    for param in params_required:
        # Put the parameter into the queue

        method_definition += param["name"]
        method_definition += ", "

    for param in params_optional:
        method_definition += param["name"]

        # Default methods not required
        method_definition += "=None, "

    # Peel off the final ", " and close off the parameter definition
    method_definition = method_definition.rstrip(", ") + "):\n"

    indent += 4

    # re-indent
    method_definition += " " * indent

    # Begin with description.

    method_definition += '"""' + func["description"]

    # re-indent
    method_definition += "\n\n" + " " * indent

    # Go through each parameter and insert description & type hint
    for param in params_required + params_optional:
        # Add the type
        method_definition += ":param " + DTYPE_MAPPING[param["type"].lower()]

        # Add the name
        method_definition += " " + param["name"] + ": "

        # Add the description
        method_definition += param["description"]

        # Add optionality & reindent
        method_definition += "\n" if param[
            "is_required"] else " (Optional)\n"

        method_definition += " " * indent
    # Do not parse the returns because it doesn't work correctly at the moment
#    open_index = func["returns"].find('(')
#    close_index = func["returns"].find(
#        ')', (open_index if open_index > -1 else 0))
#
#    func["returns"] = func["returns"].replace("\t", " " * 4)
#    return_string = func["returns"].replace("\n", "")
#
#    if open_index < close_index and func["returns"][
#                                    open_index + 1:close_index] in DTYPE_MAPPING:
#        method_definition += ":rtype: " + DTYPE_MAPPING[
#            func["returns"][open_index + 1:close_index]]
#
#        func["returns"] = func["returns"].replace(
#            func["returns"][open_index:close_index + 1], "")
#
#        method_definition += "\n" + " " * indent
#
#    method_definition += ":return: " + return_string
#
#    for i in range(0, len(return_string) + 1, 80 - (indent + 2)):
#        method_definition += return_string[i:i + (
#                80 - (indent + 2))] + "\n" + " " * indent

    # Close it off & reindent
    method_definition += '"""' + "\n" + " " * indent

    # Create the params map
    params_map = "__params_map = {"

    # Save the indent
    params_indent, num_params = len(
        params_map), len(params_required) + len(params_optional)

    # Append the map to the method_definition
    method_definition += params_map

    # Go through the required parameters first
    for i, param in enumerate(params_required + params_optional):

        # append the methods to the map
        method_definition += "'" + param["name"] + "': " + param["name"]

        if not param["is_required"]:
            method_definition + " if " + param[
                "name"] + "is not None else None"

        # add commas or ending bracket if needed & reindent correctly
        method_definition += ",\n" + " " * indent + ' ' * params_indent if i + 1 < num_params else ""

    method_definition += '}\n\n' + ' ' * indent

    method_definition += "return self.make_request(SERVER_ADDRESS, '" + func["name"] + "', " \
                         + params_map.rstrip(" = {") + ", timeout=self.timeout)\n\n"

    return method_definition


def generate_lbryd_wrapper(url=LBRY_API_RAW_JSON_URL,
                           doc=None,
                           read_file=__LBRYD_BASE_FPATH__,
                           write_file=LBRYD_FPATH):
    """Generates the wrapper for the lbrynet daemon.

    :param str url: URL to the documentation we need to obtain,
     pybry.constants.LBRY_API_RAW_JSON_URL by default
    :param str read_file: This is the path to the file from which we will be reading
    :param str write_file: Path from project root to the file we'll be writing to.
    """
    print(80 * "-")

    if doc:
        sections = get_lbry_api_function_docs(doc=doc)
        inpt = doc
    else:
        sections = get_lbry_api_function_docs(url=url)
        inpt = url

    if not sections:
        print("Empty information; wrapper module not written.")
        return True

    print("Input JSON:", inpt)

    # Open the actual file for appending
    with open(write_file, 'w') as lbry_file:
        docstring = ['"""',
                     'LBRY daemon wrapper in Python. Import it and initialize the main class.',
                     '',
                     'This file was generated at build time using the `generator` module.',
                     'You may edit it but do so with caution.',
                     'If this file contains syntax errors, check the input file',
                     'for badly formated fields.',
                     f'Input JSON: {inpt}',
                     '"""',
                     '']

        docstring = "\n".join(docstring)
        lbry_file.write(docstring)

        with open(read_file, 'r') as template:
            header = template.read()

        lbry_file.write(header)

        # Iterate through all the functions we retrieved
        # and write them to the file
        for section in sections:
            commands = sections[section]["commands"]

            for command in commands:
                method_definition = generate_method_definition(command)
                lbry_file.write(method_definition)

    print("Generated 'lbrynet' API wrapper:", write_file)
    with open(write_file) as lbry_file:
        source = lbry_file.read()

    parsed = True
    try:
        result = ast.parse(source, filename=write_file)
    except SyntaxError as err:
        print("The resulting file has syntax errors. Look at the error line for clues.")
        print("Error:", err)
        print()
        print("The problem is usually in the input JSON file; it may contain badly formatted fields.")
        print("Input:", inpt)
        print()
        parsed = False

    if parsed:
        try:
            from yapf.yapflib.yapf_api import FormatFile
            FormatFile(write_file, in_place=True)
        except ImportError:
            print()
            print("[Warning]: 'yapf' could not be imported, so the generated code will not be formatted")

    return None


def generate_basic_modules(template_dir="pybry", out_dir="pybry"):
    """Generate the static modules in the final package directory.

    These are simply copied over from the template directory.
    """
    print(80 * "-")
    print("Package:", out_dir)

    basic_modules = ["__init__.py",
                     "constants.py",
                     "base_api.py",
                     "LBRYException.py"]

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    installed = []
    for module in basic_modules:
        in_file = os.path.join(template_dir, module)

        if module == "__init__.py":
            module = "__init__.py"

        out_file = os.path.join(out_dir, module)
        try:
            shutil.copy(in_file, out_file)
        except (FileNotFoundError, shutil.SameFileError) as err:
            print(err)
        installed.append("- " + out_file)

    print("Basic modules:")
    print("\n".join(installed))


def main(argv=None):
    if argv and isinstance(argv, (list, tuple)):
        doc = argv[1] if len(argv) > 1 else None
    else:
        doc = None
    generate_basic_modules()
    generate_lbryd_wrapper(doc=doc)


if __name__ == "__main__":
    sys.exit(main(sys.argv))


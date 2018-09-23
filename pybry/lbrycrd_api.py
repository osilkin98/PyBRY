from pybry.constants import LBRYCRD_SERVER_ADDRESS as SERVER_ADDRESS
from pybry.base_api import BaseApi


class LbrycrdApi(BaseApi):

    def __init__(self, username, password, timeout=600):
        """

        :param str username: Username for lbrycrd login
        :param str password: Password for lbrycrd login
        :param float timeout: Number of seconds before we give up on waiting for server to respond
        """

        self.basic_auth = (username, password)
        self.timeout = timeout

    def call(self, method, params=None):
        """

        :param str method: Method to call from lbrycrd. To view the full list of methods, run ./lbrycrd-cli help,
         or ./lbrycrd-cli [command_name] help for information on a specific command
         https://lbryio.github.io/lbry/cli/
        :param dict params: Parameters to give the method selected
        :raises LBRYException: If the request returns an error when calling the API
        :return: A Python `dict` object containing the data requested from the API
        :rtype: dict
        """

        return self.make_request(SERVER_ADDRESS, method, params, self.basic_auth, self.timeout)

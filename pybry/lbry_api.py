from pybry.base_api import BaseApi
from pybry.constants import LBRY_SERVER_ADDRESS


class LbryApi(BaseApi):

    def __init__(self, timeout=600):
        """
        :param float timeout: The number of seconds to wait for a connection until we time out
        """
        self.timeout = timeout

    def call(self, method, params=None):
        """ Makes a Call to the LBRY API

        :param str method: Method to call from the LBRY API. See the full list of methods at
         https://lbryio.github.io/lbry/cli/
        :param dict params: Parameters to give the method selected
        :raises LBRYException: If the request returns an error when calling the API
        :return: A Python `dict` object containing the data requested from the API
        :rtype: dict
        """

        params = [] if params is None else params

        return self.make_request(LBRY_SERVER_ADDRESS, method, params, timeout=self.timeout)

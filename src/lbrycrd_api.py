from src.addresses import LBRYCRD_SERVER_ADDRESS
from src.base_api import BaseApi


class LbrycrdApi(BaseApi):

    def __init__(self, username, password, timeout=600):
        """

        :param str username: Username for lbrycrd login
        :param str password: Password for lbrycrd login
        :param float timeout: Number of seconds before we give up on waiting for server to respond
        """


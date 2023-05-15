import requests

from config import MCHS_SERVER_ADDRESS, MCHS_REQUEST_HEADERS, MCHS_SERVER_ENABLED, MCHS_REQUEST_METHOD


class MCHS:

    @staticmethod
    def send_fire(json_body):
        if not MCHS_SERVER_ENABLED: return

        requests.request(
            method=MCHS_REQUEST_METHOD,
            json=json_body,
            url=MCHS_SERVER_ADDRESS,
            headers=MCHS_REQUEST_HEADERS
        )

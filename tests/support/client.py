import os
import requests
from hamcrest import assert_that, is_


class Client:

    def __init__(self):
        self.port = os.getenv("PORT", 8080)
        self.endpoint = os.getenv("ENDPOINT", 'localhost')
        self.root = f'http://{self.endpoint}:{self.port}'

    def is_healthy(self, headers=None):
        response = requests.get(f"{self.root}/health", verify=False, headers=headers)
        assert_that(response.status_code, is_(200))
    
import pytest
from base_case import BaseCase

class TestLogin(BaseCase):
    def test_login(self, registration_page):
        return
import pytest
from base_case import BaseCase

class TestCampaigns(BaseCase):
    def test_create_campaign(self, campaigns_page):
        campaigns_page.create_campaign()
        
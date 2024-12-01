import pytest
from base_case import BaseCase

class TestCabinet(BaseCase):
    def test_learn_through_video(self, cabinet_page):
        cabinet_page.learn_through_video()
        cabinet_page.assert_video_opened()
        cabinet_page.close_video()

    def test_learn_through_course(self, cabinet_page):
        cabinet_page.learn_through_course()
        cabinet_page.assert_course_page_opened()
        cabinet_page.close_course_page()

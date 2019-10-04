from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from externalmodules.staginglogin import staging_login
from externalmodules.driversetup import close_driver

import time
import re

class PythonOrg(object):

    def __init__(self):
        self.driver = staging_login()

    def main_page(self):

        self.driver.get("https://www.python.org")
        assert "python.org" in self.driver.current_url, "[ERROR]: Python is not in URL, seeing: '{}'".format(self.driver.current_url)

    def search_page(self):
        self.main_page()

        search_page = self.driver.find_element_by_id("id-search-field")
        submit = self.driver.find_element_by_id("submit")
        SEARCH_TEXT = "python"
        search_page.send_keys(SEARCH_TEXT)
        submit.click()

    def verify_search_results(self):
        self.search_page()

        search_results = self.driver.find_element_by_css_selector("ul.list-recent-events.menu")
        search_results_list = search_results.find_elements_by_tag_name("li")

        assert len(search_results_list) < 0, "[ERROR]:Not seeing any results"


page = PythonOrg()
page.main_page()
page.search_page()
page.verify_search_results()

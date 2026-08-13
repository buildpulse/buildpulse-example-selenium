import os
import unittest

import xmlrunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ExampleTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        chrome_bin = os.environ.get("CHROME_BIN")
        if chrome_bin:
            options.binary_location = chrome_bin
        self.driver = webdriver.Chrome(options=options)

    def test_page_title(self):
        self.driver.get("http://example.com")
        self.assertIn("Example Domain", self.driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./test-reports"))

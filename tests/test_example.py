import unittest
from selenium import webdriver
import chromedriver_autoinstaller
import xmlrunner

chromedriver_autoinstaller.install()

class ExampleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_page_title(self):
        self.driver.get("http://example.com")
        self.assertIn("Example Domain", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='./test-reports'))


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://almtoolbox.com/gitlab.php")
        #self.assertIn("GitLab", driver.title)
        #elem = driver.find_element_by_id("gsc-i-id1")
        #elem.send_keys("software")
        #elem.send_keys(Keys.RETURN)
        #assert "No results found." not in driver.page_source

        # Check all links
        links = driver.find_elements_by_tag_name("a")
        for elem in links:
            print ("elem = ", elem.get_attribute('textContent'))



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

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
        for link in links:
            href = link.get_attribute('href')
            print ("Link text: ", link.get_attribute('textContent'), ", href: ", href)
            if (href is not None and href != "" and "javascript" not in href and "mailto" not in href):
                r = requests.head(href)
                print("Status: ", r.status_code)

        # Check iframes
        iframes = driver.find_elements_by_tag_name("iframe")
        for iframe in iframes:
            src = iframe.get_attribute('src')
            print ("iframe src: ", src)
            if (src is not None and src != "" and "youtube"  in src):
                driver.switch_to.frame(iframe)
                print("Successfully switched to the iframe")
                driver.switch_to.default_content()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
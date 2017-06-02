#pylint: skip-file

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DemoMaharaOrgLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_in_demo_mahara_org(self):
        driver = self.driver
        driver.get("http://demo.mahara.org/")
        self.assertIn("Home - Mahara", driver.title)
        username = driver.find_element_by_id("login_login_username")
        username.send_keys("student2")
        password=driver.find_element_by_id("login_login_password")
        password.send_keys("Testing1")
        loginbutton=driver.find_element_by_id("login_submit")
        loginbutton.click()
        self.assertTrue(driver.find_element_by_link_text("Logout"),"Logout link")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
import sys
import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))

from login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        chrome_service = Service("C:\\WebDriver\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get("https://www.saucedemo.com/")

        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.login("standard_user", "secret_sauce")
        self.assertTrue(self.login_page.is_login_successful(), "Login falhou!")

    def tearDown(self):
        #Pressionar enter para fechar o navegador
        input("Pressione Enter para fechar o navegador...") 
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

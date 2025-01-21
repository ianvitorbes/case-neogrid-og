import sys
import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Adicionando a pasta 'pages' ao sys.path para garantir a importação das páginas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))
from login_page import LoginPage
from product_page import ProductPage

class TestSortProducts(unittest.TestCase):
    def setUp(self):
        chrome_service = Service("C:\\WebDriver\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get("https://www.saucedemo.com/")

        # Inicializando
        self.login_page = LoginPage(self.driver)
        self.product_page = ProductPage(self.driver)

        # Login no sistema
        self.login_page.login("standard_user", "secret_sauce")

    def test_sort_products_by_price_low_to_high(self):
        # Critério de ordenação (Preço do mais baixo para o mais alto)"
        sort_dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        select = Select(sort_dropdown)
        select.select_by_value("lohi")

        # Verificando se os produtos estão ordenados
        product_prices_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        product_prices = [float(price.text.replace("$", "")) for price in product_prices_elements]

        # Validar se a lista está em ordem crescente
        assert product_prices == sorted(product_prices), "Os produtos não estão ordenados por preço corretamente!"
        
        print("Os produtos estão ordenados corretamente por preço: do mais baixo para o mais alto.")

    def tearDown(self):
        input("Pressione Enter para fechar o navegador...")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

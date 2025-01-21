import sys
import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Adicionando a pasta 'pages' ao sys.path para garantir a importação do ProductPage
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))
from product_page import ProductPage

class TestRemoveProductFromCart(unittest.TestCase):
    def setUp(self):
        chrome_service = Service("C:\\WebDriver\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get("https://www.saucedemo.com/")  # Acesso à página de login

        # Carregando página de produtos
        self.product_page = ProductPage(self.driver)

        # Login no sistema
        self.product_page.login("standard_user", "secret_sauce")

    def test_remove_product_from_cart(self):
        # Adiciona um produto ao carrinho e verifica se realmente foi adicionado
        self.product_page.add_product_to_cart()
        assert self.product_page.is_product_added(), "Produto não foi adicionado ao carrinho!"

        # Vai até o carrinho
        self.product_page.navigate_to_cart()

        # Delay pra tornar a remoção visivel (meramente por questões visuais de teste)
        time.sleep(2)

        # Remove o produto do carrinho
        self.product_page.remove_product_from_cart()

        # Delay pra tornar a remoção visivel (meramente por questões visuais de teste)
        time.sleep(2)  

        # Verifica se realmente o produto foi removido
        cart_count = self.product_page.get_cart_item_count()
        assert cart_count == "0", f"Carrinho não está vazio! Contagem: {cart_count}"

        # Mensagem indicando que o produto foi removido do carrinho
        print("Produto removido do carrinho!")

    def tearDown(self):
        # Espera para poder ver o resultado do teste
        input("Pressione Enter para fechar o navegador...")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

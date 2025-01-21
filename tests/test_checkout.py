import sys
import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))
from login_page import LoginPage
from product_page import ProductPage

class TestCheckout(unittest.TestCase):
    def setUp(self):
        chrome_service = Service("C:\\WebDriver\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get("https://www.saucedemo.com/")

        # Inicializando as páginas
        self.login_page = LoginPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def test_checkout_flow(self):
        # Fazendo login
        self.login_page.login("standard_user", "secret_sauce")
        self.assertTrue(self.login_page.is_login_successful(), "Login falhou!")

        # Acessando a página de produtos
        self.assertTrue(self.product_page.is_product_page(), "Página de produtos não carregada!")

        # Adicionando produto ao carrinho
        self.product_page.add_product_to_cart()
        self.assertTrue(self.product_page.is_product_added(), "Produto não foi adicionado ao carrinho!")

        # Navegando até o carrinho e fazendo checkout
        self.product_page.navigate_to_cart()
        self.product_page.start_checkout()

        # Delay para o preenchimento dos dados do usuário
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.product_page.first_name_field)
        )
        first_name_field.send_keys("John")
        last_name_field = self.driver.find_element(*self.product_page.last_name_field)
        last_name_field.send_keys("Doe")

        # Delay para o campo do CEP
        postal_code_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.product_page.zip_code_field)
        )
        postal_code_field.send_keys("12345")

        # Seguindo com o preenchimento dos dados
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.product_page.continue_button)
        )
        continue_button.click()

        # Aguardando até a página de confirmação da compra aparecer
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.product_page.finish_button)
        )

        # Finalizando a compra
        finish_button = self.driver.find_element(*self.product_page.finish_button)
        finish_button.click()

        # Aguardar até a URL conter "checkout-complete" (confirmando a finalização do pedido)
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("checkout-complete")
        )

        # Verificando se a compra foi concluída com sucesso
        self.assertTrue(self.product_page.is_checkout_complete(), "Compra não concluída com sucesso!")

        print("Compra finalizada com sucesso!")

    def tearDown(self):
        # Espera para poder ver o resultado do teste
        input("Pressione Enter para fechar o navegador...")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
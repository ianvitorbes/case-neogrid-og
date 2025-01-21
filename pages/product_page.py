# pages/product_page.py
from selenium.webdriver.common.by import By
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = "Swag Labs"  # Título da página que aparece após login bem-sucedido

        # Elementos da página de produto
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")  # Botão "Add to Cart"
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")  # Badge de itens no carrinho
    
    # Método para verificar se o usuário está na página de produtos
    def is_product_page(self):
        return self.page_title in self.driver.title
    
    # Método para adicionar um produto ao carrinho
    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    # Método para obter o número de itens no carrinho
    def get_cart_item_count(self):
        return self.driver.find_element(*self.cart_badge).text

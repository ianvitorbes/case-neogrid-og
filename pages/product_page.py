from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = "Swag Labs"  # Título da página que aparece após login bem-sucedido

        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")  # Botão "Add to Cart"
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")  # Badge de itens no carrinho

    def is_product_page(self):
        """
        Verifica se a página de produtos foi carregada corretamente, baseado no título da página.
        """
        WebDriverWait(self.driver, 10).until(
            EC.title_contains(self.page_title)
        )
        return True

    def add_product_to_cart(self):
        """
        Adiciona um produto ao carrinho.
        """
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )
        add_to_cart_button.click()

    def get_cart_item_count(self):
        """
        Retorna o número de itens no carrinho.
        """
        try:
            cart_count = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.cart_badge)
            )
            return cart_count.text
        except:
            return "0"  # Caso não haja itens no carrinho, retorna 0

    def is_product_added(self):
        """
        Verifica se um produto foi adicionado ao carrinho.
        Retorna True se o número de itens no carrinho for maior que 0.
        """
        return int(self.get_cart_item_count()) > 0
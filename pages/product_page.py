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

        # Elementos da página
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def login(self, username, password):

        # Fazendo login com os dados fornecidos
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_field))
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_product_page(self):
        # Verificação de login através do titulo da página
        WebDriverWait(self.driver, 10).until(
            EC.title_contains(self.page_title)
        )
        return True

    def add_product_to_cart(self):
        # Adicionando produto ao carrinho
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )
        add_to_cart_button.click()

    def get_cart_item_count(self):
        # Retornando numero de itens do carrinho para fazer a verificação
        try:
            cart_count = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.cart_badge)
            )
            return cart_count.text
        except:
            return "0"  # Caso não haja itens no carrinho, retorna 0

    def is_product_added(self):
        # Verificando se o item foi realmente adicionado ao carrinho
        return int(self.get_cart_item_count()) > 0

    def navigate_to_cart(self):
       # Navegando ate o carrinho de compras
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_button.click()

    def remove_product_from_cart(self):
        # Remoção de produto do carrinho
        remove_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
        )
        remove_button.click()

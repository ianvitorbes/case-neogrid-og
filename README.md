**Case de Testes Neogrid**

Criei um projeto seguindo os padrões do Page Object Model (POM), que contém testes automatizados utilizando Selenium WebDriver para o site Sauce Demo. O projeto abrange funcionalidades como login, adição de produtos ao carrinho, checkout, remoção de produtos do carrinho e ordenação de produtos.

## Padrões do Projeto

O projeto segue os padrões do Page Object Model (POM), onde cada página do site é representada por uma classe que encapsula seus elementos e ações.

## Pré-requisitos

Antes de rodar os testes, é necessário ter os seguintes pré-requisitos instalados:

Python 3.x: A versão mais recente do Python 3.

Pip: Gerenciador de pacotes do Python.

Google Chrome: Navegador para execução dos testes.

ChromeDriver: Driver para interação com o Chrome, compatível com a versão do seu navegador.

### Instalação do ChromeDriver
1. Baixe o [ChromeDriver](https://sites.google.com/chromium.org/driver/) adequado para sua versão do Google Chrome.
2. Coloque o ChromeDriver em um diretório de sua escolha (por exemplo, C:\WebDriver\chromedriver.exe), ou altere o caminho no código de teste para o local onde o arquivo foi salvo

### Instalação de dependências

Instale as dependências do projeto com o seguinte comando:
pip install -r requirements.txt

## Executando os Testes

Os testes estão organizados em arquivos separados, de modo que você pode executar testes específicos de forma independente. Para rodar um teste, utilize o comando abaixo no terminal:

1. **Teste de Login:**
python tests/test_login.py

2. **Teste de Adicionar Produto ao Carrinho:**
python tests/test_add_to_cart.py

3. **Teste de Remover Produto do Carrinho:**
python tests/test_remove_product_from_cart.py

4. **Teste de Realizar Checkout:**
python tests/test_checkout.py

5. **Teste de Ordenação de Produtos:**
python tests/test_sort_products.py   


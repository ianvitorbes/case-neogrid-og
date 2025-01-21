Criei um segundo projeto seguindo os padrões (Page Object Model). Não utilizarei mais o primeiro, pois não estava no padrão POM de testes.

Case de Testes Neogrid

Este projeto contém testes automatizados utilizando Selenium WebDriver para o site **Sauce Demo**. Os testes abordam funcionalidades como login, adição de produtos ao carrinho, checkout, e remoção de produtos do carrinho.

## Pré-requisitos

Antes de rodar os testes, certifique-se de ter os seguintes pré-requisitos instalados:

- Python 3.x
- Pip
- Google Chrome
- ChromeDriver compatível com sua versão do Chrome

### Instalação do ChromeDriver
1. Baixe o [ChromeDriver](https://sites.google.com/chromium.org/driver/) adequado para sua versão do Google Chrome.
2. Coloque o ChromeDriver em um diretório de sua escolha (exemplo: `C:\WebDriver\chromedriver.exe`) ou configure o caminho diretamente no código de teste.

### Instalação de dependências
Instale as dependências do projeto com o seguinte comando:
- pip install -r requirements.txt

Executando os Testes
Os testes estão organizados em arquivos separados. Para executar um teste específico, use o seguinte comando:

1. Teste de Login:
python tests/test_login.py

2. Teste de Adicionar Produto ao Carrinho:
python tests/test_add_to_cart.py

3. Teste de Remover Produto do Carrinho:
python tests/test_remove_product_from_cart.py

4. Teste de Realizar Checkout:
python tests/test_checkout.py

5. Teste de Ordenação de Produtos:
   


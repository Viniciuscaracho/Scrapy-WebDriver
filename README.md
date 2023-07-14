# Documentação do Projeto - Web Scraping com Scrapy e Selenium

Este projeto consiste em um código Python que realiza web scraping do site Procfy.io para extrair informações do saldo bancário. O código utiliza as bibliotecas Scrapy e Selenium para automatizar o processo de coleta de dados.

## Funcionalidades

- Acessa o site Procfy.io e realiza login usando Selenium.
- Extrai informações do saldo bancário da página inicial do Procfy.io.
- Armazena os dados extraídos em um arquivo CSV.

## Requisitos

- Python 3.x
- Bibliotecas Python: Scrapy, Selenium, scrapy_splash, csv, time

## Configuração

1. Certifique-se de ter o Python 3.x instalado em sua máquina.

2. Instale as bibliotecas necessárias executando o seguinte comando:
   ```
   pip install scrapy selenium scrapy_splash
   ```

3. Baixe o arquivo `chromedriver` adequado para o seu sistema operacional e certifique-se de que esteja disponível no PATH do sistema.

4. Abra o arquivo `ProcspiderSpider.py` e localize a seção de configuração no método `setup_selenium()`.

5. No método `setup_selenium()`, substitua `'/caminho/para/o/chromedriver'` pelo caminho completo para o arquivo `chromedriver` em sua máquina.

6. No mesmo método, substitua `'e-mail'` e `'senha'` pelas suas credenciais de login no Procfy.io.

## Executando o Código

1. Abra um terminal e navegue até o diretório do projeto.

2. Execute o seguinte comando para iniciar o web scraping:
   ```
   python ProcspiderSpider.py
   ```

3. O código começará a extrair os dados do saldo bancário do site Procfy.io e armazená-los em um arquivo chamado `file.csv` no mesmo diretório.

## Personalização

- Para extrair informações diferentes ou navegar em outras páginas do site, você pode modificar o código no método `parse()` do arquivo `ProcspiderSpider.py`. Lembre-se de ajustar a lógica de extração e o formato de armazenamento de acordo com suas necessidades.

- Você também pode personalizar a estrutura do arquivo CSV, incluindo ou removendo campos no método `export_to_csv()`.

## Observações

- Certifique-se de que está agindo em conformidade com as políticas de uso do site Procfy.io e com as leis de proteção de dados aplicáveis. O web scraping inadequado pode ser considerado uma violação de privacidade ou uma violação dos termos de serviço de um site.

- Este projeto é fornecido apenas como exemplo educacional e não deve ser usado para fins maliciosos ou ilegais.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções ou novos recursos para este projeto. Basta enviar um pull request no repositório do GitHub.

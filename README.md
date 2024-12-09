# Reading RPI magazine

Este repositório contém um script em Python que automatiza a análise de revistas do INPI (RPI - Revista da Propriedade Industrial). Ele identifica casos de **indeferimento de pedidos de registro de marcas** e os organiza em um arquivo Excel para facilitar o acompanhamento e a tomada de decisão.

## Funcionalidades

- Lê e processa arquivos da RPI no formato `.xml`.
- Filtra e identifica registros de marca com status de indeferimento.
- Exporta os resultados em formato `.xlsx`.

## Requisitos

Antes de executar o script, certifique-se de que o ambiente de desenvolvimento está configurado com os seguintes requisitos:

- Python 3.8 ou superior
- Bibliotecas Python:
  - `pandas`
  - `openpyxl`
  - `xml.etree.ElementTree` *(para manipulação do arquivo .xml)*

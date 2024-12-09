# RPI Mark Indecision Analyzer

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

Instale as dependências com o comando:

```bash
pip install -r requirements.txt
```

## Como Usar

1. **Obtenha a RPI**  
   Faça o download da revista RPI no site do INPI ([https://www.gov.br/inpi](https://www.gov.br/inpi)) no formato `.xml`.

2. **Prepare o Arquivo**  
   Certifique-se de que o arquivo está no formato correto e salve-o no diretório do script.

3. **Execute o Script**  
   Utilize o terminal para rodar o script. Exemplo:

   ```bash
   python rpi_analyzer.py
   ```

4. **Confira os Resultados**  
   O script gera um arquivo `.xlsx` contendo todos os casos de indeferimento identificados. O arquivo será salvo no diretório `output/`.

## Estrutura do Projeto

```
📂 RPI-Mark-Indecision-Analyzer
├── rpi_analyzer.py          # Script principal
├── requirements.txt         # Dependências do projeto
├── README.md                # Documentação do repositório
└── output/
    └── indeferimentos.xlsx  # Arquivo gerado com os resultados (após execução)
```

## Contribuindo

Contribuições são bem-vindas! Caso encontre problemas ou deseje adicionar melhorias, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Consulte o arquivo `LICENSE` para mais detalhes.

## Contato

Se você tiver dúvidas ou sugestões, entre em contato:

- **Autor:** Guilherme Matheus
- **LinkedIn:** [Guilherme](https://www.linkedin.com/in/gmmoraissouza/))
- **E-mail:** [gmmoraissouza10@gmail.com](mailto:gmmoraissouza10@gmail.com)

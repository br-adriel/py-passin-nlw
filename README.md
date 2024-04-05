# Pass In API

Backend para aplicação de gestão de participantes desenvolvida durante o
acompanhamento do evento Next Level Week organizado pela empresa Rocketseat em
Abril de 2024.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## Executando o projeto localmente

1. Clone o repositório e entre na pasta do projeto

    ```bash
    git clone git@github.com:br-adriel/py-passin-nlw.git
    ```

    ```bash
    cd py-passin-nlw
    ```

2. Crie um ambiente virtual python e instale as dependências do projeto

    - Linux

        ```bash
        python3 -m venv .venv
        ```

        ```bash
        source .venv/bin/activate
        ```

        ```bash
        pip install -r requirements.txt
        ```

    - Windows

        ```powershell
        py -m venv .venv
        ```

        ```powershell
        .venv\Scripts\activate
        ```

        ```powershell
        pip install -r requirements.txt
        ```

3. Crie um arquivo vazio chamado `storage.db` na raiz do projeto para o banco
de dados

    - Linux

        ```bash
        touch storage.db
        ```

4. Utilize alguma ferramenta como o [DBeaver](https://dbeaver.io/) para executar
o arquivo `schema.sql` da pasta `database`

5. Inicie o servidor de desenvolvimento

    - Linux

        ```bash
        python3 app.py
        ```

    - Windows

        ```powershell
        py app.py
        ```

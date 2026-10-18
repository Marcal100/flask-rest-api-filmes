# API REST de Filmes

API REST desenvolvida em Python com Flask para praticar desenvolvimento backend, criação de endpoints HTTP e manipulação de dados em JSON.

## Funcionalidades

- Listar todos os filmes.
- Consultar um filme pelo ID.
- Cadastrar filmes.
- Atualizar filmes.
- Excluir filmes.
- Validar os dados recebidos nas requisições.

## Tecnologias

- Python
- Flask
- REST API
- JSON
- Postman

## Como executar

1. Clone ou baixe o repositório.
2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o arquivo Python principal:

   ```bash
   python api-rest.py
   ```

4. Acesse a API em `http://127.0.0.1:5000`.

> Se o arquivo principal tiver outro nome, substitua `api-rest.py` pelo nome correto.

## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/filmes` | Lista todos os filmes |
| GET | `/filmes/<id>` | Consulta um filme |
| POST | `/filmes` | Cadastra um filme |
| PUT | `/filmes/<id>` | Atualiza um filme |
| DELETE | `/filmes/<id>` | Exclui um filme |

## Observação

Os dados são armazenados em memória e são reiniciados quando a aplicação é encerrada. Esta versão não utiliza banco de dados.
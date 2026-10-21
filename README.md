# Laboratório de Segurança em API REST com Flask

## Sobre o projeto

Este projeto demonstra a análise e o aprimoramento da segurança de uma API REST desenvolvida com Python e Flask. O laboratório foi realizado em ambiente local, utilizando o Postman para testar os endpoints e validar as respostas HTTP.

## Objetivos

- Implementar operações CRUD para gerenciamento de filmes.
- Validar os dados recebidos pela API.
- Identificar riscos relacionados à ausência de autenticação.
- Implementar proteção por chave de API nas operações de escrita.
- Validar o comportamento da aplicação por meio de testes HTTP.

## Tecnologias utilizadas

- Python
- Flask
- API REST
- Postman
- Git e GitHub

## Endpoints

| Método | Endpoint | Descrição | Proteção |
|---|---|---|---|
| GET | `/filmes` | Lista os filmes | Pública no laboratório |
| GET | `/filmes/<id>` | Consulta um filme | Pública no laboratório |
| POST | `/filmes` | Cadastra um filme | Chave de API |
| PUT | `/filmes/<id>` | Atualiza um filme | Chave de API |
| DELETE | `/filmes/<id>` | Exclui um filme | Chave de API |

## Análise de segurança

Durante os testes, foi identificada a ausência de autenticação nas operações de cadastro, atualização e exclusão. Inicialmente, foi possível executar uma exclusão sem fornecer credenciais.

Como medida de mitigação, foi implementado um decorador Flask que verifica a presença de uma chave de API no cabeçalho `X-API-Key`.

Requisições sem uma chave válida são rejeitadas com HTTP 401. Requisições autorizadas podem prosseguir para a lógica da rota, que então valida os dados e executa a operação solicitada.

## Evidências de testes

| Cenário | Resultado esperado |
|---|---|
| Exclusão sem chave de API | HTTP 401 Unauthorized |
| Exclusão com chave válida | HTTP 200 OK |
| Cadastro com dados válidos e chave válida | HTTP 201 Created |
| Atualização com dados válidos e chave válida | HTTP 200 OK |
| Cadastro com ano enviado como texto | HTTP 400 Bad Request |

## Execução local

1. Instale o Python.
2. Crie e ative um ambiente virtual.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure a variável de ambiente `API_KEY` com uma chave de laboratório.
5. Execute a aplicação:

```bash
python api-rest.py
```

A API ficará disponível localmente em `http://127.0.0.1:5000`.

## Limitações e melhorias futuras

- Os dados são armazenados em memória e não persistem após o reinício.
- A chave de API é uma proteção didática, não um sistema completo de autenticação.
- As rotas de consulta permanecem públicas neste laboratório.
- Uma implantação real exigiria HTTPS, gestão segura de segredos, autorização apropriada, testes automatizados e configuração de produção.

## Aviso

Projeto educacional executado em ambiente local, com dados fictícios. Não foi concebido para uso direto em produção.

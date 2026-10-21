
from flask import Flask, jsonify, request
from functools import wraps
import os

app = Flask(__name__)

CHAVE_API = os.environ.get("API_KEY", "chave-lab-123")


def requerer_api_key(funcao):
    @wraps(funcao)
    def verificar_chave(*args, **kwargs):
        chave = request.headers.get("X-API-Key")

        if chave != CHAVE_API:
            return jsonify({
                "erro": "Nao autorizado"
            }), 401

        return funcao(*args, **kwargs)

    return verificar_chave


filmes = [
    {
        "id": 1,
        "titulo": "Velozes e Furiosos",
        "genero": "acao",
        "ano": 2001
    },
    {
        "id": 2,
        "titulo": "Interestelar",
        "genero": "ficcao cientifica",
        "ano": 2014
    },
    {
        "id": 3,
        "titulo": "Batman",
        "genero": "acao",
        "ano": 2022
    }
]



@app.route("/filmes", methods=["GET"])
def listar_filmes():
    return jsonify(filmes), 200



@app.route("/filmes/<int:id>", methods=["GET"])
def consultar_filme(id):
    for filme in filmes:
        if filme["id"] == id:
            return jsonify(filme), 200

    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route("/filmes", methods=["POST"])
@requerer_api_key
def cadastrar_filme():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie um objeto JSON valido"}), 400

    campos = ["titulo", "genero", "ano"]

    if any(campo not in dados for campo in campos):
        return jsonify({
            "erro": "Informe titulo, genero e ano"
        }), 400

    titulo = dados["titulo"]
    genero = dados["genero"]
    ano = dados["ano"]

    if not isinstance(titulo, str) or not titulo.strip():
        return jsonify({"erro": "Titulo invalido"}), 400

    if not isinstance(genero, str) or not genero.strip():
        return jsonify({"erro": "Genero invalido"}), 400

    if type(ano) is not int or not 1888 <= ano <= 2100:
        return jsonify({"erro": "Ano invalido"}), 400

    novo_id = max(
        (filme["id"] for filme in filmes),
        default=0
    ) + 1

    novo_filme = {
        "id": novo_id,
        "titulo": titulo.strip(),
        "genero": genero.strip(),
        "ano": ano
    }

    filmes.append(novo_filme)

    return jsonify(novo_filme), 201

@app.route("/filmes/<int:id>", methods=["PUT"])
@requerer_api_key
def atualizar_filme(id):
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie um objeto JSON valido"}), 400

    campos = ["titulo", "genero", "ano"]

    if any(campo not in dados for campo in campos):
        return jsonify({
            "erro": "Informe titulo, genero e ano"
        }), 400

    titulo = dados["titulo"]
    genero = dados["genero"]
    ano = dados["ano"]

    if not isinstance(titulo, str) or not titulo.strip():
        return jsonify({"erro": "Titulo invalido"}), 400

    if not isinstance(genero, str) or not genero.strip():
        return jsonify({"erro": "Genero invalido"}), 400

    if type(ano) is not int or not 1888 <= ano <= 2100:
        return jsonify({"erro": "Ano invalido"}), 400

    for filme in filmes:
        if filme["id"] == id:
            filme["titulo"] = titulo.strip()
            filme["genero"] = genero.strip()
            filme["ano"] = ano

            return jsonify(filme), 200

    return jsonify({"erro": "Filme nao encontrado"}), 404

@app.route("/filmes/<int:id>", methods=["DELETE"])
@requerer_api_key
def excluir_filme(id):
    for indice, filme in enumerate(filmes):
        if filme["id"] == id:
            filme_removido = filmes.pop(indice)

            return jsonify({
                "mensagem": "Filme excluido com sucesso",
                "filme": filme_removido
            }), 200

    return jsonify({"erro": "Filme nao encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=False)

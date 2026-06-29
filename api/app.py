"""
API REST - DescomplicaBusiness (Sistema de Atendimento)
Trabalho Final - Cloud Computing - UNIDAVI
Aluno: Felipe Macedo

Expõe informações de saúde da aplicação e os atendimentos do
pequeno negócio. Os dados ficam em um arquivo JSON externo
(api/data/atendimentos.json), nunca embutidos no código.
"""
import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

VERSAO = "1.0.0"

# Caminho do JSON externo, relativo a este arquivo (funciona local e em container)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "atendimentos.json")


def carregar_atendimentos():
    """Lê os atendimentos do arquivo JSON externo e devolve uma lista."""
    with open(DATA_PATH, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


@app.route("/status", methods=["GET"])
def status():
    """Rota de saúde: nome, versão e status da aplicação."""
    return jsonify({
        "nome": "DescomplicaBusiness API",
        "versao": VERSAO,
        "status": "online"
    }), 200


@app.route("/atendimentos", methods=["GET"])
def listar_atendimentos():
    """Retorna todos os atendimentos cadastrados (>= 10 registros)."""
    atendimentos = carregar_atendimentos()
    return jsonify({
        "total": len(atendimentos),
        "atendimentos": atendimentos
    }), 200


@app.route("/atendimentos/<int:atendimento_id>", methods=["GET"])
def obter_atendimento(atendimento_id):
    """Retorna um único atendimento pelo id, ou 404 se não existir."""
    atendimentos = carregar_atendimentos()
    for atendimento in atendimentos:
        if atendimento["id"] == atendimento_id:
            return jsonify(atendimento), 200
    # Nenhum registro com o id informado -> 404 padronizado
    return jsonify({
        "erro": "Atendimento nao encontrado",
        "codigo": 404
    }), 404


@app.errorhandler(404)
def nao_encontrado(_e):
    """Padroniza qualquer 404 (ex.: rota inexistente) como JSON."""
    return jsonify({"erro": "Recurso nao encontrado", "codigo": 404}), 404


@app.errorhandler(500)
def erro_interno(_e):
    """Padroniza erros internos (500) como JSON."""
    return jsonify({"erro": "Erro interno do servidor", "codigo": 500}), 500


if __name__ == "__main__":
    # host 0.0.0.0 para funcionar dentro do container
    app.run(host="0.0.0.0", port=5000, debug=True)

"""
Testes unitários da API DescomplicaBusiness.
Trabalho Final - Cloud Computing - UNIDAVI - Felipe Macedo

Usam o test client do Flask, sem subir um servidor real.
"""
import os
import sys

import pytest

# Garante que o módulo app (em api/) seja importável a partir de api/tests/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # noqa: E402


@pytest.fixture
def client():
    """Cliente de teste do Flask reutilizado pelos testes."""
    app.config["TESTING"] = True
    with app.test_client() as cliente:
        yield cliente


def test_listar_atendimentos_status_200(client):
    """Teste 1 (obrigatório): GET /atendimentos deve retornar HTTP 200."""
    resposta = client.get("/atendimentos")
    assert resposta.status_code == 200


def test_estrutura_json_campos_obrigatorios(client):
    """Teste 2 (obrigatório): valida a estrutura/campos do JSON retornado."""
    resposta = client.get("/atendimentos")
    dados = resposta.get_json()

    assert "total" in dados
    assert "atendimentos" in dados
    assert dados["total"] >= 10  # o tema exige no mínimo 10 registros

    primeiro = dados["atendimentos"][0]
    campos_obrigatorios = ["id", "cliente", "assunto", "canal", "status"]
    for campo in campos_obrigatorios:
        assert campo in primeiro


def test_atendimento_inexistente_retorna_404(client):
    """Teste 3 (obrigatório): id inexistente em GET /atendimentos/{id} -> 404."""
    resposta = client.get("/atendimentos/999")
    assert resposta.status_code == 404
    assert resposta.get_json()["codigo"] == 404


def test_atendimento_existente_retorna_registro_correto(client):
    """
    Teste 4 (autoria própria): GET /atendimentos/<id> válido deve devolver
    o registro correto (id e cliente conferem). Escolhi este teste porque os
    outros três cobrem listagem, estrutura e o caminho de erro (404), mas
    nenhum valida o "caminho feliz" da busca por id — justamente a rota mais
    sujeita a erro de lógica na filtragem. Ele garante 200 e o conteúdo certo.
    """
    resposta = client.get("/atendimentos/1")
    assert resposta.status_code == 200

    dados = resposta.get_json()
    assert dados["id"] == 1
    assert dados["cliente"] == "Padaria Pão Quente"

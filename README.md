# DescomplicaBusiness API — Trabalho Final de Cloud Computing

API REST do sistema de atendimento **DescomplicaBusiness**, com pipeline de
Integração Contínua (CI) no GitHub Actions.

- **Aluno:** Felipe Macedo
- **Curso:** Sistemas de Informação — UNIDAVI
- **Disciplina:** Cloud Computing — Prof. Esp. Ademar Perfoll Junior
- **Tema individual:** Sistema de Atendimento para um Pequeno Negócio

## Tecnologias
- Python 3.12 + Flask (API REST)
- pytest (testes unitários)
- flake8 (análise estática / lint)
- Docker (execução em container)
- GitHub Actions (CI)

## Estrutura do projeto
```
descomplica-business-api/
├── api/
│   ├── app.py                 # Aplicação Flask (rotas)
│   ├── data/
│   │   └── atendimentos.json  # Dados simulados (>= 10 registros)
│   └── tests/
│       └── test_api.py        # Testes unitários (pytest)
├── .github/workflows/ci.yml   # Pipeline de Integração Contínua
├── Dockerfile                 # Imagem da API
├── requirements.txt           # Dependências
├── .flake8                    # Configuração do lint
└── README.md
```

## Rotas da API
| Método | Rota | Descrição | Códigos |
|---|---|---|---|
| GET | `/status` | Saúde da aplicação (nome, versão, status) | 200 |
| GET | `/atendimentos` | Lista todos os atendimentos (≥10) | 200 |
| GET | `/atendimentos/<id>` | Retorna um atendimento pelo id | 200 / 404 |

Exemplo de resposta de `GET /status`:
```json
{ "nome": "DescomplicaBusiness API", "versao": "1.0.0", "status": "online" }
```

## Como executar — SEM container (local)
Pré-requisito: Python 3.12 instalado.
```bash
# 1. Clonar o repositório
git clone https://github.com/FelipeMacedoK/descomplica-business-api.git
cd descomplica-business-api

# 2. (Opcional) criar ambiente virtual
python -m venv .venv
# Windows: .venv\Scripts\activate   |   Linux/Mac: source .venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Rodar a API
python api/app.py
```
A API ficará em **http://localhost:5000** (ex.: http://localhost:5000/atendimentos).

## Como executar — COM container (Docker)
```bash
docker build -t descomplica-business-api .
docker run -p 5000:5000 descomplica-business-api
```
Acesse **http://localhost:5000/status**.

## Como rodar os testes
```bash
pip install -r requirements.txt
flake8 api      # análise estática
pytest -v       # testes unitários
```

## Integração Contínua (CI)
O arquivo [`.github/workflows/ci.yml`](.github/workflows/ci.yml) executa, a cada
push na `main`: checkout → setup do Python → instalação de dependências →
**flake8 (lint)** → **pytest**. O status do pipeline aparece na aba **Actions**
do repositório.

## Uso de Inteligência Artificial
O uso de IA está descrito na seção correspondente do Relatório Técnico Final,
com a ferramenta utilizada, como foi empregada e o que foi revisado manualmente.

# live-coding-langchain-langgraph

Projeto de agente IA "Chef" construído com LangChain e LangGraph. O agente atua como um chefe de cozinha experiente, buscando receitas na internet e adaptando sugestões aos ingredientes fornecidos pelo usuário.

## Funcionalidades

- **LangChain** com `create_agent` para orquestração
- **System prompt** com persona, limites e comportamento definidos
- **Ferramenta de busca** (`search_internet`) via Tavily para pesquisar receitas na web

## Pré-requisitos

- Python 3.12 ou superior
- Contas e chaves de API:
  - [OpenAI](https://platform.openai.com/) — modelo de linguagem
  - [Tavily](https://tavily.com/) — busca na internet

## Instalação

### Com uv (recomendado)

```bash
uv sync
```

### Com pip

```bash
pip install -e .
```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as variáveis de ambiente:

```bash
OPENAI_API_KEY=sua-chave-openai
TAVILY_API_KEY=sua-chave-tavily
```

> **Nota:** O `langgraph.json` já referencia o arquivo `.env` automaticamente.

## Como executar

O agente é exposto via **LangGraph**. Para rodar:

```bash
# Instale as dependências (incluindo langgraph-cli para desenvolvimento)
uv sync --extra dev

# Inicie o servidor LangGraph
langgraph dev
```

O servidor estará disponível em `http://localhost:2024` (ou na porta indicada no terminal). A partir daí você pode interagir com o agente via interface web ou API.

> **Dica:** O `main.py` exporta o `CHEF_AGENT` referenciado no `langgraph.json`. Para usar o agente programaticamente em outro script Python, importe: `from chef_agent.main import CHEF_AGENT`.

## Estrutura do projeto

```
├── src/chef_agent/
│   ├── prompts.py    # Prompt do sistema (persona, limites, comportamento)
│   ├── tools.py      # Ferramenta de busca de receitas (Tavily)
│   ├── agent.py      # Construção do agente LangChain
│   └── main.py       # Exporta CHEF_AGENT para o LangGraph
├── langgraph.json    # Configuração do LangGraph
├── pyproject.toml    # Dependências e metadados
└── README.md
```

## Dependências principais

| Pacote | Uso |
|--------|-----|
| `langchain` | Orquestração do agente |
| `langchain-openai` | Modelo de linguagem (GPT) |
| `tavily-python` | Busca de receitas na internet |

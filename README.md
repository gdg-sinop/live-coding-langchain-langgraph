# Live Coding: LangChain Basics

Esta ramificação é um guia prático e demonstrativo sobre os fundamentos do **LangChain**, focado em ensinar como construir aplicações baseadas em LLMs (Large Language Models) de forma interativa.

O conteúdo aborda desde a invocação básica de modelos de chat até a criação de agentes autônomos com memória, uso de ferramentas personalizadas e saídas estruturadas.

## 📋 Conteúdo Abordado

O notebook principal (`1.1_intro_to_langchain_basics.ipynb`) cobre os seguintes tópicos:

1.  **Invocação de Modelos de Chat**:
    -   Inicialização e configuração de modelos (OpenAI GPT, Google Gemini).
    -   Ajuste de hiperparâmetros (temperatura, max_tokens, timeout).
2.  **Criação de Agentes (ReAct)**:
    -   Conceito e implementação de agentes que raciocinam e agem.
    -   Uso de `create_agent` do LangChain.
3.  **Engenharia de Prompt**:
    -   Definição de **System Prompts** para atribuir personas e contexto (ex: Assistente de Vendas Imobiliárias).
4.  **Saídas Estruturadas (Structured Outputs)**:
    -   Uso do Pydantic para garantir respostas em formato JSON previsível.
5.  **Ferramentas Personalizadas (Tools)**:
    -   Criação de ferramentas customizadas com o decorador `@tool` (ex: calculadora de parcelas).
    -   Integração de ferramentas de busca na web (**Tavily**).
6.  **Memória Persistente**:
    -   Implementação de memória de conversa usando `InMemorySaver` e `LangGraph`.
    -   Gerenciamento de estado da conversa (stateful vs stateless).

## 🚀 Pré-requisitos

-   **Python 3.12+**
-   Chaves de API para os serviços utilizados:
    -   [OpenAI](https://platform.openai.com/)
    -   [Google AI Studio (Gemini)](https://aistudio.google.com/)
    -   [Tavily Search](https://tavily.com/)
    -   [LangSmith](https://smith.langchain.com/) (Opcional, para tracing)

## 🛠️ Instalação e Configuração
1.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows: .venv\Scripts\activate
    ```

2.  **Instale as dependências:**

    Este projeto utiliza `uv` para gerenciamento de pacotes, mas você pode instalar via pip com base no `pyproject.toml`:

    ```bash
    pip install langchain langchain-openai python-dotenv langchain-google-genai tavily-python langchain-core ipykernel
    ```
    
    *Ou se tiver o `uv` instalado:*
    ```bash
    uv sync
    ```

3.  **Configure as Variáveis de Ambiente:**

    Copie o arquivo de exemplo `.env.example` para `.env` e preencha com suas chaves de API:

    ```bash
    cp .env.example .env
    ```

    Edite o arquivo `.env`:

    ```ini
    OPENAI_API_KEY=sua-chave-aqui
    GOOGLE_API_KEY=sua-chave-aqui
    TAVILY_API_KEY=sua-chave-aqui

    # Opcional: Configuração do LangSmith para monitoramento
    LANGSMITH_TRACING=true
    LANGSMITH_ENDPOINT=https://api.smith.langchain.com
    LANGSMITH_API_KEY=sua-chave-aqui
    LANGSMITH_PROJECT=live-coding
    ```

##  ▶️ Como Usar

Abra o notebook Jupyter para acompanhar o passo a passo:

1.  Inicie o servidor Jupyter:
    ```bash
    jupyter notebook
    ```
    Ou abra diretamente no VS Code / Cursor.

2.  Abra o arquivo `1.1_intro_to_langchain_basics.ipynb`.

3.  Execute as células sequencialmente para ver os conceitos em ação.

## 📚 Tecnologias Utilizadas

-   **[LangChain](https://www.langchain.com/)**: Framework para orquestração de LLMs.
-   **[LangGraph](https://langchain-ai.github.io/langgraph/)**: Biblioteca para construção de agentes estatais e fluxos de trabalho.
-   **[OpenAI API](https://openai.com/)**: Modelos GPT.
-   **[Google Gemini API](https://deepmind.google/technologies/gemini/)**: Modelos Gemini.
-   **[Tavily](https://tavily.com/)**: Motor de busca otimizado para agentes de IA.
-   **[Pydantic](https://docs.pydantic.dev/)**: Validação de dados e definição de schemas.

## 👤 Autor

**Sergio Ramos**
-   Email: sergio.b.snp@gmail.com

---
*Este projeto foi desenvolvido para fins educacionais.*

from __future__ import annotations

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from chef_agent.prompts import SYSTEM_PROMPT
from chef_agent.tools import search_internet


def build_chef_agent():
    """
    Cria o agente de receitas com:
    - create_agent
    - system prompt (persona, limites e comportamento)
    - ferramenta de busca na internet
    - persistência gerenciada automaticamente pelo LangGraph API
    """
    model = init_chat_model(model="gpt-4o-mini")

    return create_agent(
        model=model,
        tools=[search_internet],
        system_prompt=SYSTEM_PROMPT,
    )


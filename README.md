# live-coding-langchain-langgraph

Boilerplate de um agente "chefe de cozinha" com:
- `langchain` usando `create_agent`
- `system_prompt` com persona, limites e comportamento
- ferramenta `search_recipts_on_internet`
- memoria com checkpointer (`MemorySaver`)

## Estrutura

- `src/chef_agent/prompts.py`: prompt do sistema
- `src/chef_agent/tools.py`: ferramenta de busca de receitas
- `src/chef_agent/agent.py`: construcao do agente
- `src/chef_agent/main.py`: CLI simples para conversa

## Como executar

1. Configure o provider/modelo conforme suas dependencias do `pyproject.toml`.
2. Defina variaveis de ambiente (exemplo com OpenAI):
   - `OPENAI_API_KEY=...`
   - opcional: `CHEF_MODEL=openai:gpt-4o-mini`
   - opcional: `CHEF_THREAD_ID=usuario-1`
3. Rode:

```bash
python -m chef_agent.main
```
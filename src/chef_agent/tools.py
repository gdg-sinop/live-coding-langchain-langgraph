from langchain.tools import tool

from tavily import TavilyClient

tavily_client = TavilyClient()


@tool
def search_internet(query: str) -> str:
    """
    Pesquisa receitas e informações culinárias na internet.
    Use esta ferramenta SEMPRE que o usuário fornecer ingredientes ou pedir sugestões de receitas.
    O parâmetro query deve ser uma busca descritiva, por exemplo: "receita com frango e batata"
    ou "como fazer bolo de chocolate".
    Retorna resultados de busca com título, conteúdo e URL das fontes.
    """
    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
    )
    results = response.get("results", [])
    if not results:
        return "Nenhum resultado encontrado para a busca."

    parts = []
    for i, r in enumerate(results, 1):
        title = r.get("title", "Sem título")
        content = r.get("content", "")
        url = r.get("url", "")
        parts.append(f"[{i}] {title}\n{content}\nFonte: {url}")
    return "\n\n---\n\n".join(parts)
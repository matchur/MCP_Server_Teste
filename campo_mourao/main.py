from fastmcp import FastMCP

mcp = FastMCP("MCP", version="1.0")

async def consulta_api(cidade: str) -> str:
    return httpx.get(f"https://wttr.in/{cidade}?format=%t").text


@mcp.resource(uri="workshop://oque-o-mcp-nao-e")
def guia_mcp() -> str:
    return """
    --- MCP NÃO É ---
    - NÃO É UM FRAMEWORK
    - NÃO FAZ LOOPS DE RACIOCÍNIO OU MEMORIA
    - NÃO EXECUTA IA NO SERVIDOR
    - LEMBRETE: MCP É DETERMINÍSTICO
    """


@mcp.resource("previsao://{cidade}")
async def previsao(cidade: str) -> str:
    res = await consulta_api(cidade)
    return f"Previsão {cidade}:{res}"

if __name__ == "__main__":
    mcp.run()
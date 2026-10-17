import httpx
from fastmcp import FastMCP

mcp = FastMCP("MCP", version="1.0")


async def consulta_api(cidade: str) -> str:
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(
            f"https://wttr.in/{cidade}",
            params={"format": "%t"}
        )
        response.raise_for_status()
        return response.text


@mcp.resource("workshop://oque-o-mcp-nao-e")
def guia_mcp() -> str:
    return """
    --- MCP NÃO É ---
    - NÃO É UM FRAMEWORK
    - NÃO FAZ LOOPS DE RACIOCÍNIO OU MEMÓRIA
    - NÃO EXECUTA IA NO SERVIDOR
    - LEMBRETE: MCP É DETERMINÍSTICO
    """


@mcp.resource("previsao://{cidade}")
async def previsao(cidade: str) -> str:
    temperatura = await consulta_api(cidade)
    return f"Temperatura em {cidade}: {temperatura}"


@mcp.tool()
async def consultar_temperatura(cidade: str) -> str:
    """Consulta a temperatura atual de uma cidade."""
    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(
                f"https://wttr.in/{cidade}",
                params={"format": "%t"}
            )

            response.raise_for_status()

            return (
                f"Temperatura atual em {cidade}: "
                f"{response.text.strip()}"
            )

    except httpx.TimeoutException:
        return f"Erro: tempo limite excedido ao consultar {cidade}."

    except httpx.HTTPError as erro:
        return f"Erro HTTP na consulta: {type(erro).__name__}: {erro}"

    except Exception as erro:
        return f"Erro inesperado: {type(erro).__name__}: {erro}"


if __name__ == "__main__":
    mcp.run()
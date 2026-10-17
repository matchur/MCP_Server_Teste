# Notebook de arquitetura MCP

Abra `arquitetura_mcp.ipynb` em Jupyter ou VS Code. Use um kernel Python 3.13+ com as dependências do novo servidor:

```powershell
cd guia_estudos_mcp
uv sync
uv run --with jupyterlab jupyter lab ../python_notebook/arquitetura_mcp.ipynb
```

Execute as células em ordem. O notebook cria um arquivo de tarefas temporário; as tarefas salvas pelo servidor fora do notebook permanecem intactas.

Para consultar as definições formais depois do exercício: [arquitetura e primeiros passos do MCP](https://py.sdk.modelcontextprotocol.io/get-started/first-steps/) e [primitivas do servidor na especificação](https://modelcontextprotocol.io/specification/draft/server/index).

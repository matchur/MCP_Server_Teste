import json
from pathlib import Path
from fastmcp import FastMCP

mcp = FastMCP("Guia de Estudos")
ARQUIVO = Path(__file__).with_name("tarefas.json")

def carregar_tarefas() -> list[dict]:
    """Lê o estado local; na primeira execução ainda não existe arquivo."""
    if not ARQUIVO.exists():
        return []
    return json.loads(ARQUIVO.read_text(encoding="utf-8"))


def salvar_tarefas(tarefas: list[dict]) -> None:
    ARQUIVO.write_text(json.dumps(tarefas, ensure_ascii=False, indent=2), encoding="utf-8")


@mcp.tool
def adicionar_tarefa(assunto: str) -> str:
    """Adiciona um assunto"""
    assunto = assunto.strip()
    if not assunto:
        return "Informe um assunto para estudar."

    tarefas = carregar_tarefas()
    novo_id = max((tarefa["id"] for tarefa in tarefas), default=0) + 1
    tarefas.append({"id": novo_id, "assunto": assunto, "concluida": False})
    salvar_tarefas(tarefas)
    return f"Tarefa {novo_id} adicionada: {assunto}"


@mcp.tool
def concluir_tarefa(id_tarefa: int) -> str:
    """Marca uma tarefa de estudo como concluída pelo ID."""
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            if tarefa["concluida"]:
                return f"A tarefa {id_tarefa} já estava concluída."
            tarefa["concluida"] = True
            salvar_tarefas(tarefas)
            return f"Tarefa {id_tarefa} concluída."
    return f"Tarefa {id_tarefa} não encontrada."


@mcp.resource("estudos://tarefas")
def tarefas_de_estudo() -> str:
    """Mostra o estado atual da lista, sem alterá-la."""
    tarefas = carregar_tarefas()
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    return "\n".join(
        f"{tarefa['id']}. [{'x' if tarefa['concluida'] else ' '}] {tarefa['assunto']}"
        for tarefa in tarefas
    )


@mcp.prompt
def planejar_estudo(tema: str) -> str:
    """Instrução reutilizável para montar um plano curto de estudo."""
    return (
        f"Monte um plano introdutório e prático para estudar {tema}. "
        "Sugira até três tarefas pequenas. Antes de cadastrar qualquer uma, "
        "mostre as sugestões ao usuário."
    )


if __name__ == "__main__":
    mcp.run()

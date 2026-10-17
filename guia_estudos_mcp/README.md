 O cliente MCP pode chamar ferramentas para adicionar e concluir tarefas, ler um recurso com a lista atual e obter um prompt para planejar estudos. Os dados ficam em `tarefas.json`, criado nesta pasta na primeira inclusão.

## Executar

```powershell
uv sync
uv run python main.py
```

## Como fazer

1. Chame a ferramenta `adicionar_tarefa` com `{"assunto": "Entender tools e resources"}`.
2. Leia o recurso `estudos://tarefas`. Ele mostrará a tarefa com seu ID.
3. Chame `concluir_tarefa` com `{"id_tarefa": 1}` e leia o recurso de novo.
4. Peça o prompt `planejar_estudo` com `{"tema": "MCP"}`. Ele retorna instruções para o cliente; 

## Ideia central

`tool` representa uma ação

 `resource` fornece dados para leitura 

`prompt` oferece um roteiro reutilizável

O cliente decide quando usar cada um. O servidor executa funções Python comuns e salva estado em JSON

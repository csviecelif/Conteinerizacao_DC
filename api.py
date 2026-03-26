from fastapi import FastAPI
from pydantic import BaseModel

class Tarefa(BaseModel):
    id: int
    titulo: str
    finalizado: bool = False

API = FastAPI()
TAREFAS = []

@API.get('/')
def root():
    return 'ok'

@API.get('/tarefas')
def listar_tarefas():
    return TAREFAS

@API.post('/tarefas')
def criar_tarefa(titulo: str):
    nova = Tarefa(id=len(TAREFAS), titulo=titulo)
    TAREFAS.append(nova)
    return f"Tarefa '{titulo}' criada"

@API.delete('/tarefas/{id}')
def remover_tarefa(id: int):
    if len(TAREFAS) > 0 and id < len(TAREFAS):
        t = TAREFAS.pop(id)
        return f"Tarefa '{t.titulo}' removida"
    return "Tarefa não encontrada"

@API.put('/tarefas/{id}')
def atualizar_tarefa(id: int, titulo: str, estado: bool):
    if len(TAREFAS) > 0 and id < len(TAREFAS):
        TAREFAS[id].titulo = titulo
        TAREFAS[id].finalizado = estado
        return f"Tarefa '{id}' atualizada"
    return "Tarefa não encontrada"

@API.get('/autor')
def autor():
    return 'Cassio'

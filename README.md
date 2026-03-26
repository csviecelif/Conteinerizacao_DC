API REST simples (FastAPI) rodando em Cont. Docker, disponível na porta 8000.

## Como executar
docker build -t api-tarefas .
docker run -p 8000:8000 api-tarefas

## Ameaças STRIDE

### Tampering (Adulteração de Dados)

Um atacante pode enviar dados malformados ou com tipos errados para tentar corromper o estado da aplicação.

**Mitigação:** o uso do Pydantic (`BaseModel`) garante validação de input de usuário. 

### Denial of Service (Negação de Serviço)

Um atacante pode tentar derrubar a API enviando um volume muito grande de requisições simultâneas.

**Mitigação:** ao rodar a aplicação dentro de um contêiner Docker, é possível limitar os recursos (CPU, memória) com flags como `--memory` e `--cpus`, evitando que a API consuma todos os recursos do servidor. Exemplo: docker run -p 8000:8000 --memory=256m --cpus=0.5 api-tarefas

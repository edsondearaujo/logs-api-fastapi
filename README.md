# Logs API com FastAPI

## Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/logs-api-fastapi.git
    ```
2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3.Inicie o servidor:

   ```bash
   uvicorn app.main:app --reload
   ```
* Acesse a API em http://localhost:8000.

Como rodar com Docker
Suba os containers:

   ```bash
   docker-compose up --build
   ```

Acesse a API em http://localhost:80.
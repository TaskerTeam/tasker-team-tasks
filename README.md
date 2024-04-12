# Tarefas

Este é um projeto para gerenciar tarefas em equipe.

Configuração do Banco de Dados PostgreSQL

Antes de executar o projeto, é necessário configurar um banco de dados PostgreSQL.
Siga as instruções abaixo para configurar o banco de dados e configurar a conexão no projeto.


```sql
CREATE DATABASE notas
```

Criação da Tabela

Após configurar o banco de dados, execute o seguinte comando SQL para criar a tabela "tasks":

```sql

-- Criação da tabela 'task_status'
CREATE TABLE task_status (
    status_id SERIAL PRIMARY KEY,
    status_name VARCHAR NOT NULL
);

-- Criação da tabela 'tasks'
CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    date TIMESTAMP NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (status_id) REFERENCES task_status(status_id)
);
```

Esta tabela será usada para armazenar as tarefas do projeto.

## Configurar a Conexão no Projeto

Na pasta dotenv_files/ copie o arquivo .env_exemple e renomeie para .env

No arquivo dotenv_files/.env, altere a URL de conexão para o banco de dados PostgreSQL para refletir suas credenciais e detalhes de conexão. 

A URL padrão é a seguinte:

```python

    'postgresql+psycopg2://username:password@localhost:5432/notas'

```

- Substitua 'username' pelo seu nome de usuário do PostgreSQL
- 'password' pela senha correspondente. 
- Certifique-se de que o host seja 'localhost', a porta seja '5432' e o nome do banco de dados seja 'notas'.

## Executando o Projeto

Para instalar as dependências, execute o seguinte comando:

```bash

    pip install -r requirements.txt

```

Para iniciar o servidor, execute o seguinte comando:

```bash

python3 grpc_server.py

```
## Exemplo de Inserção

Para inserir uma nova tarefa, envie o seguinte JSON para a API:

```json

{
  "task": {
    "title": "Nova Tarefa Inserida",
    "description": "Descrição da nova tarefa inserida",
    "date": "2026-05-20 13:30:00",
    "status_id": 2
  }
}
```
## Exemplo de Atualização

Para atualizar uma tarefa existente, envie o seguinte JSON para a API:

```json

{
  "task": {
    "task_id": 14,
    "title": "Tarefa Atualizada",
    "description": "Nova descrição da tarefa atualizada",
    "date": "2026-05-20 13:30:00"
  }
}
```

Atenção: seguir padrão de data `"2026-05-20 13:30:00"`

## Exemplo Buscar status pelo nome

```json
{
	"status_name": "concluido"
}
```

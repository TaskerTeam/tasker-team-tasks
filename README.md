# Tarefas

Este é um projeto para gerenciar tarefas em equipe.

Configuração do Banco de Dados PostgreSQL

Antes de executar o projeto, é necessário configurar um banco de dados PostgreSQL.
Siga as instruções abaixo para configurar o banco de dados e configurar a conexão no projeto.


**CREATE DATABASE notas**

Criação da Tabela

Após configurar o banco de dados, execute o seguinte comando SQL para criar a tabela "tasks":

```sql

CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    date TIMESTAMP WITHOUT TIME ZONE NOT NULL
);
```

Esta tabela será usada para armazenar as tarefas do projeto.

## Configurar a Conexão no Projeto

No arquivo tasksORM/connection.py, altere a URL de conexão para o banco de dados PostgreSQL para refletir suas credenciais e detalhes de conexão. 

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
    "date": "2026-05-20 13:30:00"
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

# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST em Python para gerenciar tarefas. Você aprenderá a criar rotas com FastAPI, validar dados, retornar códigos HTTP adequados e testar suas operações.

## 📝 Tarefas

### 🛠️ Iniciar a API e criar a primeira rota

#### Descrição
Você precisará de Python 3.10 ou superior, `pip` e conhecimentos básicos de funções, listas e dicionários. Baixe `main.py` e `requirements.txt` pelo portal e coloque os dois arquivos na mesma pasta. No terminal, dentro dessa pasta, crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows, usando PowerShell, substitua o comando `source` por `.venv\Scripts\Activate.ps1`. Em seguida, instale as dependências e inicie a aplicação:

```bash
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Com o ambiente preparado, complete esta primeira rota em menos de 10 minutos. O servidor atualizará a aplicação quando você salvar alterações em `main.py`.

#### Requisitos
O programa concluído deve:

- Acrescentar ao aplicativo de `main.py` uma rota `GET /` que responda com o código HTTP `200` e o JSON `{"mensagem": "API de tarefas funcionando!"}`.
- Permitir que você abra `http://127.0.0.1:8000/docs` e experimente a rota usando a documentação interativa.

### 🛠️ Criar e listar tarefas

#### Descrição
Adicione um modelo de dados e rotas para criar e listar tarefas. Use uma lista ou um dicionário em memória; não é necessário criar um banco de dados. Os dados serão perdidos quando o servidor reiniciar, inclusive após alterações no código com `--reload`.

#### Requisitos
O programa concluído deve:

- Usar um modelo Pydantic para receber `titulo`, uma string obrigatória de 1 a 100 caracteres, e `concluida`, um booleano opcional com valor padrão `false`.
- Implementar `POST /tarefas` para validar os dados, atribuir um `id` inteiro e retornar a tarefa criada com HTTP `201`. Os identificadores devem começar em `1`, crescer de um em um e não ser reutilizados enquanto o servidor estiver em execução, mesmo após uma exclusão.
- Implementar `GET /tarefas` para retornar HTTP `200` e uma lista JSON com todas as tarefas; antes de criar a primeira, a lista deve ser `[]`.
- Retornar HTTP `422` para dados inválidos, como um `titulo` ausente ou vazio.

Por exemplo, ao enviar `{"titulo": "Estudar FastAPI"}` para `POST /tarefas` em um servidor recém-iniciado, a resposta deve ser:

```json
{"id": 1, "titulo": "Estudar FastAPI", "concluida": false}
```

### 🛠️ Consultar e atualizar uma tarefa

#### Descrição
Permita que uma tarefa seja encontrada e atualizada por seu identificador. Use o mesmo modelo de entrada da criação para substituir os dados editáveis.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tarefas/{id}` para retornar a tarefa correspondente com HTTP `200`.
- Implementar `PUT /tarefas/{id}` para substituir `titulo` e `concluida`, manter o mesmo `id` e retornar a tarefa atualizada com HTTP `200`. Use as mesmas validações e o mesmo valor padrão de `concluida` definidos para `POST`.
- Retornar HTTP `404` e `{"detail": "Tarefa não encontrada"}` quando o identificador não existir, tanto na consulta quanto na atualização.
- Retornar HTTP `422` quando os dados enviados para uma atualização forem inválidos.

Por exemplo, `PUT /tarefas/1` com `{"titulo": "Estudar FastAPI e HTTP", "concluida": true}` deve responder:

```json
{"id": 1, "titulo": "Estudar FastAPI e HTTP", "concluida": true}
```

### 🛠️ Excluir e verificar as operações

#### Descrição
Conclua o gerenciamento de tarefas e use a documentação interativa para conferir o funcionamento da API. Reinicie o servidor antes da sequência de testes para limpar a memória e reiniciar a contagem dos identificadores.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /tarefas/{id}` para excluir a tarefa e retornar HTTP `204`, sem corpo na resposta.
- Retornar HTTP `404` e `{"detail": "Tarefa não encontrada"}` ao tentar excluir um identificador inexistente.
- Não incluir tarefas excluídas em `GET /tarefas` nem permitir consultá-las por identificador.
- Testar, em `/docs` e sem reiniciar o servidor durante a sequência:
  1. Com uma lista inicialmente vazia, criar uma tarefa válida e conferir o HTTP `201` e o `id` igual a `1`.
  2. Tentar criar uma tarefa com `titulo` vazio e conferir o HTTP `422`.
  3. Consultar e atualizar a tarefa criada, conferindo as respostas e o HTTP `200`.
  4. Excluir a tarefa, conferir o HTTP `204` e verificar que uma consulta ou nova exclusão do mesmo `id` retorna HTTP `404`.
  5. Criar outra tarefa e conferir que ela recebe `id` igual a `2`, mesmo após a exclusão.

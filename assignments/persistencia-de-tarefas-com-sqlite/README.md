# 📘 Atividade: Persistência de Tarefas com SQLite

## 🎯 Objetivo

Adapte a API de tarefas feita com FastAPI para armazenar os dados em um banco SQLite. Você praticará a criação de uma tabela e operações SQL básicas, mantendo as rotas e validações da API.

## 📝 Tarefas

### 🛠️ Executar e explorar a API inicial

#### Descrição
Baixe `starter-code.py` e renomeie-o para `main.py`. Você precisará de Python 3.10 ou superior, `pip` e dos conhecimentos da atividade de APIs REST com FastAPI. No terminal, na pasta do arquivo, instale as dependências e inicie o servidor:

```bash
python -m pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

Abra `http://127.0.0.1:8000/docs`, crie uma tarefa e confira a lista. Reinicie o servidor e confira novamente: a implementação inicial guarda os dados apenas na memória.

#### Requisitos
O programa concluído deve:

- Iniciar localmente e disponibilizar a documentação interativa em `/docs`.
- Permitir criar e listar tarefas antes de qualquer alteração no código.
- Demonstrar que os dados da implementação inicial desaparecem após reiniciar o servidor.


### 🛠️ Criar o banco e a tabela de tarefas

#### Descrição
Use o módulo `sqlite3`, que já faz parte do Python, para criar um arquivo de banco chamado `tarefas.db` na pasta da aplicação. Inicialize a tabela quando a aplicação for iniciada, sem apagar os dados se a tabela já existir.

#### Requisitos
O programa concluído deve:

- Criar a tabela `tarefas` com `id` inteiro como chave primária autoincremental, `titulo` obrigatório e `concluida` inteira com valor padrão `0`.
- Usar `CREATE TABLE IF NOT EXISTS` para preservar a tabela e os dados em reinicializações.
- Criar o arquivo `tarefas.db` ao iniciar a aplicação.


### 🛠️ Salvar e consultar tarefas no SQLite

#### Descrição
Substitua o dicionário em memória pelas operações de banco de dados nas rotas existentes. Abra uma conexão para cada operação, confirme alterações com `commit()` e use parâmetros `?` nas consultas para enviar valores. Converta `concluida` entre o booleano da API e o inteiro armazenado no SQLite.

#### Requisitos
O programa concluído deve:

- Fazer `POST /tarefas` salvar a tarefa e retornar HTTP `201` com o identificador gerado pelo banco.
- Fazer `GET /tarefas` listar todas as tarefas e `GET /tarefas/{id}` consultar uma tarefa pelo identificador.
- Fazer `PUT /tarefas/{id}` atualizar título e estado de conclusão sem alterar o identificador.
- Fazer `DELETE /tarefas/{id}` excluir a tarefa e retornar HTTP `204`, sem corpo.
- Manter as validações de entrada e retornar HTTP `404` com `{"detail": "Tarefa não encontrada"}` quando o identificador não existir.
- Não montar consultas SQL concatenando valores recebidos pela API.


### 🛠️ Verificar a persistência e as operações

#### Descrição
Use `/docs` para testar as rotas. Faça a sequência sem reiniciar o servidor até a etapa indicada e, então, reinicie-o para verificar que o SQLite preservou os dados.

#### Requisitos
O programa concluído deve:

- Criar uma tarefa e confirmar que ela aparece em `GET /tarefas`.
- Atualizar a tarefa e confirmar que o título e o estado de conclusão mudaram.
- Excluir a tarefa e confirmar que uma consulta pelo identificador retorna HTTP `404`.
- Criar uma nova tarefa e reiniciar o servidor; depois, confirmar que ela continua em `GET /tarefas`.
- Confirmar que um identificador já utilizado não é reutilizado depois de excluir uma tarefa.
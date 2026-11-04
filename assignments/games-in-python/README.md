# 📘 Assignment: Jogos em Python

## 🎯 Objective

Pratique o uso de strings, entrada de dados, condicionais, laços de repetição e seleção aleatória em Python. Ao final, você terá implementado dois jogos interativos no terminal.

## 📝 Tasks

### 🛠️ Jogo da Forca

#### Descrição
Complete o código inicial para criar um jogo da Forca. O programa deve escolher uma palavra secreta e permitir que o jogador tente descobri-la, uma letra por vez.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista fornecida em `starter-code.py`.
- Exibir as letras descobertas e indicar as posições ainda não reveladas, por exemplo: `_ _ a _`.
- Aceitar um palpite de uma letra por vez e informar se ela aparece na palavra.
- Controlar e exibir o número de tentativas incorretas restantes, sem penalizar palpites repetidos.
- Encerrar quando a palavra for descoberta ou quando as tentativas incorretas acabarem, exibindo uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra.

### 🛠️ Jogo de Adivinhação

#### Descrição
Crie um jogo em que o programa escolhe um número secreto e o jogador tenta adivinhá-lo. A cada tentativa, o programa deve orientar o jogador até que ele acerte ou esgote suas chances.

#### Requisitos
O programa concluído deve:

- Escolher aleatoriamente um número inteiro entre 1 e 100.
- Permitir até 7 palpites e informar se cada palpite é maior ou menor que o número secreto.
- Validar a entrada para aceitar somente números inteiros entre 1 e 100; entradas inválidas não devem consumir uma tentativa.
- Encerrar quando o jogador acertar ou usar as 7 tentativas, exibindo uma mensagem de vitória ou derrota; em caso de derrota, revelar o número secreto.

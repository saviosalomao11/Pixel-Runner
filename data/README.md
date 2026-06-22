# Dados

Esta pasta guarda arquivos de texto usados pelo jogo.

## Arquivos

- `recorde.txt`: guarda a maior pontuacao.
- `ranking.txt`: arquivo reservado para ranking.

## Como funciona

O modulo `src/dados.py` le e grava o recorde. Se o arquivo estiver vazio, nao existir ou tiver valor invalido, o jogo considera o recorde como 0.

Esse recurso atende ao requisito de leitura e escrita em arquivo.

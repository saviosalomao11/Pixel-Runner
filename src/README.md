# Codigo-fonte

Esta pasta contem os modulos principais do jogo.

## Arquivos

- `jogo.py`: loop principal, eventos, atualizacao do mundo, colisoes, sons, telas e desenho.
- `config.py`: constantes globais, como tamanho da tela, cores, FPS, vidas, pontuacao e caminhos.
- `funcoes.py`: funcoes de logica usadas pelo jogo e pelos testes.
- `dados.py`: funcoes de leitura, escrita e atualizacao do recorde.
- `sprites.py`: funcao auxiliar para carregar partes de spritesheet.
- `__init__.py`: marca a pasta como pacote Python.

## Organizacao

A maior parte da regra visual e de interacao fica em `jogo.py`. As regras mais simples e testaveis ficam em `funcoes.py`, e a persistencia do recorde fica em `dados.py`.

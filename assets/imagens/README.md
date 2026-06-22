# Imagens

Esta pasta guarda os recursos visuais do jogo.

## Arquivos principais

- `fundo_bits.png`: fundo da fase.
- `nave_final.png`: nave de resgate mostrada no final.
- `bits_spritesheet.png`: spritesheet auxiliar do personagem.
- `spritesheet.bmp`: spritesheet base do template.
- `bits/`: imagens separadas do personagem, itens, obstaculos e partes do cenario.

## Uso no jogo

As imagens sao carregadas em `src/jogo.py` e desenhadas com Pygame. Os arquivos em `bits/` sao usados para animar BITS, desenhar obstaculos, mostrar itens coletaveis e montar partes do cenario.

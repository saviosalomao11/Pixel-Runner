# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Pixel Runner

## 2. Integrantes do grupo

- Nome 1: Sávio José Salomão Ferreira da Silva
- Nome 2: Arthur Willian Gonçalves Domingues
- Nome 3: Rodrigo Freitas Ribeiro Costa

## 3. Tipo de jogo

> Jogo de desviar de obstáculos (corrida infinita com pulo).

## 4. Descrição geral do jogo

> Na tela aparece um cenário que rola da direita para a esquerda. O jogador controla um personagem que corre automaticamente e deve pular sobre obstáculos que surgem no caminho. O desafio aumenta com o tempo, pois a velocidade dos obstáculos cresce gradualmente.

## 5. Objetivo do jogador

> Sobreviver o maior tempo possível desviando dos obstáculos e tentar superar o recorde salvo anteriormente.

## 6. Regras principais

- O personagem corre automaticamente; o jogador só controla o pulo.
- Colidir com um obstáculo remove 1 vida.
- A pontuação aumenta automaticamente com o tempo de sobrevivência.
- A velocidade dos obstáculos aumenta gradualmente ao longo da partida.
- A partida termina quando o jogador perde as 3 vidas.

## 7. Condição de vitória

> O jogo não possui condição de vitória definida. O objetivo é sobreviver o máximo possível e superar o próprio recorde.

## 8. Condição de derrota ou encerramento

> A partida termina quando o jogador perde todas as 3 vidas ao colidir com obstáculos.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

> Um personagem posicionado no lado esquerdo da tela que corre automaticamente e pode pular.

## Obstáculos, inimigos ou desafios

> Obstáculos surgem do lado direito da tela e se movem para a esquerda em velocidade crescente.

## Itens, alvos ou objetos de interação

> A definir durante o desenvolvimento.

## Pontuação, vidas, tempo ou progresso

> O jogador começa com 3 vidas. A pontuação aumenta com o tempo de sobrevivência. O recorde é salvo em arquivo.

## 10. Controles previstos

- `ESPAÇO` ou `↑`: pular
- `R`: reiniciar após Game Over
- `ESC`: sair do jogo

## 11. Organização inicial do código

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

## 12. Recursos externos previstos

> Sprites retirados do spritesheet fornecido pelo template da disciplina. Não pretendemos utilizar recursos externos adicionais.

## 13. Principais dificuldades esperadas

- Dificuldade 1: implementar a física do pulo com gravidade;
- Dificuldade 2: gerar obstáculos em intervalos aleatórios;
- Dificuldade 3: aumentar a dificuldade progressivamente sem tornar o jogo injogável.

## 14. Escopo mínimo para a entrega final

> A versão mínima terá um personagem controlado pelo teclado com mecânica de pulo, obstáculos surgindo automaticamente, sistema de 3 vidas, pontuação crescente com o tempo, recorde salvo em arquivo e tela de Game Over com opção de reiniciar.

## 15. Possíveis melhorias, caso haja tempo

- Melhoria 1: tela inicial com título e instrução para começar;
- Melhoria 2: sons de pulo e colisão;
- Melhoria 3: diferentes tipos de obstáculos.

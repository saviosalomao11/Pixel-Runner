# Proposta Inicial do Jogo

## 1. Nome provisorio do jogo

Pixel Runner: O Ultimo Sinal

## 2. Integrantes do grupo

- Savio Jose Salomao Ferreira da Silva
- Arthur Willian Goncalves Domingues
- Rodrigo Freitas Ribeiro Costa

## 3. Tipo de jogo

Jogo de desviar de obstaculos, no estilo corrida com pulo e agachamento.

## 4. Descricao geral

O jogador controla BITS, um robo explorador que corre automaticamente por um planeta em colapso. Para chegar a nave de resgate, BITS precisa desviar de fissuras no chao e rochas suspensas, alem de coletar celulas de energia que aumentam a pontuacao.

## 5. Objetivo do jogador

Percorrer 1000 metros ate a nave de resgate sem perder todas as 3 vidas.

## 6. Regras principais

- BITS corre automaticamente.
- O jogador pula para evitar fissuras no chao.
- O jogador agacha para evitar rochas suspensas.
- Cada colisao remove 1 vida.
- Celulas de energia concedem 50 pontos e um bonus temporario de velocidade.
- A velocidade aumenta a cada 200 metros percorridos.
- A partida termina quando BITS chega a 1000 metros ou perde todas as vidas.

## 7. Condicao de vitoria

O jogador vence quando a distancia chega a 1000 metros com pelo menos 1 vida restante. A tela final mostra a mensagem "BITS foi resgatado!" e a pontuacao final.

## 8. Condicao de derrota ou encerramento

O jogador perde quando as vidas chegam a 0. A tela de Game Over mostra a pontuacao final e permite reiniciar com `R` ou sair com `ESC`.

## 9. Elementos previstos

- Jogador: BITS, representado por um personagem verde do pacote Kenney New Platformer Pack.
- Obstaculos: fissuras/espinhos no chao e blocos suspensos.
- Itens: celulas de energia coletaveis representadas por uma gema azul.
- Indicadores: pontos, vidas com icones de coracao, distancia, barra de progresso e recorde.

## 10. Controles previstos

- `ESPACO` ou `SETA PARA CIMA`: pular.
- `S` ou `SETA PARA BAIXO`: agachar.
- `R`: reiniciar apos vitoria ou derrota.
- `ESC`: sair do jogo.

## 11. Estruturas de dados utilizadas

- Dicionario para armazenar o estado geral da partida.
- Lista para armazenar os obstaculos ativos.
- Retangulos do Pygame para colisao entre jogador, obstaculos e itens.

## 12. Uso previsto de arquivos

O arquivo `data/recorde.txt` guarda a maior pontuacao obtida. As funcoes de leitura e escrita estao no modulo `src/dados.py`.

Tambem sao utilizados assets livres do pacote Kenney New Platformer Pack, armazenados em `assets/kenney/new-platformer-pack/`, com licenca CC0 registrada no README.

## 13. Testes planejados

Os testes cobrem calculo de pontos, dano, derrota, vitoria, limite de valores, aumento de velocidade, pontos por distancia e leitura/escrita de recorde.

## 14. Principais dificuldades esperadas

- Ajustar a fisica do pulo para ficar responsiva.
- Gerar obstaculos sem deixar o jogo impossivel.
- Manter pontuacao, vidas, progresso e recorde sincronizados.

## 15. Escopo minimo para a entrega final

Jogo executavel com Pygame, controle por teclado, obstaculos, itens, vidas, pontuacao, progresso, condicao de vitoria, condicao de derrota, recorde salvo em arquivo, README preenchido e testes simples.

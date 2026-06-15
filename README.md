# Pixel Runner: O Ultimo Sinal

Projeto final da disciplina de Introducao a Algoritmos/Programacao, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Savio Jose Salomao Ferreira da Silva
- Arthur Willian Goncalves Domingues
- Rodrigo Freitas Ribeiro Costa

## Descricao do jogo

Pixel Runner e um jogo de corrida com obstaculos. O jogador controla BITS, um robo explorador branco e azul que precisa chegar a nave de resgate antes de perder todas as vidas. Durante a corrida aparecem fissuras no chao, rochas suspensas e celulas de energia.

## Objetivo do jogador

Percorrer 1000 metros, desviar dos obstaculos e manter pelo menos 1 vida ate o fim da fase. A pontuacao aumenta com a distancia percorrida e tambem com a coleta de celulas de energia.

## Regras do jogo

- O mapa avanca automaticamente da esquerda para a direita e nunca retrocede.
- BITS pode se mover para frente e para tras na tela; mover para frente tambem acelera o avanco no mapa, mas mover para tras nao faz o mapa (e a distancia percorrida) retroceder.
- Fissuras no chao devem ser evitadas pulando.
- Rochas suspensas devem ser evitadas agachando.
- Cada colisao remove 1 vida.
- O jogador comeca com 3 vidas.
- Coletar uma celula de energia concede 50 pontos e aumenta a velocidade por alguns segundos.
- A velocidade aumenta a cada 200 metros.
- A partida termina em vitoria ao chegar a 1000 metros.
- A partida termina em derrota quando as vidas chegam a 0.
- O recorde de pontuacao e salvo em `data/recorde.txt`.

## Telas do jogo

- **Menu inicial**: tela de "Start Game" com titulo, instrucoes e recorde. Pressione `ESPACO` ou `ENTER` para comecar.
- **Pausa**: pressione `P` ou `ESC` durante a partida para pausar/retomar (funciona como "Resume").
- **Fim de jogo**: tela de vitoria ou derrota com a pontuacao final.

## Controles

- `SETA PARA CIMA` ou `ESPACO`: pular
- `SETA PARA BAIXO` ou `S`: agachar
- `SETA PARA DIREITA` ou `D`: mover para frente (avanca no mapa)
- `SETA PARA ESQUERDA` ou `A`: mover para tras (nao retrocede o mapa)
- `P` ou `ESC`: pausar/retomar o jogo
- `R`: reiniciar depois da vitoria ou derrota
- `ESC`: sair do jogo (no menu ou apos vitoria/derrota)

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicacao.
- `src/jogo.py`: loop principal, eventos, desenho, regras e interacoes do jogo.
- `src/funcoes.py`: funcoes de logica usadas pelo jogo e pelos testes.
- `src/dados.py`: leitura e escrita do recorde.
- `src/config.py`: constantes de tela, cores, pontuacao, vidas e caminhos.
- `data/`: arquivos persistentes, como recorde e ranking.
- `tests/`: testes unitarios com `pytest`.
- `docs/proposta.MD`: proposta inicial do jogo.

## Conceitos utilizados

O projeto utiliza variaveis, condicionais, lacos, listas de obstaculos, dicionarios para o estado do jogo, funcoes, modularizacao, leitura e escrita de arquivo e testes automatizados para funcoes de logica.

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Assets e recursos externos

O projeto mantem a estrutura de assets do template oficial da disciplina e utiliza recursos livres indicados no material de apoio:

- `assets/kenney/new-platformer-pack/`: recortes de terreno, coracoes, gema, espinhos, inimigo/bloco e sons do pacote **New Platformer Pack**, criado por Kenney.
- Origem: https://kenney.nl/assets/new-platformer-pack
- Licenca: Creative Commons Zero (CC0), conforme `assets/kenney/new-platformer-pack/License.txt`.

O robo BITS, o planeta, a nave de resgate, o ceu estrelado, a barra de progresso, o menu e o HUD foram desenhados diretamente no codigo com funcoes do Pygame, usando uma paleta de azuis/cinzas inspirada na arte de referencia do personagem.

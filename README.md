# Pixel Runner: O Ultimo Sinal

## Integrantes

- Savio Jose Salomao Ferreira da Silva
- Arthur Willian Goncalves Domingues
- Rodrigo Freitas Ribeiro Costa

## Resumo do jogo

Pixel Runner: O Ultimo Sinal e um jogo 2D de corrida com obstaculos. O jogador controla BITS, um robo explorador que precisa atravessar uma base em ruinas, coletar itens de energia e chegar ate a nave de resgate antes de perder todas as vidas.

O jogo tem menu inicial, fase principal, colisao com obstaculos, coleta de itens, pontuacao, vidas, pausa, tela final de vitoria ou derrota, recorde salvo em arquivo e testes de logica.

## Objetivo

O objetivo e chegar a 1000 metros de distancia, encontrar a nave de resgate e encostar nela com pelo menos 1 vida restante.

A pontuacao nao aumenta pela distancia. Os pontos sao ganhos apenas quando o jogador coleta itens.

## Regras principais

- BITS corre automaticamente enquanto o mapa avanca.
- O jogador pode andar para frente e para tras dentro da tela.
- O jogador pode pular para escapar de obstaculos baixos.
- O jogador pode agachar para escapar de obstaculos altos ou suspensos.
- Cada colisao com obstaculo tira vida.
- Depois de sofrer dano, BITS fica invencivel por um curto periodo.
- O jogador comeca com 3 vidas.
- Energia vale 50 pontos e ativa bonus temporario de velocidade.
- Moeda de ouro vale 100 pontos.
- Cristal vale 150 pontos e recupera 1 vida, sem passar do limite inicial.
- A velocidade aumenta conforme a distancia percorrida.
- A vitoria acontece quando BITS chega ao final e toca a nave.
- A derrota acontece quando as vidas chegam a 0.

## Controles

- `ESPACO` ou `SETA PARA CIMA`: pular
- `S` ou `SETA PARA BAIXO`: agachar
- `D` ou `SETA PARA DIREITA`: andar para frente
- `A` ou `SETA PARA ESQUERDA`: andar para tras
- `P`: pausar ou continuar
- `ESC`: pausar durante o jogo ou sair fora da partida
- `R`: reiniciar depois da vitoria ou derrota

## Como executar

Entre na pasta do projeto:

```bash
cd Pixel-Runner
```

Instale a dependencia:

```bash
pip install -r requirements.txt
```

Execute o jogo:

```bash
python main.py
```

## Como executar os testes

Na pasta `Pixel-Runner`, rode:

```bash
python -m pytest tests
```

Se o pytest tentar usar cache e der problema de permissao no Windows, rode:

```bash
python -m pytest tests -p no:cacheprovider
```

## Estrutura do projeto

- `main.py`: arquivo inicial que chama o jogo.
- `requirements.txt`: dependencia principal do projeto.
- `src/config.py`: constantes do jogo, como tela, cores, vidas, pontuacao e caminhos.
- `src/funcoes.py`: funcoes simples de logica usadas tambem nos testes.
- `src/dados.py`: leitura e escrita do recorde.
- `src/jogo.py`: loop principal, eventos, atualizacao, colisao, sons e desenho.
- `src/sprites.py`: funcao auxiliar para carregar spritesheet.
- `assets/`: imagens, sons e recursos usados pelo jogo.
- `data/`: arquivos de dados, como recorde e ranking.
- `docs/proposta.md`: proposta final do jogo.
- `tests/test_logica.py`: testes automatizados da logica.


## Conceitos da disciplina utilizados

- Variaveis para guardar vidas, pontos, distancia e velocidade.
- Condicionais para decidir vitoria, derrota, dano e coleta.
- Lacos para manter o jogo rodando e atualizar os elementos.
- Listas para armazenar obstaculos e itens ativos.
- Dicionarios para organizar o estado geral da partida.
- Funcoes para separar partes da logica.
- Modularizacao com arquivos em `src/`.
- Leitura e escrita de arquivo para salvar o recorde.
- Testes automatizados para conferir regras importantes.

## Testes implementados

Os testes verificam:

- Soma de pontos.
- Dano sem deixar vida negativa.
- Condicao de derrota.
- Condicao de vitoria.
- Limite de valores.
- Aumento de velocidade.
- Avanco de distancia sem retroceder.
- Leitura e escrita do recorde.
- Pontuacao acumulada apenas por itens coletados.

## Recursos visuais e sonoros

O projeto usa imagens e sons locais dentro da pasta `assets/`.

Recursos externos utilizados:

- Kenney New Platformer Pack
- Origem: https://kenney.nl/assets/new-platformer-pack
- Licenca: Creative Commons Zero (CC0)
- Arquivo de licenca: `assets/kenney/new-platformer-pack/License.txt`

Tambem foram usados recursos visuais organizados pelo grupo em `assets/imagens/`, como BITS, fundo, nave, obstaculos e itens. Os sons finais ficam em `assets/sons/` e foram gerados para combinar com a proposta sci-fi/arcade do jogo.



# Proposta Final do Jogo

## 1. Nome do jogo

Pixel Runner: O Ultimo Sinal

## 2. Integrantes do grupo

- Savio Jose Salomao Ferreira da Silva
- Arthur Willian Goncalves Domingues
- Rodrigo Freitas Ribeiro Costa

## 3. Tipo de jogo

Jogo 2D de corrida com obstaculos, coleta de itens, pulo, agachamento, pontuacao, vidas e fase com final definido.

## 4. Ideia geral

O jogador controla BITS, um robo explorador que esta preso em uma base em ruinas. Para escapar, ele precisa correr ate a nave de resgate, desviando de obstaculos e coletando itens pelo caminho.

A fase avanca automaticamente. O jogador precisa reagir aos perigos usando pulo, agachamento e movimentacao lateral. A partida termina quando BITS chega ate a nave ou quando perde todas as vidas.

## 5. Objetivo do jogador

Chegar a 1000 metros de distancia e encostar na nave de resgate com pelo menos 1 vida.

O jogador tambem pode tentar fazer uma pontuacao maior coletando itens. A pontuacao e salva como recorde quando for maior que a pontuacao anterior.

## 6. Regras do jogo

- BITS comeca com 3 vidas.
- O mapa avanca automaticamente.
- O jogador pode andar para esquerda e direita dentro da tela.
- O jogador pode pular.
- O jogador pode agachar.
- Obstaculos causam dano.
- Depois de sofrer dano, BITS fica invencivel por um curto tempo.
- Energia vale 50 pontos.
- Moeda de ouro vale 100 pontos.
- Cristal vale 150 pontos e recupera 1 vida.
- A pontuacao aumenta apenas quando o jogador coleta itens.
- A velocidade aumenta gradualmente durante a fase.
- A partida termina em vitoria quando BITS chega na nave.
- A partida termina em derrota quando as vidas chegam a 0.

## 7. Controles

- `ESPACO` ou `SETA PARA CIMA`: pular.
- `S` ou `SETA PARA BAIXO`: agachar.
- `D` ou `SETA PARA DIREITA`: andar para frente.
- `A` ou `SETA PARA ESQUERDA`: andar para tras.
- `P`: pausar ou continuar.
- `ESC`: pausar durante o jogo ou sair fora da partida.
- `R`: reiniciar depois da vitoria ou derrota.

## 8. Elementos do jogo

### Jogador

BITS e o personagem controlado pelo jogador. Ele possui animacoes para corrida, pulo, agachamento e dano.

### Obstaculos

O jogo possui varios tipos de obstaculos:

- Espinhos.
- Rochas.
- Robo inimigo.
- Drone.
- Lasers.
- Bola de energia.
- Missil.
- Bomba.
- Agua.

Cada obstaculo exige atencao do jogador, pois pode tirar vida ao colidir com BITS.

### Itens

O jogo possui tres tipos principais de itens:

- Energia: soma pontos e ativa bonus de velocidade.
- Moeda de ouro: soma mais pontos.
- Cristal: soma pontos e recupera vida.

### Audio

O jogo possui sons diferentes para pulo, coleta de itens, impactos, lasers, explosoes, agua, pausa, inicio, vitoria e derrota.

## 9. Telas do jogo

- Menu inicial: mostra o nome do jogo, instrucoes e recorde.
- Tela principal: mostra a fase, BITS, obstaculos, itens, pontuacao, vidas, distancia e recorde.
- Tela de pausa: aparece quando o jogador pausa a partida.
- Tela final: mostra se o jogador venceu ou perdeu, a pontuacao final, itens coletados e recorde.

## 10. Condicao de vitoria

O jogador vence quando chega a 1000 metros, a nave aparece na tela e BITS encosta nela com pelo menos 1 vida.

## 11. Condicao de derrota

O jogador perde quando as vidas chegam a 0.

## 12. Organizacao do codigo

O projeto foi separado em pastas para facilitar a leitura:

- `main.py`: inicia o jogo.
- `src/jogo.py`: contem o loop principal, eventos, colisao, desenho, sons e regras da partida.
- `src/config.py`: guarda constantes do jogo.
- `src/funcoes.py`: guarda funcoes simples de logica.
- `src/dados.py`: cuida da leitura e escrita do recorde.
- `assets/`: guarda imagens e sons.
- `data/`: guarda arquivos de dados.
- `tests/`: guarda os testes.
- `docs/`: guarda documentos do projeto.

## 13. Estruturas de dados utilizadas

- Variaveis para guardar pontos, vidas, distancia, velocidade e estado do jogo.
- Listas para guardar os obstaculos e itens que estao aparecendo na tela.
- Dicionarios para guardar o estado geral da partida.
- Retangulos do Pygame para controlar posicao e colisao.

## 14. Leitura e escrita em arquivo

O arquivo `data/recorde.txt` guarda a maior pontuacao obtida.

As funcoes do arquivo `src/dados.py` fazem:

- Leitura do recorde.
- Gravacao do recorde.
- Atualizacao somente quando a nova pontuacao e maior.

Esse recurso atende ao requisito de leitura e escrita em arquivo.

## 15. Testes implementados

Os testes estao em `tests/test_logica.py`.

Eles verificam:

- Calculo de pontos.
- Dano sem deixar vida negativa.
- Condicao de derrota.
- Condicao de vitoria.
- Limitacao de valores.
- Aumento de velocidade.
- Avanco de distancia.
- Leitura e escrita do recorde.
- Pontuacao apenas por coleta de itens.

Para executar:

```bash
python -m pytest tests
```

## 16. Recursos externos utilizados

O projeto utiliza recursos do pacote Kenney New Platformer Pack:

- Site: https://kenney.nl/assets/new-platformer-pack
- Licenca: Creative Commons Zero (CC0)
- Licenca local: `assets/kenney/new-platformer-pack/License.txt`

Tambem existem imagens e sons organizados pelo grupo nas pastas `assets/imagens/` e `assets/sons/`.

## 17. Principais desafios

Durante o desenvolvimento, os principais desafios foram:

- Ajustar a movimentacao para o personagem nao flutuar.
- Controlar a quantidade de obstaculos e itens na tela.
- Fazer a pontuacao contar apenas pela coleta de itens.
- Ajustar a colisao para ficar mais justa.
- Organizar os arquivos em modulos.
- Criar testes simples para as regras principais.
- Melhorar os sons para combinar com cada acao do jogo.

## 18. Resultado final

A versao final possui loop principal funcionando, controles por teclado, colisao, itens coletaveis, pontuacao, vidas, vitoria, derrota, recorde salvo em arquivo, sons, imagens, documentacao e testes.

O projeto esta pronto para a entrega final da Semana 4.

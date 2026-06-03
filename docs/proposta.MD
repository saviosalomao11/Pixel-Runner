# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

> Pixel Runner: O Último Sinal

## 2. Integrantes do grupo

- Nome 1: Sávio José Salomão Ferreira da Silva
- Nome 2: Arthur Willian Gonçalves Domingues
- Nome 3: Rodrigo Freitas Ribeiro Costa

## 3. Tipo de jogo

> Jogo de desviar de obstáculos (corrida infinita com pulo e agachamento).

## 4. Descrição geral do jogo

> Na tela aparece um planeta em colapso rolando da direita para a esquerda. O jogador controla BITS, um robô explorador abandonado que precisa correr até sua nave de resgate antes que o planeta imploda. Durante a corrida, dois tipos de obstáculos surgem no caminho: rochas que caem do céu, que devem ser evitadas agachando, e fissuras que abrem no chão, que devem ser evitadas pulando. Células de energia aparecem pelo caminho e podem ser coletadas para ganhar pontos extras e um breve aumento de velocidade. A cada 200 metros percorridos a velocidade aumenta, intensificando a sensação de urgência. A meta é percorrer 1000 metros até a nave de resgate antes de perder todas as vidas.

## 5. Objetivo do jogador

> Percorrer 1000 metros até a nave de resgate sem perder todas as 3 vidas, desviando de detritos e coletando células de energia pelo caminho. A cada vitória, a distância necessária aumenta 30%, tornando as rodadas seguintes progressivamente mais desafiadoras.

## 6. Regras principais

- BITS corre automaticamente; o jogador controla apenas o pulo e o agachamento.
- Fissuras no chão devem ser evitadas pulando com `ESPAÇO` ou `↑`.
- Rochas que caem do céu devem ser evitadas agachando com `↓`.
- Colidir com qualquer obstáculo remove 1 vida.
- Coletar uma célula de energia concede 50 pontos e aumenta a velocidade por 3 segundos.
- A velocidade base de BITS aumenta a cada 200 metros percorridos.
- A partida termina quando o jogador perde as 3 vidas ou percorre os 1000 metros.
- Ao vencer, a meta da próxima rodada aumenta 30% em relação à anterior.
- O recorde é salvo em arquivo ao final de cada partida, registrando a pontuação e o número da tentativa.

## 7. Condição de vitória

> O jogador vence ao percorrer 1000 metros e chegar à nave de resgate com pelo menos 1 vida restante. Uma tela de vitória exibe a mensagem *"BITS foi resgatado!"* junto com a pontuação final. O recorde é salvo e a próxima rodada aumenta a meta em 30%.

## 8. Condição de derrota ou encerramento

> A partida termina quando BITS perde todas as 3 vidas ao colidir com rochas ou fissuras. Uma tela de Game Over exibe a distância percorrida, a pontuação final e o recorde salvo. O jogador pode pressionar `R` para reiniciar.

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

> BITS, um robô explorador representado por um sprite retirado do spritesheet do template. Posicionado no lado esquerdo da tela, corre automaticamente e responde a comandos de pulo (`ESPAÇO` ou `↑`) e agachamento (`↓`).

### Obstáculos, inimigos ou desafios

> Dois tipos de obstáculos surgem do lado direito da tela e se movem para a esquerda:
> - **Fissuras no chão**: aberturas no terreno que exigem que o jogador pule para cruzá-las;
> - **Rochas em queda**: detritos que caem do céu e exigem que o jogador agache para passar por baixo.
> A velocidade de ambos aumenta a cada 200 metros percorridos.

## Itens, alvos ou objetos de interação

> **Células de energia**: itens coletáveis que aparecem em posições aleatórias ao longo do percurso. Ao coletar uma célula, o jogador ganha 50 pontos e BITS recebe um aumento temporário de velocidade por 3 segundos, permitindo passar por sequências difíceis mais rapidamente.

## Pontuação, vidas, tempo ou progresso

> O jogador começa com 3 vidas. A pontuação aumenta automaticamente com a distância percorrida (1 ponto por metro) e recebe bônus de 50 pontos a cada célula de energia coletada. A distância percorrida é exibida na tela como uma barra de progresso até os 1000 metros. O recorde registra a pontuação final e o número da tentativa, salvo em `data/recorde.txt`.

## 10. Controles previstos

- `ESPAÇO` ou `↑`: pular (desviar de fissuras no chão)
- `↓`: agachar (desviar de rochas em queda)
- `R`: reiniciar após Game Over ou vitória
- `ESC`: sair do jogo

## 11. Organização inicial do código

- `main.py`: inicia o jogo chamando `executar_jogo()`;
- `src/jogo.py`: contém o loop principal, lógica de colisão, controle de vidas e progressão de velocidade;
- `src/config.py`: guarda configurações como tamanho da tela, FPS, cores, meta de distância e caminhos de arquivo;
- `src/funcoes.py`: contém funções auxiliares de lógica (calcular pontos, verificar colisão, checar vitória e derrota, limitar posição);
- `src/dados.py`: contém funções de leitura e escrita do recorde em `data/recorde.txt`.

## 12. Recursos externos previstos

> Sprites retirados do spritesheet fornecido pelo template da disciplina (`assets/imagens/spritesheet.bmp`). Não pretendemos utilizar recursos externos adicionais.

## 13. Principais dificuldades esperadas

- Dificuldade 1: implementar a física do pulo e do agachamento com gravidade de forma suave e responsiva;
- Dificuldade 2: gerar os dois tipos de obstáculos (fissuras e rochas) em intervalos aleatórios sem sobreposição;
- Dificuldade 3: aumentar a velocidade progressivamente a cada 200 metros sem tornar o jogo injogável.

## 14. Escopo mínimo para a entrega final

> A versão mínima terá: BITS controlado pelo teclado com mecânica de pulo e agachamento, fissuras e rochas surgindo automaticamente, sistema de 3 vidas, pontuação e barra de progresso até 1000 metros na tela, tela de vitória e tela de Game Over, recorde salvo em arquivo registrando pontuação e número da tentativa.

## 15. Possíveis melhorias, caso haja tempo

- Melhoria 1: tela inicial com título, história resumida e instrução para começar;
- Melhoria 2: sons de pulo, coleta de célula de energia e colisão;
- Melhoria 3: animação de explosão do planeta ao fundo conforme BITS se aproxima da nave.
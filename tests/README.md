# Testes

Esta pasta contem os testes automatizados do projeto.

## Arquivo

- `test_logica.py`: testa funcoes de logica usadas pelo jogo.

## Como executar

Na pasta principal do projeto, rode:

```bash
python -m pytest tests
```

## O que os testes verificam

- Soma de pontos.
- Dano sem deixar vida negativa.
- Condicao de derrota.
- Condicao de vitoria.
- Limite minimo e maximo de valores.
- Aumento de velocidade.
- Avanco de distancia.
- Leitura e escrita do recorde.
- Pontuacao apenas por itens coletados.

Esses testes ajudam a conferir se as regras principais continuam funcionando mesmo depois de alteracoes no codigo.

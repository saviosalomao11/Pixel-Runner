from pathlib import Path

from src.dados import atualizar_recorde, carregar_recorde
from src.funcoes import (
    avancar_distancia,
    calcular_pontos,
    calcular_velocidade,
    jogador_perdeu,
    jogador_venceu,
    limitar_valor,
    tomar_dano,
)


def caminho_recorde_teste():
    caminho = Path("data") / "recorde_teste.txt"
    if caminho.exists():
        caminho.unlink()
    return caminho


def test_calcular_pontos():
    assert calcular_pontos(10, 5) == 15


def test_tomar_dano_nao_deixa_vida_negativa():
    assert tomar_dano(1, 3) == 0


def test_jogador_perdeu_com_zero_vidas():
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    assert jogador_perdeu(3) is False


def test_jogador_venceu_ao_atingir_meta():
    assert jogador_venceu(1000, 1000) is True


def test_jogador_nao_venceu_antes_da_meta():
    assert jogador_venceu(999, 1000) is False


def test_limitar_valor_abaixo_do_minimo():
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    assert limitar_valor(50, 0, 100) == 50


def test_calcular_velocidade_aumenta_a_cada_200_metros():
    assert calcular_velocidade(0) == 6
    assert calcular_velocidade(200) == 7
    assert calcular_velocidade(450) == 8


def test_recorde_carrega_zero_quando_arquivo_nao_existe():
    caminho = caminho_recorde_teste()
    assert carregar_recorde(caminho) == 0


def test_atualizar_recorde_mantem_maior_pontuacao():
    caminho = caminho_recorde_teste()
    assert atualizar_recorde(caminho, 200) == 200
    assert atualizar_recorde(caminho, 150) == 200
    assert carregar_recorde(caminho) == 200
    caminho.unlink()


def test_avancar_distancia_com_deslocamento_positivo():
    assert avancar_distancia(100, 5) == 105


def test_avancar_distancia_nao_retrocede_com_deslocamento_negativo():
    assert avancar_distancia(100, -5) == 100


def test_avancar_distancia_com_deslocamento_zero():
    assert avancar_distancia(100, 0) == 100


def test_pontuacao_soma_apenas_itens_coletados():
    pontos = 0
    pontos = calcular_pontos(pontos, 50)
    pontos = calcular_pontos(pontos, 100)
    assert pontos == 150

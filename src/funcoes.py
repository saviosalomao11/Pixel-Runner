def calcular_pontos(pontos_atual, pontos_ganhos):

    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):

    return max(0, vida_atual - dano)


def jogador_perdeu(vidas):

    return vidas <= 0


def jogador_venceu(distancia, meta):

    return distancia >= meta


def limitar_valor(valor, minimo, maximo):

    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def avancar_distancia(distancia_atual, deslocamento):

    if deslocamento <= 0:
        return distancia_atual
    return distancia_atual + deslocamento


def verificar_colisao(retangulo_1, retangulo_2):

    return retangulo_1.colliderect(retangulo_2)


def calcular_velocidade(distancia, velocidade_base=6):

    aumento = int(distancia // 200)
    return velocidade_base + aumento

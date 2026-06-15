import os
import random

import pygame

from src.config import (
    ALTURA_CHAO,
    ALTURA_TELA,
    BONUS_VELOCIDADE_MS,
    CAMINHO_RECORDE,
    COR_BARRA,
    COR_BARRA_FUNDO,
    COR_BITS_DETALHE,
    COR_BITS_VISOR,
    COR_CEU,
    COR_CEU_BAIXO,
    COR_CHAO,
    COR_CHAO_LUZ,
    COR_ENERGIA,
    COR_ENERGIA_LUZ,
    COR_FUNDO,
    COR_OBSTACULO,
    COR_PAINEL,
    COR_PLANETA,
    COR_PLANETA_LUZ,
    COR_TEXTO,
    COR_TEXTO_APAGADO,
    FPS,
    FORCA_PULO,
    GRAVIDADE,
    INVENCIVEL_MS,
    LARGURA_TELA,
    LIMITE_DIREITO_JOGADOR,
    LIMITE_ESQUERDO_JOGADOR,
    META_DISTANCIA,
    PONTOS_ENERGIA,
    VELOCIDADE_JOGADOR,
    VIDAS_INICIAIS,
)
from src.dados import atualizar_recorde, carregar_recorde
from src.funcoes import (
    avancar_distancia,
    calcular_pontos,
    calcular_pontos_por_distancia,
    calcular_velocidade,
    jogador_perdeu,
    jogador_venceu,
    limitar_valor,
    tomar_dano,
    verificar_colisao,
)

PASTA_SPRITES = os.path.join("assets", "imagens", "bits")


def criar_estado():
    random.seed(42)
    return {
        "jogador": pygame.Rect(100, ALTURA_CHAO - 58, 40, 58),
        "altura_original": 58,
        "vel_y": 0,
        "no_ar": False,
        "agachado": False,
        "movendo_esquerda": False,
        "movendo_direita": False,
        "virado_esquerda": False,
        "vidas": VIDAS_INICIAIS,
        "pontos": 0,
        "bonus_pontos": 0,
        "distancia": 0,
        "meta": META_DISTANCIA,
        "velocidade": 6,
        "bonus_ate": 0,
        "invencivel_ate": 0,
        "resultado": "menu",
        "recorde": carregar_recorde(CAMINHO_RECORDE),
        "obstaculos": [],
        "itens": [],
        "assets": None,
        "estrelas": [(random.randint(0, LARGURA_TELA), random.randint(12, 210), random.randint(1, 3)) for _ in range(55)],
        "montanhas": [(x, random.randint(205, 265), random.randint(70, 120)) for x in range(-60, LARGURA_TELA + 160, 95)],
        "proximo_obstaculo": 0,
        "proximo_item": 0,
        "deslocamento_extra": 0,
        "fase_final": False,
        "nave_rect": None,
        "moedas_coletadas": 0,
        "cristais_coletados": 0,
        "energias_coletadas": 0,
    }


def criar_obstaculo(agora=0):
    tipo = random.choice(["espinhos", "espinhos_altos", "rocha", "robo", "drone", "laser_azul", "laser_vermelho", "laser_curto", "bola_energia", "missil", "bomba", "agua"])
    if tipo == "espinhos":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 26, 66, 22)
    elif tipo == "espinhos_altos":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 36, 92, 30)
    elif tipo == "rocha":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 43, 62, 36)
    elif tipo == "robo":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 48, 54, 42)
    elif tipo == "drone":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 118, 62, 38)
    elif tipo == "laser_azul":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 102, 132, 14)
    elif tipo == "laser_vermelho":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 84, 138, 14)
    elif tipo == "laser_curto":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 112, 62, 20)
    elif tipo == "bola_energia":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 104, 28, 28)
    elif tipo == "missil":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 96, 62, 26)
    elif tipo == "agua":
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 15, 96, 13)
    else:
        retangulo = pygame.Rect(LARGURA_TELA + 20, ALTURA_CHAO - 36, 40, 32)
    obstaculo = {"tipo": tipo, "rect": retangulo, "frame": 0, "criado_em": agora}
    if tipo == "bomba":
        obstaculo["explode_em"] = agora + random.randint(450, 1200)
        obstaculo["explodindo_ate"] = 0
    return obstaculo


def criar_item():
    sorteio = random.randint(1, 100)
    if sorteio <= 6:
        tipo = "cristal"
        tamanho = 32
        altura = ALTURA_CHAO - tamanho
    elif sorteio <= 58:
        tipo = "moeda_ouro"
        tamanho = 24
        altura = random.choice([ALTURA_CHAO - 142, ALTURA_CHAO - 104, ALTURA_CHAO - 76])
    else:
        tipo = "energia"
        tamanho = 28
        altura = random.choice([ALTURA_CHAO - 132, ALTURA_CHAO - 94])
    return {"tipo": tipo, "rect": pygame.Rect(LARGURA_TELA + 30, altura, tamanho, tamanho)}


def reiniciar_estado(estado):
    recorde = estado["recorde"]
    assets = estado.get("assets")
    estado.clear()
    estado.update(criar_estado())
    estado["recorde"] = recorde
    estado["assets"] = assets
    estado["resultado"] = "jogando"


def finalizar_partida(estado, resultado):
    estado["resultado"] = resultado
    estado["recorde"] = atualizar_recorde(CAMINHO_RECORDE, estado["pontos"])


def carregar_imagem(nome):
    caminho = os.path.join(PASTA_SPRITES, f"{nome}.png")
    if os.path.exists(caminho):
        return pygame.image.load(caminho).convert_alpha()
    return None


def carregar_lista(nomes):
    return [imagem for imagem in [carregar_imagem(nome) for nome in nomes] if imagem is not None]


def carregar_assets():
    imagens = {
        "bits_parado": carregar_lista(["bits_parado"]),
        "bits_correndo": carregar_lista(["bits_correr1", "bits_correr2", "bits_correr3", "bits_correr4", "bits_correr5", "bits_corrida_extra", "bits_dash"]),
        "bits_pulando": carregar_lista(["bits_pulo"]),
        "bits_agachado": carregar_lista(["bits_agachado", "bits_agachado2"]),
        "bits_dano": carregar_lista(["bits_dano"]),
        "fundo": pygame.image.load(os.path.join("assets", "imagens", "fundo_bits.png")).convert() if os.path.exists(os.path.join("assets", "imagens", "fundo_bits.png")) else None,
        "energia": carregar_imagem("energia"),
        "moeda_azul": carregar_imagem("moeda_azul"),
        "moeda_ouro": carregar_imagem("moeda_ouro"),
        "cristal": carregar_imagem("cristal"),
        "nave": pygame.image.load(os.path.join("assets", "imagens", "nave_final.png")).convert_alpha() if os.path.exists(os.path.join("assets", "imagens", "nave_final.png")) else None,
        "laser_azul": carregar_imagem("laser_azul"),
        "laser_vermelho": carregar_imagem("laser_vermelho"),
        "laser_curto": carregar_imagem("laser_curto"),
        "bola_energia": carregar_imagem("bola_energia"),
        "missil": carregar_imagem("missil"),
        "missil_fogo": carregar_imagem("missil_fogo"),
        "espinhos": carregar_imagem("espinho1"),
        "espinhos_altos": carregar_imagem("espinho2"),
        "rocha": carregar_imagem("rocha"),
        "robo": carregar_imagem("robo_inimigo"),
        "drone": carregar_imagem("drone"),
        "bomba": carregar_lista(["bomba_azul", "bomba_laranja", "bomba_vermelha"]),
        "agua": carregar_lista(["agua1", "agua2", "agua3"]),
        "explosao": carregar_lista(["explosao1", "explosao2", "bomba_explosao"]),
        "chao": carregar_lista(["chao_longo", "chao_grama1", "chao_grama2", "chao_metal1", "bloco_pedra"]),
        "plataforma": carregar_lista(["plataforma_amarela", "plataforma_azul", "plataforma_cinza", "plataforma_listra", "plataforma_base"]),
        "base": carregar_imagem("plataforma_base"),
        "bloco": carregar_lista(["bloco_porta", "bloco_final"]),
    }
    sons = {}
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        for nome, arquivo in {"jump": "sfx_jump.ogg", "gem": "sfx_gem.ogg", "hurt": "sfx_hurt.ogg"}.items():
            caminho = os.path.join("assets", "kenney", "new-platformer-pack", "sounds", arquivo)
            if os.path.exists(caminho):
                sons[nome] = pygame.mixer.Sound(caminho)
                sons[nome].set_volume(0.35)
    except pygame.error:
        sons = {}
    return {"imagens": imagens, "sons": sons}


def tocar_som(estado, nome):
    som = (estado.get("assets") or {}).get("sons", {}).get(nome)
    if som is not None:
        som.play()


def processar_eventos(estado):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                if estado["resultado"] == "jogando":
                    estado["resultado"] = "pausado"
                elif estado["resultado"] == "pausado":
                    estado["resultado"] = "jogando"
                else:
                    return False
            if estado["resultado"] == "menu" and evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                estado["resultado"] = "jogando"
            if estado["resultado"] == "pausado" and evento.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_p):
                estado["resultado"] = "jogando"
            if estado["resultado"] not in ("jogando",) and evento.key == pygame.K_r:
                reiniciar_estado(estado)
            if estado["resultado"] == "jogando":
                if evento.key == pygame.K_p:
                    estado["resultado"] = "pausado"
                if evento.key in (pygame.K_SPACE, pygame.K_UP) and not estado["no_ar"] and not estado["agachado"]:
                    estado["vel_y"] = FORCA_PULO
                    estado["no_ar"] = True
                    tocar_som(estado, "jump")
                if evento.key in (pygame.K_DOWN, pygame.K_s) and not estado["no_ar"]:
                    estado["agachado"] = True
                    estado["jogador"].height = estado["altura_original"] // 2
                    estado["jogador"].bottom = ALTURA_CHAO
                if evento.key in (pygame.K_LEFT, pygame.K_a):
                    estado["movendo_esquerda"] = True
                if evento.key in (pygame.K_RIGHT, pygame.K_d):
                    estado["movendo_direita"] = True
        if evento.type == pygame.KEYUP and evento.key in (pygame.K_DOWN, pygame.K_s) and estado["agachado"]:
            estado["agachado"] = False
            estado["jogador"].height = estado["altura_original"]
            estado["jogador"].bottom = ALTURA_CHAO
        if evento.type == pygame.KEYUP and evento.key in (pygame.K_LEFT, pygame.K_a):
            estado["movendo_esquerda"] = False
        if evento.type == pygame.KEYUP and evento.key in (pygame.K_RIGHT, pygame.K_d):
            estado["movendo_direita"] = False
    return True


def atualizar_jogador(estado):
    if estado["no_ar"]:
        estado["vel_y"] += GRAVIDADE
        estado["jogador"].y += int(estado["vel_y"])
        if estado["jogador"].bottom >= ALTURA_CHAO:
            estado["jogador"].bottom = ALTURA_CHAO
            estado["vel_y"] = 0
            estado["no_ar"] = False
    deslocamento_extra = 0
    if estado["movendo_direita"] and not estado["movendo_esquerda"]:
        estado["jogador"].x += VELOCIDADE_JOGADOR
        estado["virado_esquerda"] = False
        deslocamento_extra = VELOCIDADE_JOGADOR
    elif estado["movendo_esquerda"] and not estado["movendo_direita"]:
        estado["jogador"].x -= VELOCIDADE_JOGADOR
        estado["virado_esquerda"] = True
    limite_direito = 625 if estado.get("fase_final") else LIMITE_DIREITO_JOGADOR
    estado["jogador"].x = limitar_valor(estado["jogador"].x, LIMITE_ESQUERDO_JOGADOR, limite_direito)
    estado["deslocamento_extra"] = deslocamento_extra


def atualizar_mundo(estado, agora):
    if estado.get("fase_final"):
        estado["velocidade"] = 0
        estado["obstaculos"].clear()
        estado["itens"].clear()
        return
    bonus = 2 if agora < estado["bonus_ate"] else 0
    estado["velocidade"] = calcular_velocidade(estado["distancia"]) + bonus
    avanco = estado["velocidade"] / FPS + estado.get("deslocamento_extra", 0) / FPS
    estado["distancia"] = min(estado["meta"], avancar_distancia(estado["distancia"], avanco))
    if estado["distancia"] >= estado["meta"]:
        estado["fase_final"] = True
        estado["obstaculos"].clear()
        estado["itens"].clear()
        estado["nave_rect"] = pygame.Rect(595, ALTURA_CHAO - 118, 185, 108)
        return
    permitir_perigos = estado["distancia"] < estado["meta"] - 90
    if permitir_perigos and agora >= estado["proximo_obstaculo"]:
        estado["obstaculos"].append(criar_obstaculo(agora))
        estado["proximo_obstaculo"] = agora + random.randint(900, 1450)
    if agora >= estado["proximo_item"] and estado["distancia"] < estado["meta"] - 70:
        quantidade = 1 if random.randint(1, 100) > 18 else 2
        for i in range(quantidade):
            item = criar_item()
            item["rect"].x += i * 46
            estado["itens"].append(item)
        estado["proximo_item"] = agora + random.randint(1700, 3200)
    for obstaculo in estado["obstaculos"]:
        tipo = obstaculo["tipo"]
        velocidade_extra = 4 if tipo in ("missil", "laser_azul", "laser_vermelho", "laser_curto", "bola_energia") else 0
        obstaculo["rect"].x -= estado["velocidade"] + velocidade_extra
        if tipo == "bomba" and agora >= obstaculo.get("explode_em", 0) and obstaculo.get("explodindo_ate", 0) == 0:
            centro = obstaculo["rect"].center
            obstaculo["explodindo_ate"] = agora + 520
            obstaculo["rect"] = pygame.Rect(centro[0] - 42, ALTURA_CHAO - 84, 84, 78)
    estado["obstaculos"] = [obs for obs in estado["obstaculos"] if obs["rect"].right > 0 and not (obs["tipo"] == "bomba" and obs.get("explodindo_ate", 0) and agora > obs["explodindo_ate"])]
    for item in estado["itens"]:
        item["rect"].x -= estado["velocidade"]
    estado["itens"] = [item for item in estado["itens"] if item["rect"].right > 0]
    estado["pontos"] = calcular_pontos_por_distancia(estado["distancia"]) + estado["bonus_pontos"]


def verificar_interacoes(estado, agora):
    itens_restantes = []
    for item in estado["itens"]:
        if verificar_colisao(estado["jogador"], item["rect"]):
            tipo = item.get("tipo")
            ganho = PONTOS_ENERGIA
            if tipo == "moeda_ouro":
                ganho = PONTOS_ENERGIA * 2
                estado["moedas_coletadas"] += 1
            elif tipo == "cristal":
                ganho = PONTOS_ENERGIA * 3
                estado["vidas"] = min(VIDAS_INICIAIS, estado["vidas"] + 1)
                estado["cristais_coletados"] += 1
            elif tipo == "energia":
                estado["energias_coletadas"] += 1
            estado["bonus_pontos"] = calcular_pontos(estado["bonus_pontos"], ganho)
            estado["pontos"] = calcular_pontos_por_distancia(estado["distancia"]) + estado["bonus_pontos"]
            tocar_som(estado, "gem")
        else:
            itens_restantes.append(item)
    estado["itens"] = itens_restantes
    if agora >= estado["invencivel_ate"]:
        for obstaculo in estado["obstaculos"]:
            tipo = obstaculo.get("tipo")
            bomba_armada = tipo == "bomba" and obstaculo.get("explodindo_ate", 0) == 0
            if bomba_armada:
                continue
            if verificar_colisao(estado["jogador"], obstaculo["rect"]):
                dano = 2 if tipo == "bomba" and obstaculo.get("explodindo_ate", 0) else 1
                estado["vidas"] = tomar_dano(estado["vidas"], dano)
                estado["invencivel_ate"] = agora + INVENCIVEL_MS
                obstaculo["rect"].right = 0
                tocar_som(estado, "hurt")
                break
    if jogador_perdeu(estado["vidas"]):
        finalizar_partida(estado, "derrota")
    elif estado.get("fase_final") and estado.get("nave_rect") and verificar_colisao(estado["jogador"], estado["nave_rect"]):
        finalizar_partida(estado, "vitoria")


def desenhar_texto(tela, fonte, texto, x, y, cor=COR_TEXTO):
    tela.blit(fonte.render(texto, True, cor), (x, y))


def desenhar_imagem(tela, imagem, rect, virar=False):
    if imagem is None:
        return False
    escala = pygame.transform.smoothscale(imagem, (rect.width, rect.height))
    if virar:
        escala = pygame.transform.flip(escala, True, False)
    tela.blit(escala, rect.topleft)
    return True


def desenhar_fundo(tela, estado, agora):
    imagens = (estado.get("assets") or {}).get("imagens", {})
    fundo = imagens.get("fundo")
    if fundo is not None:
        imagem = pygame.transform.smoothscale(fundo, (LARGURA_TELA, ALTURA_TELA))
        tela.blit(imagem, (0, 0))
        return
    for y in range(ALTURA_CHAO):
        mistura = y / ALTURA_CHAO
        cor = (
            int(COR_CEU[0] * (1 - mistura) + COR_CEU_BAIXO[0] * mistura),
            int(COR_CEU[1] * (1 - mistura) + COR_CEU_BAIXO[1] * mistura),
            int(COR_CEU[2] * (1 - mistura) + COR_CEU_BAIXO[2] * mistura),
        )
        pygame.draw.line(tela, cor, (0, y), (LARGURA_TELA, y))


def desenhar_chao(tela, estado):
    imagens = (estado.get("assets") or {}).get("imagens", {})
    pygame.draw.rect(tela, COR_CHAO, (0, ALTURA_CHAO, LARGURA_TELA, ALTURA_TELA - ALTURA_CHAO))
    pygame.draw.line(tela, COR_CHAO_LUZ, (0, ALTURA_CHAO), (LARGURA_TELA, ALTURA_CHAO), 4)
    tiles = imagens.get("chao", [])
    deslocamento = int(estado["distancia"] * estado["velocidade"]) % 260
    for i, x in enumerate(range(-260, LARGURA_TELA + 260, 260)):
        rect = pygame.Rect(x - deslocamento, ALTURA_CHAO - 6, 260, 56)
        tile = tiles[i % len(tiles)] if tiles else None
        if not desenhar_imagem(tela, tile, rect):
            pygame.draw.rect(tela, COR_CHAO, rect)


def escolher_frame(lista, agora, velocidade=110):
    if not lista:
        return None
    return lista[(agora // velocidade) % len(lista)]


def desenhar_robo(tela, rect, agachado, piscando, estado, agora):
    imagens = (estado.get("assets") or {}).get("imagens", {})
    if piscando:
        lista = imagens.get("bits_dano", [])
    elif agachado:
        lista = imagens.get("bits_agachado", [])
    elif estado["no_ar"]:
        lista = imagens.get("bits_pulando", [])
    elif estado["movendo_direita"] or estado["movendo_esquerda"] or estado["resultado"] == "jogando":
        lista = imagens.get("bits_correndo", [])
    else:
        lista = imagens.get("bits_parado", [])
    imagem = escolher_frame(lista, agora)
    if imagem is not None:
        area = pygame.Rect(rect.x - 17, rect.bottom - 68, 78, 68)
        if agachado:
            area = pygame.Rect(rect.x - 22, rect.bottom - 46, 86, 46)
        desenhar_imagem(tela, imagem, area, estado.get("virado_esquerda", False))
        return
    pygame.draw.rect(tela, COR_BITS_DETALHE, rect, border_radius=8)
    pygame.draw.rect(tela, COR_BITS_VISOR, (rect.x + 8, rect.y + 12, rect.width - 16, 16), border_radius=5)


def desenhar_movimento_velocidade(tela, rect, virado_esquerda, agora):
    direcao = 1 if virado_esquerda else -1
    base_x = rect.x if virado_esquerda else rect.right
    for i, comprimento in enumerate((22, 16, 10)):
        y = rect.y + 14 + i * 12
        fase = (agora // 60 + i * 3) % 6
        x_inicio = base_x + direcao * (10 + fase * 2)
        pygame.draw.line(tela, COR_BITS_DETALHE, (x_inicio, y), (x_inicio + direcao * comprimento, y), 2)


def desenhar_obstaculo(tela, obstaculo):
    imagens = obstaculo.get("assets", {})
    rect = obstaculo["rect"]
    tipo = obstaculo["tipo"]
    agora = pygame.time.get_ticks()
    if tipo == "agua":
        imagem = escolher_frame(imagens.get("agua", []), agora, 150)
    elif tipo == "bomba":
        if obstaculo.get("explodindo_ate", 0):
            imagem = escolher_frame(imagens.get("explosao", []), agora, 95)
        else:
            imagem = escolher_frame(imagens.get("bomba", []), agora, 180)
    elif tipo == "missil":
        imagem = escolher_frame([imagens.get("missil"), imagens.get("missil_fogo")], agora, 120)
    else:
        imagem = imagens.get(tipo)
    if desenhar_imagem(tela, imagem, rect):
        return
    cor = COR_ENERGIA if tipo in ("drone", "agua", "laser_azul") else COR_OBSTACULO
    pygame.draw.rect(tela, cor, rect, border_radius=7)


def desenhar_item(tela, item, agora):
    imagens = getattr(desenhar_item, "imagens", {})
    rect = item["rect"]
    sprite = imagens.get(item.get("tipo", "energia"))
    pulso = 2 if (agora // 180) % 2 == 0 else 0
    pygame.draw.ellipse(tela, (31, 104, 139), rect.inflate(8 + pulso, 8 + pulso))
    if not desenhar_imagem(tela, sprite, rect.inflate(6, 6)):
        pygame.draw.circle(tela, COR_ENERGIA, rect.center, rect.width // 2)
        pygame.draw.circle(tela, COR_ENERGIA_LUZ, rect.center, rect.width // 4)



def desenhar_nave(tela, estado):
    rect = estado.get("nave_rect")
    if rect is None:
        return
    imagens = (estado.get("assets") or {}).get("imagens", {})
    sombra = pygame.Rect(rect.x + 10, rect.bottom - 6, rect.width - 20, 12)
    pygame.draw.ellipse(tela, (10, 12, 22), sombra)
    if not desenhar_imagem(tela, imagens.get("nave"), rect):
        pygame.draw.rect(tela, (220, 226, 235), rect, border_radius=18)
        pygame.draw.rect(tela, COR_BITS_DETALHE, (rect.x + 20, rect.y + 22, 70, 34), border_radius=12)
        pygame.draw.rect(tela, COR_BITS_DETALHE, (rect.right - 45, rect.y + 50, 28, 16), border_radius=5)

def desenhar_hud(tela, fonte, estado):
    pygame.draw.rect(tela, COR_PAINEL, (16, 12, 366, 106), border_radius=8)
    pygame.draw.rect(tela, (71, 85, 113), (16, 12, 366, 106), 2, border_radius=8)
    progresso = min(1, estado["distancia"] / estado["meta"])
    pygame.draw.rect(tela, COR_BARRA_FUNDO, (34, 28, 286, 14), border_radius=7)
    pygame.draw.rect(tela, COR_BARRA, (34, 28, int(286 * progresso), 14), border_radius=7)
    pygame.draw.circle(tela, (210, 220, 230), (34 + int(286 * progresso), 35), 6)
    desenhar_texto(tela, fonte, f"Pontos {estado['pontos']}", 34, 51)
    texto_distancia = "Encontre a nave" if estado.get("fase_final") else f"Distancia {int(estado['distancia'])}/{estado['meta']} m"
    desenhar_texto(tela, fonte, texto_distancia, 34, 82, COR_TEXTO_APAGADO)
    desenhar_texto(tela, fonte, f"Recorde {estado['recorde']}", 606, 22, COR_TEXTO_APAGADO)
    for i in range(VIDAS_INICIAIS):
        x = 335 + i * 18
        cor = COR_OBSTACULO if i < estado["vidas"] else (63, 68, 84)
        pygame.draw.circle(tela, cor, (x, 59), 7)
        pygame.draw.rect(tela, cor, (x - 6, 59, 12, 9), border_radius=2)


def texto_centralizado(tela, fonte, texto, y, cor=COR_TEXTO):
    superficie = fonte.render(texto, True, cor)
    tela.blit(superficie, (LARGURA_TELA // 2 - superficie.get_width() // 2, y))


def classificar_pontuacao(pontos, venceu=False):
    if venceu and pontos >= 1200:
        return "Classificacao S", "Final perfeito, você é demais!!!"
    if venceu:
        return "Classificacao A", "Missao concluida: BITS chegou à nave."
    if pontos >= 700:
        return "Classificacao B", "Quase conseguiu escapar"
    if pontos >= 350:
        return "Classificacao C", "Você falhou, mas chegou perto!"
    return "Classificacao D", "Mais sorte da próxima vez."


def desenhar_menu(tela, fonte, fonte_grande, estado):
    desenhar_fundo(tela, estado, 0)
    sombra = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
    sombra.fill((4, 5, 12, 70))
    tela.blit(sombra, (0, 0))
    painel = pygame.Rect(210, 84, 380, 214)
    pygame.draw.rect(tela, COR_PAINEL, painel, border_radius=12)
    pygame.draw.rect(tela, COR_BITS_DETALHE, painel, 2, border_radius=12)
    texto_centralizado(tela, fonte_grande, "PIXEL RUNNER", painel.y + 14)
    texto_centralizado(tela, fonte, "O Ultimo Sinal", painel.y + 48, COR_TEXTO_APAGADO)
    texto_centralizado(tela, fonte, "Leve BITS ate a nave", painel.y + 100, COR_TEXTO)
    texto_centralizado(tela, fonte, "ESPACO/ENTER para Comecar", painel.y + 125, COR_BITS_DETALHE)
    texto_centralizado(tela, fonte, "Mover: A,S,W,D ou Setas", painel.y + 185, COR_TEXTO_APAGADO)
    texto_centralizado(tela, fonte, f"Recorde: {estado['recorde']}", painel.y + 215, COR_TEXTO_APAGADO)


def desenhar_pausa(tela, fonte, fonte_grande, estado):
    sombra = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
    sombra.fill((4, 5, 12, 155))
    tela.blit(sombra, (0, 0))
    painel = pygame.Rect(245, 128, 310, 132)
    pygame.draw.rect(tela, COR_PAINEL, painel, border_radius=10)
    pygame.draw.rect(tela, COR_BITS_DETALHE, painel, 2, border_radius=10)
    texto_centralizado(tela, fonte_grande, "PAUSADO", painel.y + 22)
    texto_centralizado(tela, fonte, "ESPACO ou P - Continuar", painel.y + 72, COR_TEXTO_APAGADO)
    texto_centralizado(tela, fonte, "R - Reiniciar    ESC - Sair", painel.y + 100, COR_TEXTO_APAGADO)


def desenhar(tela, fonte, fonte_grande, estado, agora):
    if estado["resultado"] == "menu":
        desenhar_menu(tela, fonte, fonte_grande, estado)
        if pygame.display.get_surface() is tela:
            pygame.display.flip()
        return
    tela.fill(COR_FUNDO)
    desenhar_fundo(tela, estado, agora)
    desenhar_chao(tela, estado)
    desenhar_nave(tela, estado)
    piscando = agora < estado["invencivel_ate"] and (agora // 100) % 2 == 0
    desenhar_robo(tela, estado["jogador"], estado["agachado"], piscando, estado, agora)
    if estado["resultado"] == "jogando" and (estado["movendo_direita"] or estado["movendo_esquerda"]) and not estado["no_ar"]:
        desenhar_movimento_velocidade(tela, estado["jogador"], estado["virado_esquerda"], agora)
    imagens = (estado.get("assets") or {}).get("imagens", {})
    for obstaculo in estado["obstaculos"]:
        obstaculo["assets"] = imagens
        desenhar_obstaculo(tela, obstaculo)
    desenhar_item.imagens = imagens
    for item in estado["itens"]:
        desenhar_item(tela, item, agora)
    desenhar_hud(tela, fonte, estado)
    if estado["resultado"] in ("derrota", "vitoria"):
        sombra = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
        sombra.fill((4, 5, 12, 95))
        tela.blit(sombra, (0, 0))
        painel = pygame.Rect(205, 92, 390, 220)
        pygame.draw.rect(tela, COR_PAINEL, painel, border_radius=12)
        pygame.draw.rect(tela, COR_TEXTO, painel, 2, border_radius=12)
        titulo = "MISSAO CONCLUIDA" if estado["resultado"] == "vitoria" else "FIM DE JOGO"
        classe, mensagem = classificar_pontuacao(estado["pontos"], estado["resultado"] == "vitoria")
        texto_centralizado(tela, fonte_grande, titulo, painel.y + 22)
        texto_centralizado(tela, fonte, f"Pontuacao: {estado['pontos']}", painel.y + 64)
        texto_centralizado(tela, fonte, f"Moedas: {estado['moedas_coletadas']}  Energia: {estado['energias_coletadas']}  Cristais: {estado['cristais_coletados']}", painel.y + 92, COR_TEXTO_APAGADO)
        texto_centralizado(tela, fonte, classe, painel.y + 120, COR_BITS_DETALHE)
        texto_centralizado(tela, fonte, mensagem, painel.y + 148, COR_TEXTO_APAGADO)
        texto_centralizado(tela, fonte, f"Recorde: {estado['recorde']}", painel.y + 172, COR_TEXTO_APAGADO)
        texto_centralizado(tela, fonte, "R - Reiniciar    ESC - Sair", painel.y + 196)
    elif estado["resultado"] == "pausado":
        desenhar_pausa(tela, fonte, fonte_grande, estado)
    if pygame.display.get_surface() is tela:
        pygame.display.flip()


def executar_jogo():
    os.makedirs("data", exist_ok=True)
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Pixel Runner: O Ultimo Sinal")
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 20)
    fonte_grande = pygame.font.SysFont("arial", 30, bold=True)
    estado = criar_estado()
    estado["assets"] = carregar_assets()
    rodando = True
    while rodando:
        agora = pygame.time.get_ticks()
        rodando = processar_eventos(estado)
        if estado["resultado"] == "jogando":
            atualizar_jogador(estado)
            atualizar_mundo(estado, agora)
            verificar_interacoes(estado, agora)
        desenhar(tela, fonte, fonte_grande, estado, agora)
        relogio.tick(FPS)
    pygame.quit()

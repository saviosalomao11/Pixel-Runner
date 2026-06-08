import tkinter as tk
import sys
from src.config import *

def inicializar_elementos():
    return {
        "bits_x": 100,
        "bits_y": ALTURA_CHAO - 60,
        "bits_largura": 40,
        "bits_altura": 60,
        "vel_y": 0,
        "no_ar": False,
        "agachado": False,
        "obs_x": LARGURA_TELA + 50,
        "obs_y": ALTURA_CHAO - 40,
        "obs_largura": 30,
        "obs_altura": 40,
        "vel_obs": 6,
        "altura_original": 60,
        "y_original": ALTURA_CHAO - 60
    }

def executar_jogo():
    janela = tk.Tk()
    janela.title("Pixel Runner: O Último Sinal")
    janela.geometry(f"{LARGURA_TELA}x{ALTURA_TELA}")
    janela.resizable(False, False)

    canvas = tk.Canvas(janela, width=LARGURA_TELA, height=ALTURA_TELA, bg=COR_FUNDO, highlightthickness=0)
    canvas.pack()

    canvas.create_rectangle(0, ALTURA_CHAO, LARGURA_TELA, ALTURA_TELA, fill=COR_CHAO, outline="")

    est = inicializar_elementos()

    id_bits = canvas.create_rectangle(est["bits_x"], est["bits_y"], est["bits_x"] + est["bits_largura"], est["bits_y"] + est["bits_altura"], fill=COR_BITS, outline="")
    id_obs = canvas.create_rectangle(est["obs_x"], est["obs_y"], est["obs_x"] + est["obs_largura"], est["obs_y"] + est["obs_altura"], fill=COR_OBSTACULO, outline="")

    def pressionar(event):
        if event.keysym in ["space", "Up"] and not est["no_ar"] and not est["agachado"]:
            est["vel_y"] = FORCA_PULO
            est["no_ar"] = True
        elif event.keysym == "Down" and not est["no_ar"] and not est["agachado"]:
            est["agachado"] = True
            est["bits_altura"] = est["altura_original"] // 2
            est["bits_y"] = ALTURA_CHAO - est["bits_altura"]
            canvas.coords(id_bits, est["bits_x"], est["bits_y"], est["bits_x"] + est["bits_largura"], est["bits_y"] + est["bits_altura"])

    def soltar(event):
        if event.keysym == "Down" and est["agachado"]:
            est["agachado"] = False
            est["bits_altura"] = est["altura_original"]
            est["bits_y"] = est["y_original"]
            canvas.coords(id_bits, est["bits_x"], est["bits_y"], est["bits_x"] + est["bits_largura"], est["bits_y"] + est["bits_altura"])

    janela.bind("<KeyPress>", pressionar)
    janela.bind("<KeyRelease>", soltar)

    def loop():
        if est["no_ar"]:
            est["vel_y"] += GRAVIDADE
            est["bits_y"] += est["vel_y"]
            if est["bits_y"] >= est["y_original"]:
                est["bits_y"] = est["y_original"]
                est["vel_y"] = 0
                est["no_ar"] = False
            canvas.coords(id_bits, est["bits_x"], est["bits_y"], est["bits_x"] + est["bits_largura"], est["bits_y"] + est["bits_altura"])

        est["obs_x"] -= est["vel_obs"]
        if est["obs_x"] < -est["obs_largura"]:
            est["obs_x"] = LARGURA_TELA + 100
        canvas.coords(id_obs, est["obs_x"], est["obs_y"], est["obs_x"] + est["obs_largura"], est["obs_y"] + est["obs_altura"])

        b_coords = canvas.coords(id_bits)
        o_coords = canvas.coords(id_obs)

        if (b_coords[0] < o_coords[2] and b_coords[2] > o_coords[0] and
            b_coords[1] < o_coords[3] and b_coords[3] > o_coords[1]):
            print("Colisão detectada! BITS colidiu.")
            est["obs_x"] = LARGURA_TELA + 100

        janela.after(int(1000 / FPS), loop)

    loop()
    janela.mainloop()
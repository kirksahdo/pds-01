# import soundfile as sf
# import librosa
# import tkinter as tk
# from tkinter import Scale

# def ajustar_volume_voz(volume):
#     global volume_voz
#     volume_voz = float(volume) / 100
#     atualizar_mistura()

# def ajustar_volume_musica(volume):
#     global volume_musica
#     volume_musica = float(volume) / 100
#     atualizar_mistura()

# def atualizar_mistura():
#     global volume_voz, volume_musica, taxa_amostragem
#     voz_ajustada = voz * volume_voz
#     musica_ajustada = musica * volume_musica
#     min_length = min(len(voz_ajustada), len(musica_ajustada))
#     voz_ajustada = voz_ajustada[:min_length]
#     musica_ajustada = musica_ajustada[:min_length]
#     mistura = (voz_ajustada) + (musica_ajustada)
#     max_length = 120 * taxa_amostragem
#     mistura = mistura[:max_length]
#     sf.write("saida.wav", mistura, taxa_amostragem)

# # Carregar os arquivos de áudio
# voz, taxa_amostragem_voz = librosa.load("assets/q_sound_random_text.wav", sr=None)
# musica, taxa_amostragem_musica = librosa.load("assets/q_sound_titas.wav", sr=None)

# if taxa_amostragem_voz != taxa_amostragem_musica:
#     # Se as taxas de amostragem forem diferentes, resample a voz para a taxa de amostragem da música
#     voz = librosa.resample(voz, taxa_amostragem_voz, taxa_amostragem_musica)

# taxa_amostragem = taxa_amostragem_musica

# if taxa_amostragem_voz != taxa_amostragem_musica:
#     raise ValueError("As taxas de amostragem dos arquivos de áudio não são iguais")

# volume_voz = 1.0
# volume_musica = 0.3

# root = tk.Tk()
# root.title("Ajustar Volume")

# lbl_voz = tk.Label(root, text="Volume da Voz")
# lbl_voz.grid(row=0, column=0)
# scale_voz = Scale(root, from_=0, to=100, orient="horizontal", command=ajustar_volume_voz)
# scale_voz.set(volume_voz * 100)
# scale_voz.grid(row=0, column=1)

# lbl_musica = tk.Label(root, text="Volume da Música")
# lbl_musica.grid(row=1, column=0)
# scale_musica = Scale(root, from_=0, to=100, orient="horizontal", command=ajustar_volume_musica)
# scale_musica.set(volume_musica * 100)
# scale_musica.grid(row=1, column=1)

# root.mainloop()

import tkinter as tk

print("Versão do Tkinter:", tk.TkVersion)
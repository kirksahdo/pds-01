import numpy as np
import matplotlib.pyplot as plt

def plot_dft():
    # Solicitando ao usuário que insira os valores das amostras
    samples = []
    for i in range(8):
        sample = float(input(f'Insira o valor da amostra {i+1}: '))
        samples.append(sample)

    # Calculando a DFT das amostras
    samples = np.array(samples)
    DFT = np.fft.fft(samples)

    # Convertendo os índices da DFT em frequências em Hertz
    fs = 44100  # frequência de amostragem
    freqs = np.fft.fftfreq(len(DFT), 1/fs)

    # Plotando o gráfico da magnitude da DFT versus a frequência em Hertz
    plt.figure(figsize=(10, 6))
    plt.plot(freqs[:len(freqs)//2], np.abs(DFT)[:len(DFT)//2])  # Plotando apenas a metade positiva do espectro
    plt.title('Resposta em amplitude')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# Chamando a função
plot_dft()
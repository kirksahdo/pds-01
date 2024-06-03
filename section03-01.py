import numpy as np
import matplotlib.pyplot as plt

# Definindo a função de impulso h[n]
alpha1 = 0.15
beta = 0.707
h = np.array([alpha1, beta, alpha1])

# Calculando a DFT de h[n]
H = np.fft.fft(h, 512)
H = np.abs(H)  # Obtendo a magnitude
H = H / np.max(H)  # Normalizando

# Plotando o gráfico da resposta em amplitude
plt.figure(figsize=(10, 6))
plt.plot(H, label='|H(e^jΩ)|')
plt.title('Resposta em amplitude para h[n]')
plt.xlabel('Ω')
plt.ylabel('|H(e^jΩ)|')
plt.legend()
plt.grid(True)
plt.show()

# Determinando o tipo de filtro
if H[0] < H[-1]:
    print('O sistema atua como um filtro passa-alta.')
else:
    print('O sistema atua como um filtro passa-baixa.')
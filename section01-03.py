import numpy as np
import matplotlib.pyplot as plt

def plot_linearidade():
    
    # Sinal x[n]
    x = np.array([0, 0.707, 1, 0.707, 0, -0.707, -1, -0.707])
    # Constante
    a = 2
    # Computando a DTFT de x[n]
    X = np.fft.fft(x)
    # Computando a DTFT de a * x[n]
    aX = np.fft.fft(a * x)

    # Plotando os resultados
    plt.figure(figsize=(12, 6))

    # Magnitude da DTFT de x[n]
    plt.subplot(2, 2, 1)
    plt.stem(np.abs(X))
    plt.title('Magnitude de X(e^jω)')
    plt.xlabel('Índice de frequência')
    plt.ylabel('Magnitude')

    # Fase da DTFT de x[n]
    plt.subplot(2, 2, 2)
    plt.stem(np.angle(X))
    plt.title('Fase de X(e^jω)')
    plt.xlabel('Índice de frequência')
    plt.ylabel('Fase (radianos)')

    # Magnitude da DTFT de a*x[n]
    plt.subplot(2, 2, 3)
    plt.stem(np.abs(aX))
    plt.title('Magnitude de a * X(e^jω)')
    plt.xlabel('Índice de frequência')
    plt.ylabel('Magnitude')

    # Fase da DTFT de a*x[n]
    plt.subplot(2, 2, 4)
    plt.stem(np.angle(aX))
    plt.title('Fase de a * X(e^jω)')
    plt.xlabel('Índice de frequência')
    plt.ylabel('Fase (radianos)')

    plt.tight_layout()
    plt.show()
    

def plot_convolucao():
    # Sinais x[n] e h[n]
    x = np.array([0, 0.707, 1, 0.707, 0, -0.707, -1, -0.707])
    h = np.array([1, 2, 1])
    # Convolução de x[n] e h[n]
    y = np.convolve(x, h)
    # Computando as DTFTs
    X = np.fft.fft(x, n=len(x) + len(h) - 1)
    H = np.fft.fft(h, n=len(x) + len(h) - 1)
    Y = np.fft.fft(y)

    # Plotando os resultados
    plt.figure(figsize=(12, 6))

    # Magnitude da DTFT de X(e^jω)
    plt.subplot(3, 2, 1)
    plt.stem(np.abs(X))
    plt.title('Magnitude de X(e^jω) --> X[n]')
    plt.xlabel('Índice de frequência')
    plt.ylabel('Magnitude')

    # Fase da DTFT de X(e^jω)
    plt.subplot(3, 2, 2)
    plt.stem(np.angle(X))
    plt.title('Fase de X(e^jω) --> X[n]')
    plt.xlabel('Índice de frequência')
    plt.ylabel('Fase (radianos)')

    # Magnitude da DTFT de H(e^jω)
    plt.subplot(3, 2, 3)
    plt.stem(np.abs(H))
    plt.title('Magnitude de H(e^jω) --> Y[n]')
    plt.xlabel('Índice de frequência')
    plt.ylabel('Magnitude')

    # Fase da DTFT de H(e^jω)
    plt.subplot(3, 2, 4)
    plt.stem(np.angle(H))
    plt.title('Fase de H(e^jω) --> Y[n]')
    plt.xlabel('Índice de frequência')
    plt.ylabel('Fase (radianos)')

    # Magnitude da DTFT de Y(e^jω)
    plt.subplot(3, 2, 5)
    plt.stem(np.abs(Y))
    plt.title('Magnitude de Y(e^jω) --> X[n] * Y[n]')
    plt.xlabel('Índice de frequência')
    plt.ylabel('Magnitude')

    # Fase da DTFT de Y(e^jω)
    plt.subplot(3, 2, 6)
    plt.stem(np.angle(Y))
    plt.title('Fase de Y(e^jω) --> Y[n]')
    plt.xlabel('Índice de frequência')
    plt.ylabel('Fase (radianos)')

    plt.tight_layout()
    plt.show()


def main():
      c = input()
      match c:

            case "1":
                plot_linearidade()

            case "2":
                plot_convolucao()

            case _:
                raise Exception("INVÁLIDO")

if __name__ == "__main__":
    main()

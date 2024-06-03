import numpy as np
import sounddevice as sd
import msvcrt

# Frequências das notas musicaisa
NOTES_FREQS = {
    'Q': 264,  # Dó
    'W': 297,  # Ré
    'E': 330,  # Mi
    'R': 352,  # Fá
    'T': 396,  # Sol
    'Y': 440,  # Lá
    'U': 495,  # Si
    'I': 528   # dó
}

SAMPLE_RATE = 8000  # Frequência de amostragem de 8kHz
DURATION = 0.5  # Duração de cada tom em segundos
AMPLITUDE = 0.5  # Amplitude de 1Vpp (0.5Vp)

def generate_tone(frequency, duration, amplitude, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = amplitude * np.sin(2 * np.pi * frequency * t)
    return tone

def play_tone(tone, sample_rate):
    sd.play(tone, sample_rate)
    sd.wait()

def get_key():
    return msvcrt.getch().decode('utf-8').upper()

def main():
    print("Pressione as teclas para tocar as notas musicais. Pressione 'x' para sair.")
    print("Q: Dó, W: Ré, E: Mi, R: Fá, T: Sol, Y: Lá, U: Si, I: dó")
    while True:
        key = get_key()
        if key == 'X':
            break
        if key in NOTES_FREQS:
            frequency = NOTES_FREQS[key]
            tone = generate_tone(frequency, DURATION, AMPLITUDE, SAMPLE_RATE)
            play_tone(tone, SAMPLE_RATE)
        else:
            print(f"Tecla '{key}' não é uma tecla válida para uma nota musical.")

if __name__ == "__main__":
    main()

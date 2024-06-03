import soundfile as sf
import librosa

# Carregue os arquivos de áudio

voz, taxa_amostragem_voz = librosa.load("assets/q_sound_random_text.wav", sr=None)
musica, taxa_amostragem_musica = librosa.load("assets/q_sound_titas.wav", sr=None)

if taxa_amostragem_voz != taxa_amostragem_musica:
    # Se as taxas de amostragem forem diferentes, resample a voz para a taxa de amostragem da música
    voz = librosa.resample(voz, taxa_amostragem_voz, taxa_amostragem_musica)

taxa_amostragem = taxa_amostragem_musica

if taxa_amostragem_voz != taxa_amostragem_musica:
    raise ValueError("As taxas de amostragem dos arquivos de áudio não são iguais")


# Ajuste os níveis de áudio
voz = voz * 1.2  # Aumente o volume da voz
musica = musica * 0.3  # Diminua o volume da música

# Certifique-se de que ambos os arquivos têm o mesmo comprimento
min_length = min(len(voz), len(musica))
voz = voz[:min_length]
musica = musica[:min_length]

# Misture a voz com a música
mistura = voz + musica

# Certifique-se de que a duração final não exceda 120 segundos
max_length = 120 * taxa_amostragem
mistura = mistura[:max_length]

# Salve o resultado
sf.write("saida.wav", mistura, taxa_amostragem)

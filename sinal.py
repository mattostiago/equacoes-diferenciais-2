import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
fs = 1000  # Taxa de amostragem (Hz)
T = 1    # Duração (s)
t = np.linspace(0, T, int(fs * T), endpoint=False)  # Vetor de tempo

# Sinal
f = np.sin(2 * np.pi * t) + np.cos(4 * np.pi * t)

# FFT
F = np.fft.fft(f)
freqs = np.fft.fftfreq(len(f), 1 / fs)

# Reconstrução do sinal
f_reconstructed = np.fft.ifft(F).real

# Plot
plt.figure(figsize=(12, 8))

# Sinal original e reconstruído no mesmo gráfico
plt.subplot(3, 1, 1)
plt.plot(t, f, label='Sinal Original')
plt.plot(t, f_reconstructed, label='Sinal Reconstruído', linestyle='--', alpha=0.7)
plt.title('Sinal Original e Reconstruído')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Apenas o sinal original para análise separada
plt.subplot(3, 1, 2)
plt.plot(t, f, label='Sinal Original')
plt.title('Sinal Original no Domínio do Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Espectro de Frequência
plt.subplot(3, 1, 3)
plt.stem(freqs[:len(freqs)//2], np.abs(F[:len(F)//2]), basefmt=" ")
plt.title('Espectro de Frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()

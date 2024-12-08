import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
fs = 500  # Taxa de amostragem (Hz) - Deve ser no mínimo 2x a maior frequência (Nyquist)
T = 1     # Duração do sinal (s)
t = np.linspace(0, T, int(fs * T), endpoint=False)  # Vetor de tempo

# Sinal original
f_t = np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 100 * t)

# FFT
F = np.fft.fft(f_t)
freqs = np.fft.fftfreq(len(F), 1 / fs)

# Filtro passa-baixa (mantém frequências até 50 Hz)
cutoff = 50
F_filtered = F.copy()
F_filtered[np.abs(freqs) > cutoff] = 0  # Zera componentes acima do cutoff

# Reconstrução do sinal
f_reconstructed = np.fft.ifft(F_filtered).real

# Plotagem
plt.figure(figsize=(12, 8))

# Sinal original
plt.subplot(3, 1, 1)
plt.plot(t, f_t, label='Sinal Original')
plt.title('Sinal Original no Domínio do Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Espectro de frequência original
plt.subplot(3, 1, 2)
plt.stem(freqs[:len(freqs)//2], np.abs(F[:len(F)//2]), basefmt=" ", label='Espectro Original')
plt.axvline(cutoff, color='red', linestyle='--', label='Cutoff 50 Hz')
plt.title('Espectro de Frequência Original')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Sinal reconstruído
plt.subplot(3, 1, 3)
plt.plot(t, f_reconstructed, label='Sinal Reconstruído (Filtrado)', color='orange')
plt.title('Sinal Reconstruído no Domínio do Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
fs = 1000  # Taxa de amostragem (Hz)
T = 1.0    # Duração total do sinal (s)
t = np.linspace(0, T, int(fs * T), endpoint=False)  # Vetor de tempo

# Sinais no domínio do tempo
f_t = np.sin(2 * np.pi * 10 * t)  # f(t) = sin(2π × 10t)
g_t = np.cos(2 * np.pi * 5 * t)   # g(t) = cos(2π × 5t)

# Transformadas de Fourier dos sinais
F_f = np.fft.fft(f_t)  # FFT de f(t)
F_g = np.fft.fft(g_t)  # FFT de g(t)

# Convolução no domínio da frequência (multiplicação)
F_h = F_f * F_g

# Transformada inversa para obter a convolução no tempo
h_t = np.fft.ifft(F_h).real

# Plot dos resultados
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, f_t, label='$f(t) = \sin(2\pi \cdot 10t)$')
plt.xlabel('Tempo (s)')
plt.ylabel('$f(t)$')
plt.title('Sinal $f(t)$')
plt.grid()
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, g_t, label='$g(t) = \cos(2\pi \cdot 5t)$', color='orange')
plt.xlabel('Tempo (s)')
plt.ylabel('$g(t)$')
plt.title('Sinal $g(t)$')
plt.grid()
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, h_t, label='$h(t) = (f * g)(t)$', color='green')
plt.xlabel('Tempo (s)')
plt.ylabel('$h(t)$')
plt.title('Convolução $h(t)$')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

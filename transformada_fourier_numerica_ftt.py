import numpy as np
import matplotlib.pyplot as plt

# Parametros
L = 10  # Comprimento do dominio
N = 256  # Numero de pontos de discretizacao
alpha = 0.01  # Difusividade térmica
T = 1.0  # Tempo total
x = np.linspace(-L/2, L/2, N)  # Dominio espacial
dx = x[1] - x[0]
dt = 0.01  # Passo no tempo
t = np.arange(0, T, dt)  # Instantes de tempo

# Condicao inicial: Pulso gaussiano
u = np.exp(-x**2)
k = 2 * np.pi * np.fft.fftfreq(N, d=dx)  # Frequencias de Fourier

# Evolucao temporal usando FFT
u_hat = np.fft.fft(u)
for ti in t:
    u_hat *= np.exp(-alpha * (k**2) * dt)  # Solucao no dominio da frequencia
    u = np.fft.ifft(u_hat).real  # Transformada inversa para o dominio do espaco

# Plot da solucao final
plt.figure(figsize=(8, 6))
plt.plot(x, np.exp(-x**2), label="Condicao inicial", linestyle="--")
plt.plot(x, u, label=f"Solucao em t = {T}")
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('Solucao Numerica da Equacao do Calor (FFT)')
plt.legend()
plt.grid()
plt.show()
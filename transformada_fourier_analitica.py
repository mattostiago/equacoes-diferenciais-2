import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
L = 10  # Comprimento do domínio
N = 256  # Número de pontos de discretização
alpha = 0.01  # Difusividade térmica
T = 1.0  # Tempo total
x = np.linspace(-L/2, L/2, N)  # Domínio espacial
dx = x[1] - x[0]
t = np.linspace(0, T, 100)  # Instantes de tempo

# Condição inicial: Pulso gaussiano
u0 = np.exp(-x**2)
k = 2 * np.pi * np.fft.fftfreq(N, d=dx)  # Frequências de Fourier

# Solução analítica usando Transformada de Fourier
u_hat0 = np.fft.fft(u0)  # Transformada de Fourier inicial
u_analytical = []

for ti in t:
    u_hat = u_hat0 * np.exp(-alpha * (k**2) * ti)  # Solução no domínio da frequência
    u_t = np.fft.ifft(u_hat).real  # Transformada inversa para o domínio do espaço
    u_analytical.append(u_t)

# Plot da solução analítica
plt.figure(figsize=(8, 6))
for i in range(0, len(t), 20):  # Exibir apenas algumas curvas para clareza
    plt.plot(x, u_analytical[i], label=f't={t[i]:.2f}')
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('Solução Analítica da Equação do Calor')
plt.legend()
plt.grid()
plt.show()
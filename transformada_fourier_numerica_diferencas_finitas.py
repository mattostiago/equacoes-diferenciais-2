import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
L = 2 * np.pi  # Comprimento do domínio [-pi, pi]
nx = 100  # Número de pontos espaciais
dx = L / nx  # Passo no espaço
alpha = 1.0  # Coeficiente de difusão
dt = 0.001  # Passo no tempo
t_max = 1.0  # Tempo máximo de simulação
r = alpha * dt / dx**2  # Número de Courant

# Verificação de estabilidade
if r > 0.5:
    raise ValueError(f"Atenção: o esquema não será estável, r = {r:.2f} > 0.5")

# Discretização espacial
x = np.linspace(-np.pi, np.pi, nx)

# Condição inicial
u0 = np.where(np.abs(x) < np.pi, 2 * np.cos(x) + 2, 0.0)

# Função para resolver por diferenças finitas
def solve_heat_eq(u0, nx, nt, r):
    u = u0.copy()
    u_new = u0.copy()
    for _ in range(nt):
        for i in range(1, nx - 1):  # Evitar bordas
            u_new[i] = u[i] + r * (u[i + 1] - 2 * u[i] + u[i - 1])
        u[:] = u_new
    return u

# Solução numérica
nt = int(t_max / dt)  # Número de passos de tempo
u_final = solve_heat_eq(u0, nx, nt, r)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(x, u0, label="Condição inicial", linestyle="--")
plt.plot(x, u_final, label=f"Solução em t = {t_max}")
plt.xlabel("x")
plt.ylabel("u(x, t)")
plt.title("Solução Numérica da Equação do Calor (Diferenças Finitas)")
plt.legend()
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2, fftshift, ifftshift
from skimage import color, data, img_as_float
from skimage.io import imread

# Carregar a imagem (convertendo para tons de cinza)
image = color.rgb2gray(imread('uerj.jpg')) 

# Aplicar FFT 2D
fft_image = fft2(image)
fft_shifted = fftshift(fft_image)  # Centralizar as frequências baixas

# Visualizar espectro de frequências
magnitude_spectrum = np.log(1 + np.abs(fft_shifted))

# Criar um filtro passa-baixa
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2
radius = 50  # Raio do filtro
mask = np.zeros((rows, cols), dtype=np.float32)
y, x = np.ogrid[:rows, :cols]
mask_area = (x - ccol)**2 + (y - crow)**2 <= radius**2
mask[mask_area] = 1

# Aplicar o filtro
filtered_fft = fft_shifted * mask
filtered_fft_shifted_back = ifftshift(filtered_fft)

# Reconstruir a imagem (IFFT)
reconstructed_image = np.real(ifft2(filtered_fft_shifted_back))

# Plotar os resultados
plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.title("Imagem Original")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(232)
plt.title("Espectro de Frequência")
plt.imshow(magnitude_spectrum, cmap="gray")
plt.axis("off")

plt.subplot(233)
plt.title("Filtro Passa-Baixa")
plt.imshow(mask, cmap="gray")
plt.axis("off")

plt.subplot(234)
plt.title("Espectro Filtrado")
plt.imshow(np.log(1 + np.abs(filtered_fft)), cmap="gray")
plt.axis("off")

plt.subplot(235)
plt.title("Imagem Reconstruída")
plt.imshow(reconstructed_image, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()

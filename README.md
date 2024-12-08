# Análise de Sinais e Transformada de Fourier

Este repositório contém diversos scripts em Python para análise de sinais, filtragem, convolução e transformada de Fourier, tanto analítica quanto numérica. Abaixo está uma descrição dos arquivos e suas funcionalidades.

## Estrutura do Repositório

- [`convolucoes.py`](convolucoes.py): Implementa a convolução de dois sinais no domínio do tempo utilizando a Transformada de Fourier.
- [`filtragem_sinais.py`](filtragem_sinais.py): Aplica um filtro passa-baixa a um sinal e reconstrói o sinal filtrado.
- [`reconstrucao_imagens.py`](reconstrucao_imagens.py): Realiza a reconstrução de imagens utilizando a Transformada de Fourier 2D.
- [`sinal.py`](sinal.py): Gera um sinal composto por senos e cossenos, aplica a FFT e reconstrói o sinal original.
- [`transformada_fourier_analitica.py`](transformada_fourier_analitica.py): Resolve a equação do calor utilizando a solução analítica via Transformada de Fourier.
- [`transformada_fourier_numerica_diferencas_finitas.py`](transformada_fourier_numerica_diferencas_finitas.py): Resolve a equação do calor utilizando diferenças finitas.
- [`transformada_fourier_numerica_ftt.py`](transformada_fourier_numerica_ftt.py): Resolve a equação do calor utilizando a Transformada de Fourier numérica (FFT).

## Dependências

Para executar os scripts, você precisará das seguintes bibliotecas Python:

- `numpy`
- `matplotlib`
- `scipy`
- `scikit-image`

Você pode instalar todas as dependências utilizando o seguinte comando:

```sh
pip install numpy matplotlib scipy scikit-image
```
## Uso

### Convoluções de Sinais

O script [`convolucoes.py`] realiza a convolução de dois sinais no domínio do tempo utilizando a Transformada de Fourier. Para executá-lo, use:

```sh
python convolucoes.py
```
### Filtragem de Sinais

O script [`filtragem_sinais.py`] aplica um filtro passa-baixa a um sinal e reconstrói o sinal filtrado. Para executá-lo, use:

```sh
python filtragem_sinais.py
```

### Reconstrução de Imagens

O script [`reconstrucao_imagens.py`] realiza a reconstrução de imagens utilizando a Transformada de Fourier 2D. Para executá-lo, use:

```sh
python reconstrucao_imagens.py
```
### Análise de Sinais

O script [`sinal.py gera um sinal`] composto por senos e cossenos, aplica a FFT e reconstrói o sinal original. Para executá-lo, use:

```sh
python sinal.py
```

### Transformada de Fourier Analítica

O script [`transformada_fourier_analitica.py`] resolve a equação do calor utilizando a solução analítica via Transformada de Fourier. Para executá-lo, use:

```sh
python transformada_fourier_analitica.py
```

### Transformada de Fourier Numérica (Diferenças Finitas)

O script [`transformada_fourier_numerica_diferencas_finitas.py`] resolve a equação do calor utilizando diferenças finitas. Para executá-lo, use:

```sh
python transformada_fourier_numerica_diferencas_finitas.py
```

### Transformada de Fourier Numérica (FFT)

O script transformada_fourier_numerica_fft.py resolve a equação do calor utilizando a Transformada de Fourier numérica (FFT). Para executá-lo, use:


```sh
python transformada_fourier_numerica_fft.py
```

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato
Para mais informações, entre em contato com o mantenedor do projeto.
import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# caracteristicas do filtro
order = 3
fs = 12000.0       # amostragem em HZ
r = 1000
c = 100*10**(-9)
cutoff = (1/(2*np.pi*r*c))  # frequencia de corte em Hz

#Pegando os filtros dos coeficientes para poder checar a resposta da frequencia 
b, a = butter_lowpass(cutoff, fs, order)

# Trace a resposta de frequência.
w, h = freqz(b, a, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()


# Demonstre o uso do filtro.
# Primeiro faça com que alguns dados sejam filtrados.
T = 5.0         # segundos
n = int(T * fs) # numero total de amostra
t = np.linspace(0, T, n, endpoint=False)
# "Noisy" data. Queremos recuperar o sinal de 1,2 Hz disso.
data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)

# Filtrar os dados e plotar ambos o original e o sinal filtrado
y = butter_lowpass_filter(data, cutoff, fs, order)

plt.subplot(2, 1, 2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()
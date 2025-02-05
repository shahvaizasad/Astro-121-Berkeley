import numpy as np
import ugradio
import matplotlib.pyplot as plt

freq = 1e6

#these two lines for data that is less likely to alias
sdr = ugradio.sdr.SDR(sample_rate=freq)
data = sdr.capture_data()


# For 5.4 Leakage Power Section of Lab
N= 300000
f = np.linspace(-freq/2, freq/2, num =N, endpoint = False)

fourier_voltage = ugradio.dft.dft(data[0],f=f,vsamp=freq)
fourier_power = fourier_voltage[1]*np.conj(fourier_voltage[1])


plt.plot(fourier_voltage[0], fourier_power)
#plt.yscale('log')
plt.show()

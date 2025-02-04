import numpy as np
import ugradio
import matplotlib.pyplot as plt

freq = 1e6

#these two lines for data that is less likely to alias
sdr = ugradio.sdr.SDR(sample_rate=freq)
data = sdr.capture_data()

#these lines will increase aliasing
#coeffs = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047])
#sdr_filtered = ugradio.sdr.SDR(sample_rate=freq,fir_coeffs=coeffs)
#data_filtered = sdr_filtered.capture_data()

# For 5.4 Leakage Power Section of Lab
N= 30000
f = np.linspace(0, freq/2, num =N, endpoint = False)

fourier_voltage = ugradio.dft.dft(data[0],f=f,vsamp=freq)
fourier_power = fourier_voltage[1]*np.conj(fourier_voltage[1])


plt.plot(fourier_voltage[0], fourier_power)
plt.yscale('log')
plt.show()

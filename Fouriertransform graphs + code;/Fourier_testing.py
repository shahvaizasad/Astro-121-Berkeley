import numpy as np
import ugradio
import matplotlib.pyplot as plt

freq = 1e6

#these two lines for data that is less likely to alias
sdr = ugradio.sdr.SDR(sample_rate=freq)
data = sdr.capture_data()

#these lines will increase aliasing
coeffs = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047])
#sdr_filtered = ugradio.sdr.SDR(sample_rate=freq,fir_coeffs=coeffs)
#data_filtered = sdr_filtered.capture_data()

#setting up the x_axis in terms of frequency rather than indexing
n = 2048
timestep = 1 /freq
x_axis  = np.fft.fftshift(np.fft.fftfreq(n, d=timestep))

#y-axis is fourier transformed voltage data, second line has filtered_data
#fourier = np.fft.fftshift(np.fft.fft(data))
#fourier = np.fft.fftshift(np.fft.fft(data_filtered))

#y-axis is fourier transformed power data, second line has filtered data

#fourier_voltage = np.fft.fft(data)
#fourier_power = fourier_voltage*np.conj(fourier_voltage)
#fourier = np.fft.fftshift(fourier_power)

#autocorrelation function (acf) for voltage series is same as power series
fourier_voltage = np.fft.fft(data)
fourier = np.correlate(fourier_voltage[0], fourier_voltage[0], mode='full')
fourier = fourier[fourier.size//2:]
fourier = np.fft.fftshift(fourier)

plt.plot(x_axis,fourier)
#fourier = np.fft.fftshift(np.fft.fft(data_filtered))

#for real or imaginary component
#fourier = fourier.real
#fourier = fourier.imag

#plt.plot(x_axis, fourier[0])
plt.show()

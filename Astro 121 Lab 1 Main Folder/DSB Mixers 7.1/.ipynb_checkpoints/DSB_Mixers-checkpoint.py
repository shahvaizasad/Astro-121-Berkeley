import numpy as np
import ugradio
import matplotlib.pyplot as plt

sample_freq = 2.5e6

radio_freq = 630000 
local_oscil = 600000
delta_freq = +3e4


#these lines will increase aliasing
coeffs = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047])
sdr_filtered = ugradio.sdr.SDR(sample_rate=sample_freq,fir_coeffs=coeffs)
data_filtered = sdr_filtered.capture_data(nsamples=20480)

#setting up the x_axis in terms of frequency rather than indexing
n = 20480
timestep = 1 /sample_freq
x_axis  = np.fft.fftshift(np.fft.fftfreq(n, d=timestep))

#y-axis is fourier transformed voltage data, second line has filtered_data
#fourier = np.fft.fftshift(np.fft.fft(data))
#fourier = np.fft.fftshift(np.fft.fft(data_filtered))

#y-axis is fourier transformed power data, second line has filtered data
fourier_voltage = np.fft.fft(data_filtered)
#fourier_power = fourier_voltage*np.conj(fourier_voltage)
fourier_power = np.abs(fourier_voltage)**2
fourier = np.fft.fftshift(fourier_power)

#for removing summation spikes
#a = np.array([-(radio_freq + local_oscil), (radio_freq + local_oscil)])
#x_axis[:,a] = 0 

fourier = np.log(fourier)

np.savez(f"sample_freq:{sample_freq}_RF:{radio_freq}_LO:{local_oscil}",data_filtered)

plt.plot(x_axis, fourier[0])
plt.show()

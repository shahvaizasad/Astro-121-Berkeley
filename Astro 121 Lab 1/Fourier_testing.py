import numpy as np
import ugradio
import matplotlib.pyplot as plt

freq = 1e6
sdr = ugradio.sdr.SDR(sample_rate=freq)
data = sdr.capture_data()

fourier = np.fft.fft(data)

plt.plot(fourier[0])
plt.show()

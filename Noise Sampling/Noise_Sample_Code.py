import numpy as np
import ugradio
import matplotlib.pyplot as plt

sample_freq = 1e6

sdr = ugradio.sdr.SDR(sample_rate=sample_freq)
data = sdr.capture_data()

np.savez(f"{sample_freq}_Noise",data)

plt.plot(data[0])
plt.show()

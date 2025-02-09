import numpy as np
import ugradio
import matplotlib.pyplot as plt

#sample_freq = 2.3e6
sample_freqs = np.arange(3e6, 3.3e6, 0.10e6)
sdr = ugradio.sdr.SDR(sample_rate=sample_freqs[0])
for sample_freq in sample_freqs:
    filter  = 1
    sdr.set_sample_rate(sample_freq)
    data = sdr.capture_data(nblocks=2)[1]
    np.savez(f"{sample_freq}_Noise,filter?_ {filter}",data)

#plt.plot(data[0])
#plt.show()

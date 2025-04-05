import numpy as np
import ugradio
import matplotlib.pyplot as plt

coeffs = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047])

sample_freq = 3e6
freq = 1.6e5
#sdr = ugradio.sdr.SDR(sample_rate=sample_freq)
#data = sdr.capture_data()

sdr_filtered = ugradio.sdr.SDR(sample_rate=sample_freq,fir_coeffs=coeffs)
data_filtered = sdr_filtered.capture_data()

#np.savez(f"{sample_freq}_{freq}_puredata",data)
np.savez(f"{sample_freq}_{freq}_filtereddata",data_filtered)
plt.plot(data_filtered[0])
plt.show()

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define Gaussian function with normalization
def gaussian(x, a, b, c):
    """
    Gaussian function:
    a = amplitude (height of the curve)
    b = mean (center of the curve)
    c = standard deviation (spread of the curve)
    """
    return a / (c * np.sqrt(2 * np.pi)) * np.exp(-(x - b)**2 / (2 * c**2))

stuff = "Astro 121 Lab 1/Filtered Noise"  

for file_name in os.listdir(stuff):
    
    if not file_name.endswith('.txt'):
        continue
    
    # Load the data from the file
    data = np.loadtxt(os.path.join(stuff, file_name))
    
    freq_str = file_name.split('_')[0]  # Extract frequency part before '_'
    freq = float(freq_str) * 1e6  # Convert MHz to Hz
    
    # Create histogram and calculate bin centers
    hist, bin_edges = np.histogram(data, bins=80, density=True)  
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2  

    p0 = [max(hist), np.median(data), (max(data) - min(data)) / 6]  # [amplitude, mean, std dev]
    
    # Fit Gaussian to histogram data
    try:
        popt, pcov = curve_fit(gaussian, bin_centers, hist, p0=p0)
    except RuntimeError as e:
        print(f"Could not fit Gaussian for {file_name}: {e}")
        continue
    
    x_fit = np.linspace(bin_edges[0], bin_edges[-1], 1000)
    
    # Plot histogram and Gaussian fit
    plt.figure(figsize=(8, 6))
    plt.rc('font', family='serif', size=14)
    
    plt.hist(data, bins=bin_edges, density=True, alpha=0.6, color='r', edgecolor='black')
    plt.plot(x_fit, gaussian(x_fit, *popt), 'k--', lw=2,
             label=f'Fit: $\\mu$={popt[1]:.2f}, $\\sigma$={popt[2]:.2f}')
    
    plt.xlabel('Voltage [Au]')
    plt.ylabel('Density')
    plt.legend(loc = 1, fontsize =12)
    plt.grid(linestyle=':')
    plt.title(f'Noise sampled at {freq_str} MHz')
    
    # plt.show()
    plt.savefig(os.path.join(stuff, f'{freq_str}_MHz_noise.png'))  # Save plot as PNG file

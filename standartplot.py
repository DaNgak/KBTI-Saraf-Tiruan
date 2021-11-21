import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 20, 100) # membuat list angka berjarak sama dalam range yang ditentukan
plt.plot(x, np.sin(x)) # Plot sinusoida dari tiap nilai
plt.show() # tampilkan plot
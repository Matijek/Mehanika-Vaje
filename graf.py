import matplotlib.pyplot as plt
import numpy as np

# Data
force = np.array([0.50, 0.99, 1.46, 1.96, 1.46, 0.99, 0.50])
force_error = np.array([0.00098, 0.00098, 0.00098, 0.00098, 0.00098, 0.00098, 0.00098])
x = np.array([6.8, 13.5, 19.8, 26.6, 19.8, 13.4, 6.6])
x_error = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

# Linear fit through the origin
slope, _ = np.polyfit(x, force, 1)

# Plotting the data
plt.errorbar(x, force, xerr=x_error, yerr=force_error, fmt='o', label='Podatki z napakami')

# Plotting the linear fit
fit_line = np.poly1d([slope, 0])  # y = mx, where m is the slope
x_fit = np.linspace(0, max(x), 100)
plt.plot(x_fit, fit_line(x_fit), label=f'F = {slope:.3f}x \nNapaka = {slope_error:.3f}', color='red')

# Adding labels and title
plt.xlabel('x [cm]')
plt.ylabel('F [N]')
plt.title('Sila v odvisnosti od raztezka')

# Adding legend
plt.legend()

# Show the plot
plt.show()

# Display the slope
print(f"Slope: {slope:.3f}")
print(f"Slope Error: {slope_error:.3f}")
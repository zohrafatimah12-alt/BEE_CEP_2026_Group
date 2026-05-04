import numpy as np
import matplotlib.pyplot as plt

# ----------- USER INPUT -----------
R = float(input("Enter Resistance (Ohm): "))
L = float(input("Enter Inductance (H): "))
C = float(input("Enter Capacitance (F): "))
V = float(input("Enter Voltage (V): "))

# Frequency range for graph
f = np.linspace(1, 500, 500)  # 1 Hz to 500 Hz

# ----------- CALCULATIONS -----------

XL = 2 * np.pi * f * L
XC = 1 / (2 * np.pi * f * C)

Z = np.sqrt(R**2 + (XL - XC)**2)
I = V / Z
pf = R / Z

# ----------- SINGLE VALUE OUTPUT (at 50 Hz) -----------

f0 = 50

XL0 = 2 * np.pi * f0 * L
XC0 = 1 / (2 * np.pi * f0 * C)
Z0 = np.sqrt(R**2 + (XL0 - XC0)**2)
I0 = V / Z0
pf0 = R / Z0
P0 = V * I0 * pf0

print("\n--- Results at 50 Hz ---")
print(f"XL = {XL0:.2f} Ohm")
print(f"XC = {XC0:.2f} Ohm")
print(f"Z = {Z0:.2f} Ohm")
print(f"Current = {I0:.2f} A")
print(f"Power Factor = {pf0:.3f}")
print(f"Power = {P0:.2f} W")

# ----------- GRAPHS -----------

# 1. Frequency vs Impedance
plt.figure()
plt.plot(f, Z)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Impedance (Ohm)")
plt.title("Frequency vs Impedance")
plt.grid()

# 2. Frequency vs Current
plt.figure()
plt.plot(f, I)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Current (A)")
plt.title("Frequency vs Current")
plt.grid()

# 3. Frequency vs Power Factor
plt.figure()
plt.plot(f, pf)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power Factor")
plt.title("Frequency vs Power Factor")
plt.grid()

plt.show()
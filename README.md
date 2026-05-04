# BEE_CEP_2026_Group
# ⚡ Single-Phase RLC Series Circuit Impedance and Power Calculator

## 👥 Group Members
- Zohra Fatimah – 25881A05BY  
- Rathlavath Akisha – 25881A05Y5  
- R. Shyamala – 25881A05BN  

---

## 📌 Problem Description
This project develops a computational tool to analyze a single-phase RLC series circuit.  
It calculates key electrical parameters such as impedance, current, power factor, and power using given inputs like resistance, inductance, capacitance, voltage, and frequency.

The tool helps in understanding AC circuit behavior and resonance condition, where impedance is minimum and current is maximum.

---

## 📐 Mathematical Formulation

- Inductive Reactance:  
  \( X_L = 2\pi f L \)

- Capacitive Reactance:  
  \( X_C = \frac{1}{2\pi f C} \)

- Impedance:  
  \( Z = \sqrt{R^2 + (X_L - X_C)^2} \)

- Current:  
  \( I = \frac{V}{Z} \)

- Power Factor:  
  \( \cos\phi = \frac{R}{Z} \)

- Power:  
  \( P = VI\cos\phi \)

---

## 🔢 Input Format

The program takes the following inputs from the user:

- Resistance (R) in Ohms  
- Inductance (L) in Henry  
- Capacitance (C) in Farads  
- Voltage (V) in Volts  

---

## 📤 Output Format

The program displays:

- Inductive Reactance (XL)  
- Capacitive Reactance (XC)  
- Impedance (Z)  
- Current (I)  
- Power Factor  
- Power (P)  

It also generates graphs:
- Frequency vs Impedance  
- Frequency vs Current  
- Frequency vs Power Factor  

---

## ▶️ How to Run the Program

### 1. Install Python
Make sure Python is installed on your system.

### 2. Install Required Libraries

```bash
pip install numpy matplotlib
R = 10 Ohm
L = 0.1 H
C = 100 µF
V = 230 V
XL = 31.4 Ohm
XC = 31.8 Ohm
Z = 10.03 Ohm
Current = 22.93 A
Power Factor = 0.997
Power = 5260 W

## 📝 Requirements

This project requires the following Python libraries:
numpy
matplotlib
Install all dependencies using:

```bash
pip install -r requirements.txt

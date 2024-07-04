# Bicycle model Benchmark

This repository contains Python code to analyze the eigenvalues of a vehicle dynamics system. The system parameters and equations are based on the mass, moments of inertia, and geometric properties of various components of the vehicle.

## Overview

The code computes and analyzes the eigenvalues of the vehicle dynamics system to understand its stability and response characteristics under different forward velocities (v).

## Parameters

The system parameters used in the analysis include:
- **Geometry and Dimensions:**
  - Wheelbase (w)
  - Trail (c)
  - Steer axis tilt (lamb)
- **Mass and Inertia Properties:**
  - Rear wheel: mass (m_R), moments of inertia (I_Rxx, I_Ryy, I_Rzz)
  - Rear frame: mass (m_B), moments of inertia (I_Bxx, I_Byy, I_Bzz, I_Bxz)
  - Front frame: mass (m_H), moments of inertia (I_Hxx, I_Hyy, I_Hzz, I_Hxz)
  - Front wheel: mass (m_F), moments of inertia (I_Fxx, I_Fyy, I_Fzz)
- **Other Constants:**
  - Gravity (g)

## Files

- **Bicycle_Benchmark.ipynb:** Python script that computes eigenvalues for the vehicle dynamics system based on the provided parameters.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Usage

To run the code:
```bash
python Bicycle_Benchmark.ipynb
```


## Output
The script computes the eigenvalues for the system and prints them for various forward velocities (v). It also plots the real and imaginary parts of the eigenvalues as functions of velocity.

## Results
The computed eigenvalues provide insights into the stability and dynamic behavior of the vehicle under different operating conditions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

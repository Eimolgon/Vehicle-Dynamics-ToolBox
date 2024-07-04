import numpy as np
from Parameters_Motorcycle import *

def Matrix():
    E = np.zeros((10,10))
    E[0,0] = m
    E[0,1] = m*b
    E[0,2] = m*h
    E[0,3] = m_f * e_f
    E[0,4] = -m_b*z_b

    E[1,1] = m*b**2 + I_zz
    E[1,2] = m*b*h - I_xz
    E[1,3] = m_f*e_f*b_f + I_fzz * np.cos(eps)
    E[1,4] = -m_b*z_b*b_b -I_bxx * np.sin(eps)

    E[2,2] = m*h**2 + I_xx
    E[2,3] = m_f*e_f*h_f + I_fzz * np.sin(eps)
    E[2,4] = -m_b*h_b*z_b + I_bxx * np.cos(eps)

    E[3,3] = m_f*e_f**2 + I_fzz
    E[3,4] = -m_b*e_b*z_b

    E[4,4] = m_b*z_b**2 + I_bzz

    E[5,5] = k_alpha_r

    E[6,6] = k_alpha_f

    E[7,7] = 1
    E[8,8] = 1
    E[9,9] = 1

    for i in range(1, 10):
        for j in range(i):
            E[i, j] = E[j, i]

    return E
import numpy as np
from Parameters_Motorcycle import *

def Matrix(V_x):
    omega_f = V_x/R_f               # Front wheel angular velocity
    omega_r = V_x/R_r               # Rear wheel angular velocity

    F_ad = 0.5 * rho_air * V_x**2 * (CdA + Cd*Surface)
    F_al = 0.5 * rho_air * Cl * Surface * V_x**2
    X_r = F_ad

    N_r = N_r_0 + (h_A/w) * F_ad - (1 - (l_A/w)) * F_al
    N_f = N_f_0 - (h_A/w) * F_ad - (l_A/w) * F_al


    A = np.zeros((10,10))
    A[0,1] = -m * V_x
    A[0,5] = k_alpha_r * N_r
    A[0,6] = k_alpha_f * N_f
    A[0,7] = k_gamma_f * N_f + k_gamma_r * N_r
    A[0,8] = X_f * np.cos(eps) + N_f * k_gamma_f * np.sin(eps)
    A[0,9] = -X_f * np.sin(eps) + N_f * k_gamma_f * np.cos(eps)

    A[1,1] = -m * b * V_x
    A[1,2] = I_omega_r * omega_r + I_omega_f * omega_f
    A[1,3] = I_omega_f * omega_f * np.sin(eps)
    A[1,4] = I_omega_f * omega_f * np.cos(eps)
    A[1,5] = k_a_r * N_r
    A[1,6] = k_alpha_f * w * N_f + k_a_f * N_f
    A[1,7] = k_t_r * N_r + (k_t_f + w * k_gamma_f) * N_f + h * m * a_x + h_A * F_ad + \
            I_omega_r * omega_r_dot + I_omega_f * omega_f_dot - X_f * rho_f - X_r * rho_r + l_A * F_al
    A[1,8] = k_t_f * N_f * np.sin(eps) + (w * np.cos(eps) - rho_f * np.sin(eps) + a_n) * X_f + \
            m_f * e_f * a_x + I_omega_f * omega_f_dot * np.sin(eps) + N_f * k_gamma_f * w * np.sin(eps)
    A[1,9] = (l_b - rho_f * np.cos(eps) - w * np.sin(eps)) * X_f + I_omega_f * omega_f_dot * np.cos(eps) - \
            m_b * z_b * a_x + k_t_f * N_f * np.cos(eps) + N_f * k_gamma_f * w * np.cos(eps)

    A[2,1] = -m * h * V_x - I_omega_r * omega_r - I_omega_f * omega_f
    A[2,3] = -I_omega_f * omega_f * np.cos(eps)
    A[2,4] = I_omega_f * omega_f * np.sin(eps)
    A[2,7] = m * g * h - rho_f * N_f - rho_r * N_r
    A[2,8] = (a_n - rho_f * np.sin(eps)) * N_f + m_f * e_f * g - I_omega_f * omega_f_dot * np.cos(eps)
    A[2,9] = (l_b - rho_f * np.cos(eps)) * N_f - m_b * z_b * g + I_omega_f * omega_f_dot * np.sin(eps)

    A[3,1] = -m_f * e_f * V_x - I_omega_f * omega_f * np.sin(eps)
    A[3,2] = I_omega_f * omega_f * np.cos(eps)
    A[3,3] = -c_delta
    A[3,4] = I_omega_f * omega_f
    A[3,6] = (k_a_f  * np.cos(eps) - a_n * k_alpha_f) * N_f
    A[3,7] = (a_n * (1 - k_gamma_f) - rho_f * np.sin(eps)) * N_f - rho_f * X_f * np.cos(eps) + \
            m_f * e_f * g + N_f * k_t_f * np.cos(eps)
    A[3,8] = k_gamma_f * a_n * N_f * np.sin(eps)  + A[3,7] * np.sin(eps) - N_f * a_n * k_gamma_f * np.sin(eps)
    A[3,9] = (k_t_f * np.cos(eps)**2 - rho_f * np.sin(eps) * np.cos(eps) + l_b * np.sin(eps)) * N_f - \
            m_b * z_b * (g * np.sin(eps) + a_x * np.cos(eps)) + \
                    (a_n * np.sin(eps) - rho_f * np.cos(eps)**2 + l_b * np.cos(eps)) * X_f + \
                            I_omega_f * omega_f_dot  - N_f * a_n * k_gamma_f * np.cos(eps)

    A[4,1] = m_b * z_b * V_x - I_omega_f * omega_f *np.cos(eps)
    A[4,2] = -I_omega_f * omega_f
    A[4,3] = -I_omega_f * omega_f * np.sin(eps)
    A[4,4] = -I_omega_f * omega_f * np.cos(eps)
    A[4,6] = -(k_a_f * np.sin(eps) + l_b * k_alpha_f) * N_f
    A[4,7] = ((1 - k_gamma_f) * l_b - k_t_f * np.sin(eps) - rho_f * np.cos(eps)) * N_f + \
            rho_f * X_f * np.sin(eps) - m_b * z_b * g
    A[4,8] =  - m_b * z_b * a_x * np.cos(eps) + A[4,7] * np.sin(eps)
    A[4,9] =  m_b * z_b * a_x * np.sin(eps) + A[4,7] * np.cos(eps) - k_beta

    A[5,0] = -k_l_r / N_r
    A[5,2] = 1 - k_gamma_r
    A[5,5] = -V_x * k_l_r / N_r

    A[6,0] = -k_l_f/N_f
    A[6,1] = (- k_l_f) / N_f * w
    A[6,2] = 1 - k_gamma_f
    A[6,3] = (1 - k_gamma_f) * np.sin(eps) + a_n * k_l_f/N_f
    A[6,4] = (1 - k_gamma_f) * np.cos(eps) + (l_b - rho_f * np.cos(eps))* k_l_f/N_f
    A[6,6] = -(V_x * k_l_f) / N_f
    A[6,8] = V_x*np.cos(eps) * k_l_f/N_f
    A[6,9] = - V_x*np.sin(eps) * k_l_f/N_f

    A[7,2] = 1
    A[8,3] = 1
    A[9,4] = 1

    return A
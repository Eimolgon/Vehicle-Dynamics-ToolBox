import numpy as np


g = 9.81                        # Gravity
w = 1.448                       # Wheelbase
eps = np.radians(26.8)          # Caster angle
a_n = 0.105                     # Trail
m_0 = 195                       # Motorcycle mass
b_0 = 0.722                     # CoM longitudinal position
h_0 = 0.482                     # CoM vertical position
I_0xx = 13.5                    # Moments of inertia
I_0xz = 3                       # Moments of inertia
I_0zz = 55                      # Moments of inertia
m = 270                         # Total mass (w/rider)
b = 0.688                       # CoM longitudinal position (w/rider)
h = 0.64                        # CoM vertical position (w/rider)
I_xx = 35.5                     # Moments of inertia (w/rider)
I_xz = -1.7                     # Moments of inertia (w/rider)
I_zz = 59.3                     # Moments of inertia (w/rider)
m_f = 34                        # Front assembly mass
e_f = 0.025                     # Front CoM coordinates 
h_f = 0.6                       # Front CoM coordinates
I_fzz = 0.83                    # Front moment of inertia
I_omega_f = 0.6                 # Front wheel spin inertia
I_omega_r = 0.8                 # Rear wheel spin inertia
c_delta = 1                     # Steering damping

R_f = 0.294                     # Front wheel rolling radius
R_r = 0.299                     # Rear wheel rolling radius
rho_f = 0.064                   # Front tyre cross-section radius 
rho_r = 0.078                   # Rear tyre cross-section radius 
k_alpha_f = 16                  # Front normalised cornering stiffness
k_alpha_r = 14.5                # Rear normalised cornering stiffness
k_gamma_f = 0.85                  # Front normalised camber stiffness
k_gamma_r = 0.95                  # Rear normalised camber stiffness
k_a_f = -0.2                    # Front normalised self-aligning stiffness
k_a_r = -0.2                    # Rear normalised self-aligning stiffness
k_t_f = 0.015                   # Front normalised twist stiffness
k_t_r = 0.018                   # Rear normalised twist stiffness
k_l_f = 160000                  # Front transverse structural stiffness
k_l_r = 140000                  # Rear transverse structural stiffness

l_b = 0.67                      # Fork bending axis position
k_beta = 38000                  # Bending stiffness
m_b = 18                        # Bending mass
e_b = 0                         # Bending mass longitudinal CoM position in front reference system
h_b = 0.35                      # Bending mass vertical CoM position in overall reference system
I_bxx = 0.8                     # Bending mass moment of inertia
I_bzz = I_bxx                   # Bending mass moment of inertia (REVISE)

b_f = w + (e_f + a_n - h_f * np.sin(eps))/np.cos(eps)       # Front CoM longitudinal position in overall reference system
b_b = w + (e_b + a_n - h_b * np.sin(eps))/np.cos(eps)       # Bending mass longitudinal CoM position in overall reference system
z_b = l_b + ((a_n + e_b) * np.sin(eps) - h_b)/np.cos(eps)   # Bending mass vertical CoM position in front reference system



# ----- ----- ----- Aerodynamic parameters ----- ----- -----

CdA = 0.467                     # Aerodynamic drag factor
h_A = 0.35                      # CoP height
l_A = 1.16                      # CoP longitudinal position
rho_air = 1.2041                # Air density
chord = 0.1
span = 0.2
Nwing = 5
Surface = span*chord*Nwing      # Surface
Cl = 0                          # Lift coefficient
ARatio = span/chord             # Aspect ratio
e = 0.8                         # Oswald efficiency number

Cd_0 = 0.0
Cd = Cd_0 + (Cl**2)/(np.pi*ARatio*e)

# ----- ------ ----- Other ----- ----- -----

X_f = 0                         # Front wheel longitudinal force
a_x = 0                         # Acceleration
omega_f_dot = 0
omega_r_dot = 0

N_r_0 = ((w - b)/w) * m * g     # Front static normal force
N_f_0 = (b/w) * m * g           # Rear static normal force




import numpy as np
import matplotlib.pyplot as plt
from labellines import labelLines
from eigen_functions import Damping_ratio, filter_positive_imaginary_part
import MatrixA as A0
import MatrixE as E0


# ----- ----- ----- Lists to store eigenvalues ----- ----- -----
A_total = []
wobble = []
weave = []
chi_weave = []
chi_wobble = []

# ----- ----- ----- Create Damping Factor lines for root loci plot ----- ----- -----
DampingFactor = np.arange(0.1, 0.6, 0.1)
img_df = np.arange(0, 75, 10)
DF_total = []

for ij in DampingFactor:
    real_df = -img_df*ij
    DF_total.append(real_df)


min_speed = 5
max_speed = 100
Speed_range = np.arange(min_speed, max_speed, 1)


# Compute matrix E and its inverse
E = E0.Matrix()
E_inv = np.linalg.inv(E)

# Compute matrix A for each speed
for V_x in Speed_range:
    A = A0.Matrix(V_x)
    A_total.append(A)



'''
Here is the algorithm of the code, we obtain eigenvalues u, 
filter it to leave only the positive imaginary part and then we compute the damping ratio.
'''

fig, ax1 = plt.subplots()

sizecounter = 0
for k in A_total:
    u = np.linalg.eigvals(np.dot(E_inv, k))
    u2 = filter_positive_imaginary_part(u)
    wobble.append(u2[0])
    weave.append(u2[1])
    chi_wobble.append(Damping_ratio(u2[0]))
    chi_weave.append(Damping_ratio(u2[1]))

    ax1.scatter(np.real(u2), np.imag(u2), facecolors="none", edgecolors="black", s=10+sizecounter)
    sizecounter += 1

# Plot settings and annotations
ax1.axvline(x = 0, color = 'k', linestyle = '-')
ax1.set_xlabel('Real part [1/s]')
ax1.set_ylabel('Imaginary part [1/s]')
ax1.set_xlim([-10, 2])
ax1.set_ylim([0, 61])
txtwobble = ('Wobble')
txtweave = ('Weave')
ax1.text(-7, 51, txtwobble, size=15)
ax1.text(-2, 28, txtweave, size=15)
ax1.text(-9, 35, 'Stable', size=12, weight='bold')
ax1.text(0.5, 35, 'Unstable', size=12, weight='bold')
ax1.fill_betweenx(np.arange(0, 66), 0, 10, where=(np.arange(0, 66) >= 0), color='lightgray', alpha=0.5)
ax1.grid()

# Plot damping factor lines
ax1.plot(DF_total[0], img_df, color = 'grey', linestyle = '--', linewidth = 1, label = r'$\zeta = 0.1$')
ax1.plot(DF_total[1], img_df, color = 'grey', linestyle = '--', linewidth = 1, label = r'$\zeta = 0.2$')
ax1.plot(DF_total[2], img_df, color = 'grey', linestyle = '--', linewidth = 1, label = r'$\zeta = 0.3$')
ax1.plot(DF_total[3], img_df, color = 'grey', linestyle = '--', linewidth = 1, label = r'$\zeta = 0.4$')
ax1.plot(DF_total[4], img_df, color = 'grey', linestyle = '--', linewidth = 1, label = r'$\zeta = 0.5$')

#Label damping factor lines
labelLines(ax1.get_lines(), zorder = 5, color = 'k', fontsize = 15, xvals = (-1, -10))

plt.tick_params(labelsize=15)
plt.show()

# Additional plots for stability and damping factor analysis
# Coordinates to shadow unstable zone
x_shadow = np.linspace(0, 105, 100)
y_shadow = np.linspace(5, 5, 100)

fig, ax = plt.subplots()

ax.plot(Speed_range[1:len(Speed_range)-1], weave[1:len(Speed_range)-1], label = 'Weave')
ax.plot(Speed_range[1:len(Speed_range)-1], wobble[1:len(Speed_range)-1], label = 'Wobble')

plt.title(' Influence of speed on weave stability')
plt.xlabel('Longitudinal speed [m/s]')
plt.ylabel('Real part [1/s]')
plt.fill_between(x_shadow, y_shadow, color='lightgray', alpha = 0.5)
plt.hlines(0, 0, 105, colors='k', linestyles='solid')
plt.text(10, 0.5, 'Unstable', size=12, weight='bold')
plt.text(10, -8, 'Stable', size=12, weight='bold')
plt.xlim(0, 105)
plt.legend(loc = 'lower right')
plt.ylim(-10, 2)
plt.grid()

# Zoomed-in plot for stability analysis
xx1, xx2, yy1, yy2 = 92, 95, -0.025, 0.025
axins = ax.inset_axes([0.4, 0.4, 0.3, 0.2],
    xlim=(xx1, xx2), ylim=(yy1, yy2))

axins.plot(Speed_range, weave)
axins.fill_between(x_shadow, y_shadow, color='lightgray', alpha = 0.5)
axins.hlines(0, 0, 105, colors='k', linestyles='solid')
axins.grid()
ax.indicate_inset_zoom(axins, edgecolor="black")

# Damping factor analysis plot
fig_2, ax_2 = plt.subplots()

ax_2.plot(Speed_range[1:len(Speed_range)-1], chi_weave[1:len(Speed_range)-1], label = 'Weave')
ax_2.plot(Speed_range[1:len(Speed_range)-1], chi_wobble[1:len(Speed_range)-1], label = 'Wobble')

plt.title(' Influence of speed on damping factor')
plt.xlabel('Longitudinal speed [m/s]')
plt.ylabel('Damping factor')
plt.hlines(0, 0, 105, colors='k', linestyles='solid')
plt.xlim(0, 105)
plt.ylim(-0.15, 0.6)
plt.legend(loc = 'best')
plt.grid()

xx1_2, xx2_2, yy1_2, yy2_2 = 92, 95, -0.001, 0.001
axins_2 = ax_2.inset_axes([0.55, 0.55, 0.4, 0.4],
    xlim=(xx1_2, xx2_2), ylim=(yy1_2, yy2_2))

axins_2.plot(Speed_range, chi_weave)
axins_2.hlines(0, 0, 105, colors='k', linestyles='solid')
axins_2.grid()
ax_2.indicate_inset_zoom(axins_2, edgecolor="black")

plt.show()
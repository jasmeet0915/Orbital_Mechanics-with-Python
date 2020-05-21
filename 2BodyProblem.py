import numpy as np
from scipy.integrate import ode
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import planetary_data as pd
from OrbitPropagator import OrbitPropagator as op
plt.style.use('dark_background')


cb = pd.earth

if __name__ == "__main__":

    # initial position and velocity magnitude
    r_mag = cb['radius'] + 500.0
    v_mag = np.sqrt(cb['mu']/r_mag)

    # initial position and velocity vectors respectively
    r0 = [r_mag, 0, 0]
    v0 = [0, v_mag, 0]

    # total timespan of one day in seconds
    timespan = 3600 * 24.0

    dt = 100.0

    propagator = op(r0, v0, timespan, dt, cb)
    propagator.propagate()
    propagator.plot_3d(show=True, save=True)



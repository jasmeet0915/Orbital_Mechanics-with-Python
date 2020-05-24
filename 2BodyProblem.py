import numpy as np
from scipy.integrate import ode
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from planetary_data import earth
from OrbitPropagator import OrbitPropagator as op
from central_body import CentralBody
from satellite import Satellite
plt.style.use('dark_background')


if __name__ == "__main__":
    cb = CentralBody("Earth", earth['mass'], earth['radius'], axis_tilt=23.5)

    sphere_x, sphere_y, sphere_z, axis_x, axis_z = cb.plot_attributes()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(sphere_x, sphere_y, sphere_z, cmap="Blues", alpha=0.6)
    axis_y = [0] * axis_x.shape[0]
    print(axis_x.shape)
    print(axis_z.shape)
    print(axis_y)
    ax.plot(axis_x, axis_y, axis_z, 'k--', label="Axis")

    max_val = cb.radius * 10

    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])

    ax.set_title("Orbit Propagation")
    plt.legend()
    plt.show()

    sat1 = Satellite(sat_id=1, name="ISS", center_body=cb.name, sat_type="Station")
    sat1.propagate_with_tle("iss.txt")

    # initial position and velocity magnitude
    r_mag = cb.radius + 500.0
    v_mag = np.sqrt(cb.mu/r_mag)

    # initial position and velocity vectors respectively
    r0 = [r_mag, 0, 0]
    v0 = [0, v_mag, 0]

    # total timespan of one day in seconds
    timespan = 3600 * 24.0

    dt = 100.0


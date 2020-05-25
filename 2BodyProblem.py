import numpy as np
from scipy.integrate import ode
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from data.planetary_data import earth
from OrbitPropagator import OrbitPropagator as op
from central_body import CentralBody
from satellite import Satellite
from data.orbital_elements_data import iss
plt.style.use('dark_background')


def init_central_body():
    cb = CentralBody("Earth", earth['mass'], earth['radius'], axis_tilt=23.5)
    return cb


cb = init_central_body()


def get_orbital_elements(sat_name="iss"):
    a = cb.radius + (iss['perigee height'] + iss['apogee height'])/2
    eles = [a, iss['e'], iss['i'], iss['raan'], iss['arg_perigee'], iss['ma@epoch'], iss['Epoch']]
    period = (24.0*3600.0)/iss['revs/day']
    return eles, period


if __name__ == "__main__":
    cb = init_central_body()
    sphere_coords = cb.plot_attributes()

    '''fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(sphere_x, sphere_y, sphere_z, cmap="Blues", alpha=0.6)
    axis_y = [0] * axis_x.shape[0]
    ax.plot(axis_x, axis_y, axis_z, 'k--', label="Axis")

    max_val = cb.radius * 10

    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])

    ax.set_title("Orbit Propagation")
    plt.legend()
    plt.show()
'''
    # get list of orbital elements for ISS
    coes, timespan = get_orbital_elements("iss")

    # create satellite object and propagate it using orbital elements
    sat1 = Satellite(sat_id=1, name="ISS", center_body=cb, sat_type="Station")
    r0, v0 = sat1.propagate_with_coes(coes)

    r0 = r0.tolist()
    v0 = v0.tolist()

    print(r0)
    print(v0)

    propagtor = op(r0, v0, timespan, dt=100.0, central_body=cb)
    propagtor.propagate()
    propagtor.plot_3d(sphere_coords)




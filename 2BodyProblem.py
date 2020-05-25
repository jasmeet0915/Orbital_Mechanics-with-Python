import numpy as np
from scipy.integrate import ode
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from planetary_data import earth
from OrbitPropagator import OrbitPropagator as op
from central_body import CentralBody
from satellite import Satellite
from orbital_elements_data import iss
plt.style.use('dark_background')


def init_central_body():
    cb = CentralBody("Earth", earth['mass'], earth['radius'], axis_tilt=23.5)
    return cb


def get_orbital_elements(sat_name="iss"):
    a = (iss['perigee height'] + iss['apogee height'])/2
    eles = [a, iss['e'], iss['i'], iss['raan'], iss['arg_perigee'], iss['ma@epoch'], iss['Epoch']]
    period = iss['revs/day']
    return eles


if __name__ == "__main__":
    # initialize central body
    cb = init_central_body()
    sphere_x, sphere_y, sphere_z, axis_x, axis_z = cb.plot_attributes()

    # get list of orbital elements for ISS
    coes = get_orbital_elements("iss")

    # create satellite object and propagate it using orbital elements
    sat1 = Satellite(sat_id=1, name="ISS", center_body=cb.name, sat_type="Station")
    r0, v0 = sat1.propagate_with_coes(coes)



    propagtor = op(r0, v0, )


    dt = 100.0


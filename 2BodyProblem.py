import numpy as np
from scipy.integrate import ode
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from data.planetary_data import earth
from OrbitPropagator import OrbitPropagator as op
from central_body import CentralBody
from satellite import Satellite
from data.orbital_elements_data import iss
import utils
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

    # create satellite object and propagate it using orbital elements
    sat1 = Satellite(sat_id=1, name="ISS", center_body=cb, sat_type="Station")
    sat1r0, sat1v0 = sat1.propagate_with_tle("data/iss.tle")
    sat1r0 = sat1r0.tolist()
    sat1v0 = sat1v0.tolist()
    propagtor1 = op(sat1r0, sat1v0, sat1.period, dt=100.0, central_body=cb)
    propagtor1.propagate()

    sat2 = Satellite(sat_id=2, name="Starlink-31", center_body=cb, sat_type="Communication")
    sat2r0, sat2v0 = sat2.propagate_with_tle("data/starlink-31.tle")
    sat2r0 = sat2r0.tolist()
    sat2v0 = sat2v0.tolist()
    propagtor2 = op(sat2r0, sat2v0, sat2.period, dt=100.0, central_body=cb)
    propagtor2.propagate()

    sat3 = Satellite(sat_id=3, name="NOAA", center_body=cb, sat_type="Weather")
    sat3r0, sat3v0 = sat3.propagate_with_tle("data/noaa.tle")
    sat3r0 = sat3r0.tolist()
    sat3v0 = sat3v0.tolist()
    propagtor3 = op(sat3r0, sat3v0, sat3.period, dt=100.0, central_body=cb)
    propagtor3.propagate()

    sat1_plot = [propagtor1.rs, 'k', sat1.name]
    sat2_plot = [propagtor2.rs, 'g', sat2.name]
    sat3_plot = [propagtor3.rs, 'm', sat3.name]

    satellites_rs = [sat1_plot, sat2_plot, sat3_plot]

    utils.plot_orbits(sphere_coords, satellites_rs)




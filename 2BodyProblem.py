import numpy as np
from scipy.integrate import ode
from matplotlib import pyplot as plt

earth_radius = 6372.0
earth_mu = 398600.0     # product of mass of earth and gravitational constant


# function to numerically calculate the derivatives of the state of the object
# which consists of position vector and velocity vector
# Those derivative values are passed to the ode solver of scipy module which integrate
# the velocity to calculate the position and integrate the accl. to get velocity
def diff_y(t, y, mu):
    rx, ry, rz, vx, vy, vz = y

    # position vector
    r = np.array([rx, ry, rz])

    # magnitude of r also known as the norm of vector r
    mag_r = np.linalg.norm(r)

    # accleration of the body calculated using newton's law of gravitation
    ax, ay, az = -(r * mu)/mag_r**3

    # we return the derivavtive of position(velocity) and derivative of velocity(accleration)
    return [vx, vy, vz, ax, ay, az]


if __name__ == "__main__":

    # initial position and velocity magnitude
    r_mag = earth_radius + 500.0
    v_mag = np.sqrt(earth_mu/r_mag)

    # initial state vectors, position and vector
    # both vectors made relative to the centre of earth
    # velocity will be in direction perpendicular to the position as it is circular motion
    r0 = [r_mag, 0, 0]
    v0 = [0, v_mag, 0]

    # total timespan for the simulation which is equal to period of the orbit in seconds(s)
    timespan = 100 * 60.0

    # timestep the smaller the value, more accurate will be the orbit
    dt = 100.0

    # total number of timesteps, position and velocity will be calculated for each timestep
    # and then used to plot the orbit. np.ceil gives the nearest integer value
    steps = int(np.ceil(timespan/dt))

    # an empty matrix initialized to store the state of the satellite, position & velocity
    # for each time step taken
    ys = np.zeros((steps, 6))
    # a column vector for all the timesteps
    ts = np.zeros((steps, 1))

    # initial conditions and insert into ys as state for the first state
    y0 = r0 + v0
    ys[0] = np.array(y0)
    step_count = 1

    solver = ode(diff_y)
    solver.set_integrator('lsoda')
    solver.set_initial_value(y0, 0)     # initial state & time
    solver.set_f_params(earth_mu)


    # loop to propagate through the orbit step by step
    while solver.successful() and step_count < steps:
        solver.integrate(solver.t+dt)
        ts[step_count] = solver.t
        ys[step_count] = solver.y
        step_count = step_count + 1

    # get position for all the steps in orbit so that it can be plotted
    rs = ys[:, :3]

    print(rs)
    print(rs.shape)



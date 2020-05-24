import numpy as np

# Universal Gravitational Constant
G_m = 6.67408e-11
G_km = G_m*10**-9


class CentralBody:
    def __init__(self, name, mass, radius, tilt, axis_tilt=0, rotation_period=0):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.tilt = tilt
        self.axis_tilt = axis_tilt
        self.rotation_period = rotation_period

        self.mu = G_km * self.mass

    def plot_attributes(self):
        # plot central_body using polar coordinates of sphere
        _u, _v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
        _x = self.radius * np.cos(_u) * np.sin(_v)
        _y = self.radius * np.sin(_u) * np.sin(_v)
        _z = self.radius * np.cos(_v)



# Universal Gravitational Constant
G_m = 6.67408e-11
G_km = G_m*10**-9


class CentralBody:
    def __init__(self, name, mass, radius, tilt, axis_tilt, rotation_period):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.tilt = tilt
        self.axis_tilt = axis_tilt
        self.rotation_period = rotation_period

        self.mu = G_km * self.mass

import numpy as np
from scipy.integrate import ode


class OrbitPropagator:
    def __init__(self, r0, v0, timespan, dt, central_body):
        self.r0 = r0
        self.v0 = v0
        self.timespan = timespan
        self.dt = dt
        self.central_body = central_body



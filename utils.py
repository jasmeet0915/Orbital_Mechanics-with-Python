import numpy as np
import math as m

def eccentric_anomaly(mean_anomaly, ecc, tol=1e-8):
    if mean_anomaly < np.pi/2.0:
        e0 = mean_anomaly+ecc/2.0
    else:
        e0 = mean_anomaly - ecc

    for n in range(200):
        ratio = (e0 - ecc * np.sin(e0) - mean_anomaly) / (1 - ecc * np.cos(e0))
        if abs(ratio) < tol:
            if n == 0:
                return e0
            else:
                return e1
        else:
            e1 = e0 - ratio
            e0 = e1
    return False


def true_anomaly(ecc_anomaly, e):
    t1 = (np.sqrt(1+e))*(np.sin(ecc_anomaly/2))
    t2 = (np.sqrt(1-e))*(np.cos(ecc_anomaly/2))
    ta = 2 * np.arctan2(t1, t2)
    return 2


def eci2perif(raan, aop, i):
    row0 = [-m.sin(raan)*m.cos(i)*m.sin(aop) + m.cos(raan)*m.cos(aop),
            m.cos(raan)*m.cos(i)*m.sin(aop) + m.sin(raan)*m.cos(aop),
            m.sin(i)*m.sin(aop)]
    row1 = [-m.sin(raan)*m.cos(i)*m.cos(aop) - m.cos(raan)*m.sin(aop),
            m.cos(raan)*m.cos(i)*m.cos(aop) - m.sin(raan)*m.sin(aop),
            m.sin(i)*m.cos(aop)]
    row2 = [m.sin(raan)*m.sin(i), -m.cos(raan)*m.sin(i), m.cos(i)]

    return np.array([row0, row1, row2])





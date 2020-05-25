import numpy as np
import utils

# conversion factor for degree to radian conversion
degree2rad = np.pi/180


class Satellite:
    def __init__(self, sat_id, name, center_body, sat_type):
        self.sat_id = sat_id
        self.name = name
        self.sat_type = sat_type
        self.center_body = center_body

    def propagate_with_coes(self, orbital_elements):
        self.orbital_elements = orbital_elements
        a, e, i, raan, arg_periapsis, mean_anomaly, epoch = self.orbital_elements
        i = i * degree2rad
        arg_periapsis = arg_periapsis * degree2rad
        mean_anomaly = mean_anomaly * degree2rad
        raan = raan * degree2rad

        # eccentricity anomaly at epoch calculated using mean anomaly at epoch
        ecc_anomaly = utils.eccentric_anomaly(mean_anomaly, e)


    """Use this function if you want to use satellite TLE data to plot the orbit
    path: path to the file containing the TLE data"""
    def propagate_with_tle(self, path):
        with open(path, 'r') as f:
            lines = f.readlines()

        # name of satellite
        line0 = lines[0].strip()
        # TLE data
        line1 = lines[1].strip().split()
        line2 = lines[2].strip().split()

        print(line0)
        print(line1)
        print(line2)

        # to do: change the check as person may not enter exactly same name as the one in tle
        # this is a condition that checks to see if the correct tle data is loaded
        if line0 != self.name:
            print("Name of satellite object does not match name on TLE!!")



import numpy as np


class Satellite:
    def __init__(self, sat_id, name, center_body, sat_type):
        self.sat_id = sat_id
        self.name = name
        self.sat_type = sat_type
        self.center_body = center_body

    '''Use this function to plot orbit of the satellite using Classical/Keplerian
     Orbital Elements. Required Parameters:
     e: eccentricity of the orbit, it is the value that determines the shape of the orbit
     a: semi-major axis, this vale determines the size of the orbit, it is equal to radius in
                         case of circular orbit
     inclination: inclination of orbit in degrees from the equatorial plane of the central body
     asc_node_long: Longitude of Ascending Node, angle b/w asc_node and vernal equinox
     arg_periapsis: argument of periapsis, angle b/w periapsis and asc_node in orbital plane'''
    def propagate_with_coes(self, e, a, inclination, asc_node_long,
                            arg_periapsis, period):
        self.e = e
        self.a = a
        self.inclination = inclination
        self.asc_node_long = asc_node_long
        self.arg_periapsis = arg_periapsis
        self.period = period

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



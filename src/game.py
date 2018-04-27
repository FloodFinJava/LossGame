# -*- coding: utf-8 -*-

"""Provide the functions to run the flood risk game
"""

import random

def distribute_inhabited_points(extent, n_points):
    """Randomly select a n number of points inside a given extent
    return two lists of lat/long coordinates
    """
    lat = []
    lon = []
    for n in range(n_points):
        lat.append(random.uniform(extent['latmin'], extent['latmax']))
        lon.append(random.uniform(extent['lonmin'], extent['lonmax']))
    return lat, lon

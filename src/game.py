# -*- coding: utf-8 -*-

"""Provide the functions to run the flood risk game
"""

import numpy as np

def distribute_points(extent, n_points):
    """Randomly select a n number of points inside a given extent
    return two lists of lat/long coordinates
    """
    lat = np.random.uniform(low=extent['latmin'], high=extent['latmax'], size=n_points)
    lon = np.random.uniform(low=extent['lonmin'], high=extent['lonmax'], size=n_points)
    return lat, lon

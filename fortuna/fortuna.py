"""
Fortuna

Python project to visualize uncertatinty.

Created on 09/06/2018

@authors: Natalia Shchukina, Graham Brew, Marco van Veen, Behrooz Bashokooh, Tobias Stål, Robert Leckenby
"""

# Import libraries

import numpy as np
import glob
from matplotlib import pyplot as plt
import pandas as pd
import xarray as xr
import pyproj as proj
from scipy.stats import norm



class Fortuna(object):
    """
    Class to load the fortuna dataset and call different methods for visualization in a web frontend.

    Args:
        There are no required arguments at the moment. Input files could be defined.

    Keyword Args:
        scalar_field(numpy.ndarray): 3D array containing a individual potential field
        verbose(int): Level of verbosity during the execution of the functions (up to 5). Default 0
    """

    def __init__(self, **kwargs):
        """
        Method that is called when a object of the class Fortuna is initiated, it imports the data and directly creates some important variables.
        """

        self.size_raster = (250,162)

        self.base_cube, self.base_n = folder2cube('data/Hackaton/BaseSet/MapSimu__*.data', size_raster)
        self.top_cube, self.top_n = folder2cube('data/Hackaton/TopSet/MapSimu__*.data', size_raster)

        self.vol = pd.read_csv('data/Hackaton/VolumeDistribution/Volumes', delim_whitespace=True)


    def folder2cube(files, size_raster):
        """
        Function to import data from files.
        """
        base_set = glob.glob(files)
        cube = np.zeros(size_raster + (len(base_set),))
        for i, model in enumerate(base_set):
            cube[:, :, i] = np.loadtxt(model, skiprows=1).reshape(size_raster)
        return cube, len(base_set)




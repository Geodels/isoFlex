# Example usage
################################
#
# Running using for example 10 processors
# mpirun -np 10 python3 runflex.py
#
#
# Options for initialization
# xxxxxxxxxxxxxxxxxxxxxx
# 
#
# Input dataset is specified by either 'filename', 'dsin', or 'data'
#
# Case 1:
# -------
# in case where 'filename' is chosen a netcdf file is required
# with the following variables should be provided:
#   - 'erodep': erosion deposition thickness in metres,
#   - 'te': elastic thickness in metres
#
# Case 2:
# -------
# Similarly if a xarray dataset is given ('dsin') it should contain the
# same variable names (i.e., 'erodep', 'te').
# 
# The resolution for the input dataset (either filename or dsin) needs
# to be in longitude/latitude and be 0.25 deg resolution.
# Dimensions:    (latitude: 721, longitude: 1441).
#
# Coordinates:
#   * latitude   (latitude) float64 6kB -90.0 -89.75 -89.5 ... 89.5 89.75 90.0
#   * longitude  (longitude) float64 12kB -180.0 -179.8 -179.5 ... 179.8 180.0
# Data variables:
#     erodep     (latitude, longitude) float64 8MB ...
#     te         (latitude, longitude) float64 8MB ...
#
# Case 3:
# -------
# Optionally one might want to give scattered values distributed across the globe 
# in cartesian coordinates.
#  In such a case the user needs to use the 'data' variable as a numpy array of
# dimensions (n,5) where n is the number of records on the globe and 5 corresponds
# to the following X,Y,Z,erodep,te
# A Kd-tree interpolation will then be performed to map the variables in a
# regular lon/lat mesh.
#
# Additional parameters
# xxxxxxxxxxxxxxxxxxxxxx
#
# The flexural response could be saved in a netcdf file defined in 'fileout'.
#
# Young's Modulus `young` (default 65.e9),
# Poisson's Ratio `nu` (default 0.25),
# Mantle density `rho_m` (default 3300),
# Sediment density `rho_s` (default 2300)
#
################################

from isoflex.model import Model as iflex

model = iflex(filename='data/init_conditions.nc',
              fileout='data/cpt_flex.nc',
              verbose=True)

model.runFlex(False)
